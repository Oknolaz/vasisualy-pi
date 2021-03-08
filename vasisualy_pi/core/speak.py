import speechd

tts_d = speechd.SSIPClient('Vasisya')
tts_d.set_output_module('rhvoice')
tts_d.set_language('ru')
tts_d.set_synthesis_voice('Artemiy')
tts_d.set_rate(30)
tts_d.set_punctuation(speechd.PunctuationMode.NONE)
tts_d.set_pitch(0)

def speak(string):
    tts_d.speak(string)
    print(string)
