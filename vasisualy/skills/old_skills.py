from ..core import speak
import sys


def old_skills_activate(user_message):
    '''Активирует "старые" навыки.
    :param: user_message: сообщение пользователя (string)
    :param: widget: виджет, в который должно выводиться сообщение навыка (QWidget)
    '''
    skills = ("time_date", "exit", "weather", "music", "open", "screenshot", "search", "poweroff",
              "ytvideo", "resay", "map", "wiki", "location", "weather_no_city", "translate", "news", "coin",
              "upd_upg", "shoplist", "todolist", "netconnection", "record", "math", "audio", "crystal_ball",
              "random_num", "timer")
    skillUse = False
    skill_loc = "vasisualy.skills."

    for skill in skills:
        skill = skill_loc + skill
        if skill == skill_loc + "time_date":
            if sys.modules[skill].main(user_message):
                speak.speak(sys.modules[skill].main(user_message))
                skillUse = True
                break

        if skill == skill_loc + "exit":
            if sys.modules[skill].main(user_message):
                skillUse = True
                break

        if skill == skill_loc + "math":
            if sys.modules[skill].calculate(user_message):
                skillUse = True
                break

        if ((not skillUse) and (skill != skill_loc + "time_date")
                and (skill != skill_loc + "exit") and (skill != skill_loc + "math")):
            if sys.modules[skill].main(user_message):
                skillUse = True
                break

    return skillUse