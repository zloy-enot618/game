import random
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import sys
import time
import speech_recognition as sr

### СЛОВА НА АНГЛ
en_words_ez = ["cat", "dog", "house", "hello", "goodbye"]
en_words_mid = ["apartaments", "soccer", "angry", "weather", "ball"]
en_words_hard = ["Domain Name System", "request", "english", "speak", "Russia"]
### Конец слов на англ

### ИХ ПЕРЕВОД
ru_tr_ez = ["кот", "собака", "дом", "привет", "пока"]
ru_tr_mid = ["апартаменты", "футбол", "злой", "погода", "мяч"]
ru_tr_hard = ["Система доменных имён", "запрос", "английский", "говорить", "Россия"]
# Конец их перевода

#Speech test
en_speech = ["Hello my friend", "I love my country", "I love Russia"]
ru_speech = ["Привет мой друг", "Я люблю мою страну", "Я люблю Россию"]
#Конец speech test

delay = 0
result = 0

def hello(name):
    print(f'Здравствуй, {name}! Хочешь принять участие в игре? ', end=' ')
    a338 = input()
    if a338.lower() == 'да':
        return
    elif a338.lower() == 'нет':
        print('До свидания!')
        sys.exit()


#СЕРДЦЕ ПРОЕКТА часть 1
def translate_quest(delay, result, name):
    print(f"Приготовьтесь, {name}! Игра началась!")
    if delay == 20:
        yui1 = random.randrange(len(en_words_ez))
        qustus1 = en_words_ez[yui1]
        qustus1_pre = ru_tr_ez[yui1]
        answ1 = input(f"{name}, как переводится {qustus1}?  ")
        if answ1 == qustus1_pre:
            print("ВЫ ПОБЕДИЛИ!")
            result = 1
            return result
        else:
            print("Вы проиграли! Получится в следующий раз!")
            result = 20
            return result
    elif delay == 10:
        yui2 = random.randrange(len(en_words_mid))
        qustus2 = en_words_mid[yui2]
        qustus2_pre = ru_tr_mid[yui2]
        answ2 = input(f"{name}, как переводится {qustus2}?  ")
        if answ2 == qustus2_pre:
            print("ВЫ ПОБЕДИЛИ!!!")
            result = 2
            return result
        else:
            print("Вы проиграли! Получится в следующий раз!")
            result = 20
            return result
    elif delay == 5:
        yui3 = random.randrange(len(en_words_hard))
        qustus3 = en_words_hard(yui3)
        qustus3_pre = ru_tr_hard(yui3)
        answ3 = input(f"{name}, как переводится {qustus3}?  ")
        if answ3 == qustus3_pre:
            print("ВЫ ПОБЕДИЛИ!!!!!!")
            result = 3
            return result
        else:
            print("Вы проиграли! Получится в следующий раз!")
            result = 20
            return result
#Конец части 1

#СЕРДЦЕ ПРОЕКТА часть 2
def speech_quest(name, result):
    print(f"{name}, сейчас вам выпадет рандомное выражение на русском, а вы скажите на английском.")
    random_rus = random.randrange(len(ru_speech))
    ru_sp1 = ru_speech[random_rus]
    eng_sp1 = en_speech[random_rus]
    print(f'{name}, произнесите эту фразу: "{ru_sp1}" на английском.')
    sample_rate = 44100
    duration = 7
    print(f"{name}, говорите. У вас 7 секунд. Ctrl+C, чтобы выйти.")
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype='int16'
    )
    sd.wait()
    wav.write("voice.wav", sample_rate, recording)
    print("Распознаём текст...")
    recognizer = sr.Recognizer()
    with sr.AudioFile("voice.wav") as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="en-US")
        if eng_sp1.lower() == text.lower():
            print("Вы победили!")
            result = 4
            return result
        elif eng_sp1.lower() != text.lower():
            print('Вы проиграли! Получится в другой раз!')
            result = 20
            return result
    except sr.UnknownValueError:          
        print("Не удалось распознать речь. Попробуйте ещё раз.")
    except sr.RequestError as e:          
        print(f"Ошибка сервиса: {e}. Пожалуйста, попробуйте в другой раз.")
#Конец части 2

time.sleep(0.33333)
print('Введите ваше имя, чтобы мы могли к вам обращаться:    ', end=' ')
name = input()
hello(name)
print(f'{name}, приятно познакомиться. Выберите уровень сложности.  ')
print(f"\n\n\njunior - 20 секунд на ответ, middle - 10 секунд на ответ, senior - 5 секунд на ответ.")
print(f"{name}, выбирай. Всё зависит только от тебя:    ", end=' ')
while True:
    level = input()
    if level.lower() == 'junior':
        print('Уровень выбран.')
        delay = 20
        break
    elif level.lower() == 'middle':
        print('Уровень выбран.')
        delay = 10
        break
    elif level.lower() == 'senior':
        print('Уровень выбран.')
        delay = 5
        break
    else:
        print(f"{name}, я вас не понимаю. Введите указанные выше варианты или нажмите CTRL+C, чтобы аварийно завершить выполнение кода.")
print(f'{name}, выберите испытание из указанных ниже.')
print(f"\n1: Перевести английское слово на русский за {delay} секунд.\n2: Русское слово/фразу сказать по английски за {delay} секунд.")

while True:
    tyrt = input("")
    if tyrt == '1':
        translate_quest(delay, result, name)
        break
    elif tyrt == '2':
        speech_quest(name, result)
    else:
        print(f"{name}, я вас не понимаю. Выберите число из указанных выше или нажмите CTRL+C для аварийного завершения выполнения кода.")
print("ВЫ ПОБЕДИЛИ!")
if result == 1:
    print('Вы прошли тест по переводу на лёгкий уровень. Так держать!')
elif result == 2:
    print("Вы прошли тест по переводу на средний уровень. Вы уже продвинуты в английском!")
elif result == 3:
    print("ВЫ ПРОШЛИ САМУЮ СЛОЖНУЮ ВЕРСИЮ ТЕСТА НА ПЕРЕВОД! ВЫ ГЕНИЙ В АНГЛИЙСКОМ!")
elif result == 20:
    print("Вы не прошли тест :(. Удачи в следующий раз!")
elif result == 4:
    print('Круто! Вы смогли пройти испытание! Удачи!')