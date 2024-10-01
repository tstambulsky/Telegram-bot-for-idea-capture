# Bot de Telegram para Captura de Ideas

## Descripción

Este bot de Telegram permite a los usuarios capturar ideas rápidamente mediante notas de voz. El bot procesa estas notas, expande las ideas utilizando inteligencia artificial y envía una versión detallada por correo electrónico. Es perfecto para capturar pensamientos fugaces o inspiraciones cuando estás en movimiento.

## Características

- Recibe notas de voz a través de Telegram
- Procesa e interpreta el contenido de las notas de voz
- Expande la idea inicial utilizando IA
- Envía versiones detalladas de las ideas por correo electrónico
- Establece recordatorios para seguimiento de tus ideas

## Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente:

- Python 3.7+
- Un Token de Bot de Telegram (obtenido de BotFather)
- Una clave de API de OpenAI
- (Opcional) Una clave de API de servicio de correo electrónico (si se implementa la funcionalidad de correo)

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tstambulsky/Telegram-bot-for-idea-capture.git
   cd Telegram-bot-for-idea-capture
   ```

2. Instala las dependencias requeridas:
   ```
   pip install -r requirements.txt
   ```

3. Configura las variables de entorno:
   - `TELEGRAM_TOKEN`: Tu Token de Bot de Telegram
   - `OPENAI_API_KEY`: Tu clave de API de OpenAI

## Uso

1. Inicia el bot:
   ```
   python bot_logic.py
   ```

2. Abre Telegram e inicia un chat con tu bot.

3. Envía una nota de voz con tu idea.

4. El bot procesará tu idea y responderá con una confirmación.

5. Revisa tu correo electrónico para ver la versión expandida de tu idea.

## Contribuir

Las contribuciones al Bot de Captura de Ideas son bienvenidas. Por favor, sigue estos pasos:

1. Haz un fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/caracteristica-asombrosa`)
3. Realiza tus cambios
4. Haz commit de tus cambios (`git commit -m 'Añadir alguna característica asombrosa'`)
5. Haz push a la rama (`git push origin feature/caracteristica-asombrosa`)
6. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.

## Agradecimientos

- OpenAI por proporcionar el modelo de IA utilizado en la expansión de ideas
- Los contribuidores de la biblioteca Python Telegram Bot

## Contacto

Si tienes alguna pregunta o comentario, por favor abre un issue en este repositorio o contacta [tu-email@ejemplo.com].