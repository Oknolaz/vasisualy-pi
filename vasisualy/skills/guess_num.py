import random
from ..core import speak

trigger = ("Угадай число", "угадай число", "Поиграем в число", "поиграем в число", "Играть в угадай число",
           "играть в угадай число", "Играть в число", "играть в число", "Угадать число", "угадать число",
           "Угадывать число", "угадывать число")

def isTriggered(say):
    for i in trigger:
        if i in say:
            triggered = True
            break
        else:
            triggered = False
    
    return triggered

def getRandomNum():
    randnum = random.randint(0, 100)
    return randnum

def startGame():
    speak.speak("Я загадал число от 0 до 100. Угадай его.")
    isGuessNum = True
    return isGuessNum

def game(say, num, gameState):
    usrnum = -1
    gameState = True
    guessTry = 0
    try:
        usrnum = int(say)
    except Exception:
        pass
    if usrnum == -1:
        pass
    elif usrnum < num:
        speak.speak("Моё число больше.")
        guessTry += 1
    elif usrnum > num:
        speak.speak("Моё число меньше.")
        guessTry += 1
    elif usrnum == num:
        speak.speak(f"Поздравляю, ты выиграл затратив на это {str(guessTry+1)} попытки.")
        gameState = False
        guessTry = 0
    return gameState
