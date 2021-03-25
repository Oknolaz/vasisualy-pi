from ..core import speak
import random
import vlc

inst = vlc.Instance()
player=inst.media_player_new()

trigger = ("Русская рулетка", "русская рулетка", "В русскую рулетку", "в русскую рулетку")

def isTriggered(say):
    for i in trigger:
        if i in say:
            triggered = True
            break
        else:
            triggered = False
    
    return triggered

def startGame():
    bullet = random.choice([0, 0, 0, 0, 0, 1])
    isRuLette = True
    speak.speak("Я первый стреляю, если хочешь выстрелить - скажи \"выстрел\".")
    if bullet == 1:
        media = inst.media_new("vasisualy_pi/assets/shot.wav")
        player.set_media(media)
        player.play()
        speak.speak("Ты выиграл.")
        isRuLette = False
    else:
        media = inst.media_new("vasisualy_pi/assets/misfire.wav")
        player.set_media(media)
        player.play()
        speak.speak("Выстрела нет. Твоя очередь.")
    return isRuLette
    
def game(say):
    gameState = True
    if say == "Выстрел" or say == "выстрел":
        bullet = random.choice([0, 0, 0, 0, 0, 1])
        if bullet == 1:
            speak.speak("Ты проиграл.")
            media = inst.media_new("vasisualy_pi/assets/shot.wav")
            player.set_media(media)
            player.play()
            gameState = False
        else:
            media = inst.media_new("vasisualy_pi/assets/misfire.wav")
            player.set_media(media)
            player.play()
            speak.speak("Кручу барабан...")
            bullet = random.choice([0, 0, 0, 0, 0, 1])
            if bullet == 1:
                speak.speak("Ты выиграл.")
                media = inst.media_new("vasisualy_pi/assets/shot.wav")
                player.set_media(media)
                player.play()
                gameState = False
            else:
                media = inst.media_new("vasisualy_pi/assets/misfire.wav")
                player.set_media(media)
                player.play()
                speak.speak("Теперь ты.")
    return gameState
