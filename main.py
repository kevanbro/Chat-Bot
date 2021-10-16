import Constents as keys
from telegram.ext import*
import Responses as R

print("Bot started...(A bot by @SanilaRanatunga)")


def start_command(update, context):
    update.message.reply_text('Welcome to Useful & Powerful Chat bot🤗\nJust type random to get started✍\nHavent any idea about hove to use me🤔 type /help\n(A bot by @SanilaRanatunga)')


def help_command(update, context):
    update.message.reply_text('Just send me the command that you want🙂\n/song - I will download songs for you📩\n/video - I will download youtube videos for you📩\n/torrent - I will download torrent files to you📩\n/feedback - Send me problems and errors in this bot☺')


def song_command(update, context):
    update.message.reply_text('📨Use this telegram bot link to download songs. t.me/songdownload597_bot')

def feedback_command(update, context):
    update.message.reply_text("Are there any problems in this bot🤔 or have you any idea that should in this bot💡\nSend your problems - @SanilaRanatunga\nThanks for connecting with us🤗❤")

def video_command(update, context):
    update.message.reply_text('📨Use this telegram bot link to download youtube videos. t.me/youtubevideodownloader45_bot')

def torrent_command(update, context):
        update.message.reply_text('📨Use this telegram bot to download torrent files. t.me/torrentdownloader55_bot')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("song", song_command))
    dp.add_handler(CommandHandler("video", video_command))
    dp.add_handler(CommandHandler("torrent", torrent_command))
    dp.add_handler(CommandHandler("feedback", feedback_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
