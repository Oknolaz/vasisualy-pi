from ..core import speak
import alsaaudio

increase = ("Сделай громче", "сделай громче", "Сделай звук громче", "сделай звук громче", "Увеличить звук",
            "увеличить звук", "Увеличь звук", "увеличь звук", "Повысь звук", "повысь звук", "Повысить звук",
            "повысить звук", "Увеличить громкость", "увеличить громкость", "Увеличь громкость", "увеличь громкость",
            "Повысь громкость", "повысь громкость", "Повысить громкость", "повысить громкость")
decrease = ("Сделай тише", "сделай тише", "Сделай звук тише", "сделай звук тише", "Уменьшить звук", "уменьшить звук",
            "Уменьши звук", "уменьши звук", "Понизить звук", "понизить звук", "Уменьшить громкость",
            "уменьшить громкость", "Уменьши громкость", "уменьши громкость", "Понизить громкость", "понизить громкость",
            "Понизь громкость", "понизь громкость")
off = ("Выключи звук", "выключи звук", "Отключи звук", "отключи звук", "Выключить звук", "выключить звук")
on = ("Включи звук", "включи звук", "Включить звук", "включить звук")

def main(say):
    mixer = alsaaudio.Mixer()
    volume = int(mixer.getvolume()[0])
    
    for i in increase:
        if i in say:
            if volume <= 95:
                mixer.setvolume(volume + 5)
                toSpeak = "Громкость увеличена."
            elif volume > 95 and volume < 100:
                mixer.setvolume(100)
                toSpeak = "Громкость увеличена."
            else:
                toSpeak = "Громкость максимальная."
            break
        else:
            toSpeak = ""
            
    for i in decrease:
        if i in say:
            if volume <= 5 and volume != 0:
                mixer.setvolume(0)
                toSpeak = "Звук выключен."
            elif volume == 0:
                toSpeak = "Звук уже выключен!"
            else:
                mixer.setvolume(volume - 5)
                toSpeak = "Громкость уменьшена."
            break
        
    for i in off:
        if i in say:
            mixer.setvolume(0)
            toSpeak = "Звук выключен."
            break
    
    for i in on:
        if i in say:
            mixer.setvolume(20)
            toSpeak = "Звук включен с уровнем громкости 20 процентов."
            break
            
    if toSpeak != "":
        speak.speak(toSpeak)
    return toSpeak
