import speech_recognition as sr
from gtts import gTTS
import os

# Загрузка аудиофайла
audio_file = "audio.wav"
r = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data, language="ru-RU")

# Добавление слова к тексту
new_text = text + " получилось добавить текст"

# Преобразование текста в речь и сохранение в аудиофайл
tts = gTTS(text=new_text, lang='ru')
tts.save("output.mp3")

# Воспроизведение аудиофайла
os.system("start output.mp3")