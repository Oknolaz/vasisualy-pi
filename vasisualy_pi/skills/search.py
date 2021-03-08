import webbrowser
from ..core import speak

trigger = ("Почему", "почему", "Зачем", "зачем", "Какой", "какой", "Какая", "какая", "Какое", "какое", "Когда", "когда", "Куда", "куда", "Откуда", "откуда", "В интернете", "в интернете", "Поиск в сети", "поиск в сети", "Ищи в сети", "ищи в сети", "Что делать если", "что делать если") # Команды для поиска в сети
excludeList = ("Васисуалий", "Васисуали", "васисуалий", "васисуали", "Васян", "васян", "Васёк", "васёк", "Васися", "васися", "Васисяндра", "васисяндра", "Васька", "васька", "Вася", "вася", "Василий", "василий", "Пожалуйста", "пожалуйста")

def main(say):
    for i in trigger:
        if i in say:
            for toExclude in excludeList:
                say = say.replace(toExclude, '')
            toSpeak = "Сейчас найду."
            try:
                webbrowser.open_new_tab(f"https://duckduckgo.com/{say}") # Поиск данного запроса в интернетах
            except Exception:
                toSpeak = "Не удалось открыть браузер."
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak)
    
    return toSpeak
