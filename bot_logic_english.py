import telebot
import schedule
import time
from datetime import datetime, timedelta
import threading
import json
from openai import OpenAI

# Configuration: recommended to use environment variables
CONFIG = {
    'TELEGRAM_TOKEN': 'TELEGRAM_TOKEN',
    'OPENAI_API_KEY': 'OPEN AI API KEY',
    'OPENAI_MODEL': 'gpt-4o-mini'
}

# OpenAI Module
class OpenAIModule:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def parse_reminder(self, text):
        response = self.client.chat.completions.create(
            model=CONFIG['OPENAI_MODEL'],
            messages=[
                {"role": "system", "content": "You are an assistant that helps set reminders. Extract the duration in hours (or fractions of an hour) and the reminder message from the user's text. Respond with a JSON containing 'hours' (number) and 'message' (string). If the time is in minutes, convert it to hours."},
                {"role": "user", "content": text}
            ]
        )
        
        parsed = response.choices[0].message.content
        print(f"OpenAI Response: {parsed}")  # Debug log
        try:
            result = json.loads(parsed)
            hours = result.get('hours')
            message = result.get('message')
            if hours is not None and message:
                return float(hours), message
        except json.JSONDecodeError as e:
            print(f"Error processing JSON: {e}")  # Debug log
        return None, None

    def personalize_reminder(self, message):
        response = self.client.chat.completions.create(
            model=CONFIG['OPENAI_MODEL'],
            messages=[
                {"role": "system", "content": "You are a friendly assistant. Your task is to personalize a reminder to make it more motivating and specific."},
                {"role": "user", "content": f"Personalize this reminder in a friendly and motivating way: {message}"}
            ]
        )
        return response.choices[0].message.content.strip()

# Reminders Module
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
        self.bot.send_message(chat_id, f"Reminder! {message}")

# Telegram Bot Module
class TelegramBot:
    def __init__(self, token, openai_module):
        self.bot = telebot.TeleBot(token)
        self.openai_module = openai_module
        self.reminder_module = ReminderModule(self.bot, openai_module)

    def handle_message(self, message):
        print(f"Message received: {message.text}")  # Debug log
        hours, reminder_text = self.openai_module.parse_reminder(message.text)
        print(f"Interpreted hours: {hours}")  # Debug log
        print(f"Interpreted message: {reminder_text}")  # Debug log
        
        if hours is not None and reminder_text is not None:
            self.reminder_module.add_reminder(message.chat.id, hours, reminder_text)
            
            schedule.every().minute.do(self.reminder_module.check_reminders)
            
            if hours < 1:
                minutes = int(hours * 60)
                self.bot.reply_to(message, f"Understood. I'll remind you '{reminder_text}' in approximately {minutes} minutes (at {(datetime.now() + timedelta(hours=hours)).strftime('%H:%M')}).")
            else:
                self.bot.reply_to(message, f"Understood. I'll remind you '{reminder_text}' in approximately {hours:.1f} hours (at {(datetime.now() + timedelta(hours=hours)).strftime('%H:%M')}).")
        else:
            self.bot.reply_to(message, "Sorry, I couldn't understand your reminder request. Please try to be more specific with the time and reminder message. For example: 'Remind me to drink water in 30 minutes' or 'Remind me to call mom in 2 hours'.")

    def run(self):
        @self.bot.message_handler(func=lambda message: True)
        def message_handler(message):
            self.handle_message(message)

        print("Bot started and waiting for messages...")
        scheduler_thread = threading.Thread(target=self.run_scheduler)
        scheduler_thread.start()
        self.bot.polling()

    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

# Main function
def main():
    openai_module = OpenAIModule(CONFIG['OPENAI_API_KEY'])
    bot = TelegramBot(CONFIG['TELEGRAM_TOKEN'], openai_module)
    bot.run()

if __name__ == "__main__":
    main()