#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Core
from .core import (speak, talk, defaults)
import vasisualy.utils as utils
import random
import speech_recognition
import os

# Skills
from .skills import (skill_loader, time_date, exit, weather, music, open, screenshot, search, poweroff, ytvideo,
                     resay, map, wiki, location, weather_no_city, translate, news, coin, upd_upg, shoplist, todolist,
                     netconnection, record, guess_num, rulette, math, audio, crystal_ball, random_num, timer,
                     old_skills)

# Ответы на неизвестную команду.
wrong = ("Прости, я тебя не понимаю.", "Мне кажется ты несёшь какой-то бред.", "Что?",
         "Ты, наверное, ошибаешься. Я тебя не понимаю.",
         "Извини, я появился совсем недавно, я пока понимаю очень мало слов.",
         "Чего?", "А? Что? Я тебя не понимаю.", "Пожалуйста, не говори слов, которых я незнаю.",
         "Ты пытаешься оскорбить меня этим?", "Не издевайся надо мной, я знаю не так много слов.",
         "Извини, я не могу тебя понять.", "А?", "Объясни попроще.",
         "Пожалуйста, прочитай моё описание. Скорее всего я не умею делать то, что ты меня просишь или попробуй использовать синонимы.",
         "Ты ошибаешься.", "Я не понимаю твоего вопроса.", "Мне не понятен твой вопрос.",
         "Не могу понять о чём ты говоришь.", "Я не понимаю.", "О чём ты?", "Я не могу распознать вопрос.")
code_words = ("Васисуалий", "васисуалий", "Васися", "васися", "Василий", "василий", "Васямба", "васямба", "Вася",
              "вася", "Васёк", "васёк", "Васис", "васис")

# Настройки распознавания речи
recognizer = speech_recognition.Recognizer()
recognizer.pause_threshold = 1
mph = speech_recognition.Microphone()

randnum = -1
isGuessNum = False
isRuLette = False


class Main:
    def __init__(self):
        speak.speak("Привет, меня зовут Васисуалий. Чем могу быть полезен?")
        self.guessTry = 0
        self.isGuessNum = False
        randnum = 0
        self.isRoulette = False
        skill_loader.load()  # Импорт новых навыков
        self.program()

    def recognise(self):
        print("[sys] Говорите...")
        with mph as source:
            say = recognizer.listen(source)
        print("[sys] Речь распознаётся...")
        hot_word_is_detected = False
        try:
            say = recognizer.recognize_google(say, language="ru-RU")
            say = str(say)
            for code_word in code_words:
                if code_word in say:
                    say = say.replace(code_word + ' ', '', 1)
                    say = say.capitalize()
                    hot_word_is_detected = True
                    break
        except Exception:
            say = ''
            print("[sys] Не удалось распознать речь. Нет подключения к интернету или не подключен микрофон.")

        if hot_word_is_detected:
            print(f"Вы: {say}")
        else:
            say = ''
        return say

    def program(self):
        skillUse = False

        print("[sys] ТИХО!..")

        with mph as source:
            recognizer.adjust_for_ambient_noise(source)

        while True:
            tmp = utils.tmp

            say = self.recognise()
            skillUse = False

            if os.path.exists(f"{tmp}/.skill_lock"):
                # Если файл блокировки существует - сообщение пользователя
                # передаётся запущенному циклу навыка.
                skill_loader.run_looped(say, self.listWidget)
                skillUse = True

            elif skill_loader.run_skills(say):
                skillUse = True

            elif old_skills.old_skills_activate(say):
                skillUse = True
                
            elif guess_num.isTriggered(say):
                skillUse = True
                global randnum, isGuessNum
                randnum = guess_num.getRandomNum()
                isGuessNum = guess_num.startGame()
            
            elif rulette.isTriggered(say):
                skillUse = True
                global isRuLette
                isRuLette = rulette.startGame()
            
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
