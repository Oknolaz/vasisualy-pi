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

wrong = ("Простите, я вас не понимаю.", "Мне кажется вы несёте какой-то бред.", "Что?", "Вы, наверное, ошиблись. Я вас не понимаю.", "Извините, я появился совсем недавно, я пока понимаю очень мало слов.", "Чего?", "А? Что? Я Вас не понимаю.", "Пожалуйста, не говорите слов, которых я незнаю.", "Вы пытаетесь оскорбить меня этим?", "Не издевайтесь надо мной, я знаю не так много слов.", "Извините, я не могу Вас понять.", "А?", "Объясните попроще.", "Пожалуйста, прочитайте моё описание. Скорее всего я не умею делать то, что вы меня просите или попробуйте использовать синонимы.", "Вы ошиблись.", "Я не понимаю твоего вопроса.", "Мне не понятен твой вопрос.", "Не могу понять о чём ты говоришь.", "Я не понимаю.", "О чём ты?", "Я не могу распознать вопрос.") # Ответы на неизвестную команду.
guessnum = ("Угадай число", "угадай число", "Поиграем в число", "поиграем в число", "Играть в угадай число", "играть в угадай число", "Играть в число", "играть в число", "Угадать число", "угадать число", "Угадывать число", "угадывать число")
russian_roulette = ("Русская рулетка", "русская рулетка", "В русскую рулетку", "в русскую рулетку")
code_words = ("Васисуалий", "васисуалий", "Васися", "васися", "Василий", "василий", "Васямба", "васямба", "Вася", "вася", "Васёк", "васёк", "Васис", "васис")

# Настройки распознавания речи
recognizer = speech_recognition.Recognizer()
recognizer.pause_threshold = 0.5
mph = speech_recognition.Microphone()


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
        
            for i in guessnum:
                if i in say:
                    global randnum
                    randnum = random.randint(0, 100)
                    speak.speak("Я загадал число от 0 до 100. Угадай его.")
                    self.isGuessNum = True
                    skillUse = True
                    guessTry = 0
                    break
                
            for i in russian_roulette:
                if i in say:
                    global isRoulette
                    skillUse = True
                    bullet = random.choice([0, 0, 0, 0, 0, 1])
                    speak.speak("Я первый стреляю, если хочешь выстрелить - скажи \"выстрел\".")
                    self.isRoulette = True
                    if bullet == 1:
                        media=music.inst.media_new("assets/shot.wav")
                        music.player.set_media(media)
                        music.player.play()
                        speak.speak("Ты выиграл.", self.listWidget)
                        isRoulette = False
                    else:
                        media=music.inst.media_new("assets/misfire.wav")
                        music.player.set_media(media)
                        music.player.play()
                        speak.speak("Выстрела нет. Твоя очередь.")
                
            if time_date.main(say) != "":
                speak.speak(time_date.main(say))
                skillUse = True
                
            elif exit.main(say) != "":
                skillUse = True
                
            elif joke.main(say) != "":
                speak.speak(joke.main(say))
                skillUse = True
                
            elif weather.main(say) != "":
                skillUse = True
                
            elif music.main(say) != "":
                skillUse = True
                
            elif open.main(say) != "":
                skillUse = True
                
            elif screenshot.main(say) != "":
                skillUse = True
                
            elif search.main(say) != "":
                skillUse = True
                
            elif poweroff.main(say) != "":
                skillUse = True
                
            elif ytvideo.main(say) != "":
                skillUse = True
                
            elif resay.main(say) != "":
                skillUse = True
            
            elif coin.main(say) != "":
                skillUse = True
                
            elif map.main(say) != "":
                skillUse = True
                
            elif wiki.main(say) != "":
                skillUse = True
                
            elif location.main(say) != "":
                skillUse = True
            
            elif weather_no_city.main(say) != "":
                skillUse = True
            
            elif translate.main(say) != "":
                skillUse = True
                
            elif news.main(say) != "":
                skillUse = True
                
            elif upd_upg.main(say) != "":
                skillUse = True
                
            elif todolist.main(say) != "":
                skillUse = True
                
            elif shoplist.main(say) != "":
                skillUse = True
                
            elif netconnection.main(say) != "":
                skillUse = True
            
            elif say == 'stop' or say == 'Stop' or say == 'Стоп' or say == 'стоп':
                speak.tts_d.stop()
                    
            elif self.isGuessNum:
                usrnum = -1
                try:
                    usrnum = int(say)
                except Exception:
                    pass
                if usrnum == -1:
                    pass
                elif usrnum < randnum:
                    speak.speak("Моё число больше.")
                    self.guessTry += 1
                elif usrnum > randnum:
                    speak.speak("Моё число меньше.")
                    self.guessTry += 1
                elif usrnum == randnum:
                    speak.speak(f"Поздравляю, ты выиграл затратив на это {str(self.guessTry+1)} попытки.")
                    isGuessNum = False
                    self.guessTry = 0
                    
            elif self.isRoulette:
                if say == "Выстрел":
                    bullet = random.choice([0, 0, 0, 0, 0, 1])
                    if bullet == 1:
                        speak.speak("Ты проиграл.")
                        media = music.inst.media_new("assets/shot.wav")
                        music.player.set_media(media)
                        music.player.play()
                        self.isRoulette = False
                    else:
                        media = music.inst.media_new("assets/misfire.wav")
                        music.player.set_media(media)
                        music.player.play()
                        speak.speak("Кручу барабан...")
                        bullet = random.choice([0, 0, 0, 0, 0, 1])
                        if bullet == 1:
                            speak.speak("Ты выиграл.")
                            media = music.inst.media_new("assets/shot.wav")
                            music.player.set_media(media)
                            music.player.play()
                            self.isRoulette = False
                        else:
                            media = music.inst.media_new("assets/misfire.wav")
                            music.player.set_media(media)
                            music.player.play()
                            speak.speak("Теперь ты.")
                
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
