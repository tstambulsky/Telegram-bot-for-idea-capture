# Telegram Bot for Idea Capture

## Description

This Telegram bot allows users to quickly capture ideas using voice notes. The bot then processes these notes, expands on the ideas using artificial intelligence, and sends a detailed version via email. It's perfect for capturing fleeting thoughts or inspirations when you're on the go.

## Features

- Receive voice notes through Telegram
- Process and interpret the content of voice notes
- Expand on the initial idea using AI
- Send detailed versions of the ideas via email
- Set reminders for follow-ups on your ideas

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- A Telegram Bot Token (obtain from BotFather)
- An OpenAI API key
- (Optional) An email service API key (if implementing email functionality)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/tstambulsky/Telegram-bot-for-idea-capture.git
   cd Telegram-bot-for-idea-capture
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - `TELEGRAM_TOKEN`: Your Telegram Bot Token
   - `OPENAI_API_KEY`: Your OpenAI API key

## Usage

1. Start the bot:
   - For the Spanish version:
     ```
     python bot_logic.py
     ```
   - For the English version:
     ```
     python bot_logic_english.py
     ```

2. Open Telegram and start a chat with your bot.

3. Send a voice note with your idea.

4. The bot will process your idea and respond with a confirmation.

5. Check your email for the expanded version of your idea.

## Deployment on PythonAnywhere

This project includes two additional files for deployment on PythonAnywhere:

### keep_alive.py

This file creates a simple Flask web application to keep the bot alive on PythonAnywhere. It does the following:

1. Sets up a Flask app that responds with "Bot is alive!" when accessed.
2. Creates a thread to run the Flask app.
3. Implements a `ping_self()` function that sends a request to the bot's URL every 5 minutes to prevent it from going to sleep.

To use this file:
1. Replace `USER_NAME` in the URL with your PythonAnywhere username.
2. Ensure you have the `flask` and `requests` libraries installed.

### run_bot.py

This file is the entry point for running the bot on PythonAnywhere. It does the following:

1. Imports the main bot logic and the keep_alive module.
2. Calls the `keep_alive()` function to start the Flask app thread.
3. Starts the bot polling process to listen for incoming messages.

To run the bot on PythonAnywhere:
1. Upload both `keep_alive.py` and `run_bot.py` to your PythonAnywhere account.
2. Set up a new web app on PythonAnywhere and point it to the Flask app in `keep_alive.py`.
3. In the PythonAnywhere bash console, run:
   ```
   python run_bot.py
   ```

This setup will keep your bot running continuously on PythonAnywhere, even with the free tier account.

## Contributing

Contributions to the Idea Capture Bot are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- OpenAI for providing the AI model used in idea expansion
- The Python Telegram Bot library contributors

## Contact

If you have any questions or feedback, please open an issue on this repository or contact [your-email@example.com].