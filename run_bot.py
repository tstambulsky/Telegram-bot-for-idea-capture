import telebot
import schedule
import time
from datetime import datetime, timedelta
import threading
import json
from openai import OpenAI

# Configuración: recomendable hacerlo con variables de entorno
CONFIG = {
    'TELEGRAM_TOKEN': 'TELEGRAM_TOKEN',
    'OPENAI_API_KEY': 'OPEN AI API KEY',
    'OPENAI_MODEL': 'gpt-4o-mini'
}

# Módulo de OpenAI
class OpenAIModule:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def parse_reminder(self, text):
        response = self.client.chat.completions.create(
            model=CONFIG['OPENAI_MODEL'],
            messages=[
                {"role": "system", "content": "Eres un asistente que ayuda a configurar recordatorios. Extrae la duración en horas (o fracciones de hora) y el mensaje del recordatorio del texto del usuario. Responde con un JSON que contiene 'hours' (número) y 'message' (string). Si el tiempo está en minutos, conviértelo a horas."},
                {"role": "user", "content": text}
            ]
        )
        
        parsed = response.choices[0].message.content
        print(f"Respuesta de OpenAI: {parsed}")  # Log para depuración
        try:
            result = json.loads(parsed)
            hours = result.get('hours')
            message = result.get('message')
            if hours is not None and message:
                return float(hours), message
        except json.JSONDecodeError as e:
            print(f"Error al procesar JSON: {e}")  # Log para depuración
        return None, None

    def personalize_reminder(self, message):
        response = self.client.chat.completions.create(
            model=CONFIG['OPENAI_MODEL'],
            messages=[
                {"role": "system", "content": "Eres un asistente amigable. Tu tarea es personalizar un recordatorio para hacerlo más motivador y específico."},
                {"role": "user", "content": f"Personaliza este recordatorio de forma amigable y motivadora: {message}"}
            ]
        )
        return response.choices[0].message.content.strip()

# Módulo de Recordatorios
class ReminderModule:
    def __init__(self, bot, openai_module):
        self.reminders = {}
        self.bot = bot
        self.openai_module = openai_module

    def add_reminder(self, chat_id, hours, message):
        reminder_time = datetime.now() + timedelta(hours=hours)
        personalized_message = self.openai_module.personalize_reminder(message)
        self.reminders[chat_id] = (reminder_time, personalized_message)

    def check_reminders(self):
        now = datetime.now()
        for chat_id, (reminder_time, reminder_text) in list(self.reminders.items()):
            if now >= reminder_time:
                self.send_reminder(chat_id, reminder_text)
                del self.reminders[chat_id]

    def send_reminder(self, chat_id, message):
        self.bot.send_message(chat_id, f"¡Recordatorio! {message}")

# Módulo del Bot de Telegram
class TelegramBot:
    def __init__(self, token, openai_module):
        self.bot = telebot.TeleBot(token)
        self.openai_module = openai_module
        self.reminder_module = ReminderModule(self.bot, openai_module)

    def handle_message(self, message):
        print(f"Mensaje recibido: {message.text}")  # Log para depuración
        hours, reminder_text = self.openai_module.parse_reminder(message.text)
        print(f"Horas interpretadas: {hours}")  # Log para depuración
        print(f"Mensaje interpretado: {reminder_text}")  # Log para depuración
        
        if hours is not None and reminder_text is not None:
            self.reminder_module.add_reminder(message.chat.id, hours, reminder_text)
            
            schedule.every().minute.do(self.reminder_module.check_reminders)
            
            if hours < 1:
                minutes = int(hours * 60)
                self.bot.reply_to(message, f"Entendido. Te recordaré '{reminder_text}' en aproximadamente {minutes} minutos (a las {(datetime.now() + timedelta(hours=hours)).strftime('%H:%M')} horas).")
            else:
                self.bot.reply_to(message, f"Entendido. Te recordaré '{reminder_text}' en aproximadamente {hours:.1f} horas (a las {(datetime.now() + timedelta(hours=hours)).strftime('%H:%M')} horas).")
        else:
            self.bot.reply_to(message, "Lo siento, no pude entender tu solicitud de recordatorio. Por favor, intenta ser más específico con el tiempo y el mensaje del recordatorio. Por ejemplo: 'Recuérdame tomar agua en 30 minutos' o 'Recuérdame llamar a mamá en 2 horas'.")

    def run(self):
        @self.bot.message_handler(func=lambda message: True)
        def message_handler(message):
            self.handle_message(message)

        print("Bot iniciado y esperando mensajes...")
        scheduler_thread = threading.Thread(target=self.run_scheduler)
        scheduler_thread.start()
        self.bot.polling()

    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

# Función principal
def main():
    openai_module = OpenAIModule(CONFIG['OPENAI_API_KEY'])
    bot = TelegramBot(CONFIG['TELEGRAM_TOKEN'], openai_module)
    bot.run()

if __name__ == "__main__":
    main()