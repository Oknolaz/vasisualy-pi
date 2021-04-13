#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Core
from .core import speak
from .core import talk
import random
import speech_recognition
import time

# Skills
from .skills import time_date
from .skills import exit
from .skills import joke
from .skills import weather
from .skills import music
from .skills import open
from .skills import screenshot
from .skills import search
from .skills import poweroff
from .skills import ytvideo
from .skills import resay
from .skills import map
from .skills import wiki
from .skills import location
from .skills import weather_no_city
from .skills import translate
from .skills import news
from .skills import coin
from .skills import upd_upg
from .skills import todolist
from .skills import shoplist
from .skills import netconnection
from .skills import record
from .skills import guess_num
from .skills import rulette
from .skills import math
from .skills import audio
from .skills import crystal_ball
from .skills import random_num
from .skills import timer

wrong = ("Прости, я тебя не понимаю.", "Мне кажется ты несёшь какой-то бред.", "Что?", "Ты, наверное, ошибаешься. Я тебя не понимаю.", "Извини, я появился совсем недавно, я пока понимаю очень мало слов.", "Чего?", "А? Что? Я тебя не понимаю.", "Пожалуйста, не говори слов, которых я незнаю.", "Ты пытаешься оскорбить меня этим?", "Не издевайся надо мной, я знаю не так много слов.", "Извини, я не могу тебя понять.", "А?", "Объясни попроще.", "Пожалуйста, прочитай моё описание. Скорее всего я не умею делать то, что ты меня просишь или попробуй использовать синонимы.", "Ты ошибаешься.", "Я не понимаю твоего вопроса.", "Мне не понятен твой вопрос.", "Не могу понять о чём ты говоришь.", "Я не понимаю.", "О чём ты?", "Я не могу распознать вопрос.") # Ответы на неизвестную команду.
code_words = ("Васисуалий", "васисуалий", "Васися", "васися", "Василий", "василий", "Васямба", "васямба", "Вася", "вася", "Васёк", "васёк", "Васис", "васис")

# Настройки распознавания речи
recognizer = speech_recognition.Recognizer()
recognizer.pause_threshold = 0.5
mph = speech_recognition.Microphone()

randnum = -1
isGuessNum = False
isRuLette = False


class Main():
    def __init__(self):
        speak.speak("Привет, меня зовут Васисуалий. Чем могу быть полезен?")
        self.guessTry = 0
        self.isGuessNum = False
        randnum = 0
        self.isRoulette = False
        self.program()
        
    def program(self):
        # Сама программа
        skillUse = False
        print("[sys] ТИХО!..")
        with mph as source:
            recognizer.adjust_for_ambient_noise(source)
        while True:
            print("[sys] Говорите...")
            with mph as source:
                say = recognizer.listen(source)
            print("[sys] Речь распознаётся...")
            try:
                say = recognizer.recognize_google(say, language="ru-RU")
                say = str(say)
                for code in code_words:
                    if code in say:
                        say.replace(code, "")
                        say = say.lower()
                        say = say.capitalize()
                        print(f"Вы: {say}")
                    else:
                        print(f"Вы: {say}")
            except Exception:
                say = ''
                print("[sys] Не удалось распознать речь. Нет подключения к интернету или не подключен микрофон.")
                
            if time_date.main(say):
                speak.speak(time_date.main(say))
                skillUse = True
                
            elif exit.main(say):
                skillUse = True
                
            elif joke.main(say):
                speak.speak(joke.main(say))
                skillUse = True
                
            elif weather.main(say):
                skillUse = True
                
            elif music.main(say):
                skillUse = True
                
            elif open.main(say):
                skillUse = True
                
            elif screenshot.main(say):
                skillUse = True
                
            elif search.main(say):
                skillUse = True
                
            elif poweroff.main(say):
                skillUse = True
                
            elif ytvideo.main(say):
                skillUse = True
                
            elif resay.main(say):
                skillUse = True
            
            elif coin.main(say):
                skillUse = True
                
            elif map.main(say):
                skillUse = True
                
            elif wiki.main(say):
                skillUse = True
                
            elif location.main(say):
                skillUse = True
            
            elif weather_no_city.main(say):
                skillUse = True
            
            elif translate.main(say):
                skillUse = True
                
            elif news.main(say):
                skillUse = True
                
            elif upd_upg.main(say):
                skillUse = True
                
            elif todolist.main(say):
                skillUse = True
                
            elif shoplist.main(say):
                skillUse = True
                
            elif netconnection.main(say):
                skillUse = True
                
            elif record.main(say):
                skillUse = True
                
            elif guess_num.isTriggered(say):
                skillUse = True
                global randnum, isGuessNum
                randnum = guess_num.getRandomNum()
                isGuessNum = guess_num.startGame(self.listWidget)
            
            elif rulette.isTriggered(say):
                skillUse = True
                global isRuLette
                isRuLette = rulette.startGame()
                
            elif math.calculate(say):
                skillUse = True
                
            elif audio.main(say):
                skillUse = True
                
            elif crystal_ball.main(say):
                skillUse = True

            elif random_num.main(say):
                skillUse = True

            elif timer.main(say):
                skillUse = True
            
            elif say == 'stop' or say == 'Stop' or say == 'Стоп' or say == 'стоп':
                speak.tts_d.stop()
                
            elif isGuessNum:
                isGuessNum = guess_num.game(say, randnum, isGuessNum)
            
            elif isRuLette:
                isRuLette = rulette.game(say)
                
            else:
                if talk.talk(say) != "" and not skillUse:
                    speak.speak(talk.talk(say))
                elif not skillUse:
                    if say != "":
                        # Фразы для ответа на несуществующие команды
                        randwrong = random.choice(wrong)
                        speak.speak(randwrong)
                    

if __name__ == "__main__":
    Main()
