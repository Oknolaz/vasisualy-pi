import geocoder
from ..core import speak

trigger = ("Где я", "где я", "Моё местоположение", "моё местоположение", "Что за место", "что за место")

def main(say):
    for i in trigger:
        if i in say:
            geo = geocoder.ip('me')
            toSpeak = f"Ты находишься в {geo.country}, {geo.city}."
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak)
    return toSpeak
