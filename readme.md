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
     python run_bot.py
     ```
   - For the English version:
     ```
     python run_bot_english.py
     ```

2. Open Telegram and start a chat with your bot.

3. Send a voice note with your idea.

4. The bot will process your idea and respond with a confirmation.

5. Check your email for the expanded version of your idea.

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