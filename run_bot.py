import bot
import keep_alive

if __name__ == '__main__':
    keep_alive.keep_alive()
    bot.bot.polling(none_stop=True)