import speechd
from . import defaults
import os

tts_d = speechd.SSIPClient('Vasisya')
tts_d.set_output_module('rhvoice')
tts_d.set_language('ru')
try:
    appDir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(f"{appDir}/../../")
    config = open("vasisualy.conf", "r")
    for line in config:
        if "voice:" in line:
            voice = line.replace("voice:", "")
        elif "speed:" in line:
            speed = int(line.replace("speed:", ""))
        elif "pitch:" in line:
            pitch = int(line.replace("pitch:", ""))
except Exception:
    voice = defaults.defaults["voice"]
    speed = defaults.defaults["speed"]
    pitch = defaults.defaults["pitch"]
tts_d.set_synthesis_voice(voice)
tts_d.set_rate(speed)
tts_d.set_punctuation(speechd.PunctuationMode.NONE)
tts_d.set_pitch(pitch)

def speak(string):
    tts_d.speak(string)
    print(string)
