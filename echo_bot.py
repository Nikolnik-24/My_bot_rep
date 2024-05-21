# Libraries:
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

# Inforbations:
BOT_TOKEN = '6977974410:AAE90eYwQuznUSLtf_rk3L1ClEgdeRlbHA4'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Hendlers:

# /start
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ Test-bot(echo_bot)\nНапиши мне что-нибудь\n'
                         '/start - Начать диалог\n'
                         '/help - Что умееет этот бот\n')


# /help
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Режим эхо-бота\nОтправь что-угодно и бот перешлет тебе это:\n'
                         'All text message\n'
                         'Photo\n'
                         'Audio\n'
                         'Video\n'
                         'Sticker\n'
                         'Video_note\n'
                         'Voice\n'
                         'Document\n'
                         'Animation\n')


# Photo
@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


# Audio
@dp.message(F.audio)
async def send_audio_echo(message: Message):
    await message.reply_audio(message.audio.file_id)


# Video
@dp.message(F.video)
async def send_video_echo(message: Message):
    await message.reply_video(message.video.file_id)


# Sticker
@dp.message(F.sticker)
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)


# Video_note
@dp.message(F.video_note)
async def send_video_note_echo(message: Message):
    await message.answer_video_note(message.video_note.file_id)


# Voice
@dp.message(F.voice)
async def send_voice_echo(message: Message):
    await message.answer_voice(message.voice.file_id)


# Document
@dp.message(F.document)
async def send_document_echo(message: Message):
    await message.answer_document(message.document.file_id)


# Animation
@dp.message(F.animation)
async def send_animation_echo(message: Message):
    await message.ansewer_animation(message.animation.file_id)


# all message
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

# Registration hendlers
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_video_note_echo, F.video_note)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_document_echo, F.document)
dp.message.register(send_animation_echo, F.animation)
dp.message.register(send_echo)

# Finish:
if __name__ == '__main__':
    dp.run_polling(bot)

"Сохранение на PC"