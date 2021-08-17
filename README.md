# Голосовой ассистент Васисуалий :+1:
Васисуалий - это простой голосовой помощник, уважающий вашу свободу. Поддерживается только русский язык.
**Данный репозиторий содержит CLI версию программы, основной репозиторий находится [здесь](https://github.com/Oknolaz/vasisualy-pi).**
## Поддерживаемые платформы
- **GNU/Linux (Qt5 и CLI)**
- **Microsoft Windows**
- **Android**
## Васисуалий может:
- Сказать текущую дату и время.
- Рассказать анекдот.
- Сказать о текущей погоде в любом городе мира.
- Включить радио.
- Открыть браузер или веб-сайт (например, YouTube).
- Запустить программу, установленную на вашем ПК.
- Сделать снимок экрана.
- Искать информацию в Итернете.
- Выключить или перезагрузить компьютер.
- Искать видео на YouTube.
- Повторять ваши слова, как попугай.
- Подкинуть монетку.
- Сказать скороговорку.
- Открыть карты (OpenStreetMap)
- Искать ответ на ваш вопрос в [Википедии](https://wikipedia.org).
- Сказать где вы.
- Перевести текст с любого языка на русский, испанский, английский, французский, итальянский и др..
- Рассказать новости с [Wikinews](https://wikinews.org/).
- Сыграть в Угадай число и Русскую рулетку с вами.
- Примитивно общаться.
- [И многое другое...](https://github.com/Oknolaz/vasisualy/wiki/%D0%92%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D0%B8)

## Установка
### Debian GNU/Linux
Для начала Вам понадобится установить синтезатор речи [RHVoice](https://github.com/Olga-Yakovleva/RHVoice/):
```
sudo add-apt-repository ppa:linvinus/rhvoice
sudo apt-get update
sudo apt-get install speech-dispatcher-rhvoice rhvoice-russian
```
Затем нужно нужно установить модуль [speechd](https://freebsoft.org/speechd) для [Python](https://python.org/), [PyQt5](https://riverbankcomputing.com/software/pyqt/) и [VLC плеер](https://videolan.org/) с помощью менеджера пакетов в вашем дистрибутиве (например apt):
```
sudo apt-get install python3-speechd python3-pyqt5 vlc python3-pyqt5.qtwebengine python3-pyaudio python3-vlc
```
Клонируйте данный репозиторий с помощью Git:
```
git clone --recursive https://github.com/Oknolaz/vasisualy-pi
cd vasisualy-pi
```
Далее необходимо установить другие модули с помощью pip:
```
pip3 install -r requirements.txt
```
После этих действий можно запускать скрипт этой командой для Qt GUI версии:
```
python3 run.py
```

### Arch Linux
Для начала необходимо установить модули [RHVoice](https://aur.archlinux.org/packages/rhvoice) и [python-vlc](https://aur.archlinux.org/packages/python-vlc/) из [AUR](https://aur.archlinux.org/). Для установки с помощью [yay](https://aur.archlinux.org/packages/yay/) используйте:
```
yay -Sy rhvoice python-vlc
```
Установите необходимые пакеты с помощью [Pacman](https://wiki.archlinux.org/index.php/Pacman_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)):
```
pacman -Sy python-pyaudio python-pyqt5 python-pyalsa speech-dispatcher qt5-webengine vlc python-pyqt5-webengine
```
Клонируйте данный репозиторий:
```
git clone --recursive https://github.com/Oknolaz/vasisualy-pi
cd vasisualy-pi
```
Затем установите зависимости с помощью Pip:
```
pip3 install -r requirements.txt
```
После этих действий можно запускать скрипт этой командой для Qt GUI версии:
```
python3 run.py
```
**Также доступен [AUR репозиторий](https://aur.archlinux.org/packages/vasisualy-git/)**

## Помочь проекту
Если вы хотите помочь в разработке программы, вы можете открыть `Issue` и рассказать об ошибках, предложить свои идеи.
Также, при наличии необходимых умений, вы можете [создать собственный навык для голосового ассистента](https://github.com/Oknolaz/vasisualy/wiki/%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D0%BE%D0%B1%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BD%D0%B0%D0%B2%D1%8B%D0%BA%D0%B0) и добавить его в официальный репозиторий, используя [данную инструкцию](https://github.com/Oknolaz/vasisualy/wiki/%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D0%BE%D0%B1%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BD%D0%B0%D0%B2%D1%8B%D0%BA%D0%B0).

## Лицензия
Vasisualy - это свободное программное обеспечение: вы можете использовать и изменять его по условиям лицензии [GNU General Public License 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Поддержка
С вопросами и трудностями обращайтесь в нашу Telegram группу: [Vasisualy](https://t.me/vasisualy_voice_assistant)[<img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" height="40px"></img>](https://t.me/vasisualy_voice_assistant)
