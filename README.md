# Homework 6

### Домашнее задания №6 студента курса Hillel Python Advanced Ксендзюка Глеба

***

## Описание

####Сайт представляет собой 3 вкладки, которые между которыми можно переключаться в меню сверху:
####Вкладка About COVID-19. Выводит информацию о вирусе
####Вкладка Statics. Выводит статистику по странам
####Вкладка Contact us. На вкладке можно заполнить таблицу, описать вашу проблему, отправить на сервер

## Руководство по применению

## Установка GIT

### Установка в Linux

Если вы хотите установить Git под Linux как бинарный пакет, это можно сделать, используя обычный менеджер пакетов вашего
дистрибутива. Если у вас Fedora (или другой похожий дистрибутив, такой как RHEL или CentOS), можно воспользоваться dnf:

```bash
$ sudo dnf install git-all
```

Если же у вас дистрибутив, основанный на Debian, например, Ubuntu, попробуйте apt:

```bash
$ sudo apt install git
```

Чтобы воспользоваться дополнительными возможностями, посмотрите инструкцию по установке для нескольких различных
разновидностей Unix на сайте Git http://git-scm.com/download/linux.

### Установка на Mac

Существует несколько способов установки Git на Mac. Самый простой — установить Xcode Command Line Tools. В версии
Mavericks (10.9) и выше вы можете добиться этого просто первый раз выполнив git в терминале.

```bash
$ git --version
```

Если Git не установлен, вам будет предложено его установить.
![OS X инсталлятор Git](https://git-scm.com/book/en/v2/images/git-osx-installer.png)
***

## Установка в Windows

Для установки Git в Windows также имеется несколько способов. Официальная сборка доступна для скачивания на официальном
сайте Git. Просто перейдите на страницу http://git-scm.com/download/win, и загрузка запустится автоматически. Обратите
внимание, что это отдельный проект, называемый Git для Windows; для получения дополнительной информации о нём перейдите
на https://gitforwindows.org.

Для автоматической установки вы можете использовать пакет Git Chocolatey. Обратите внимание, что пакет Chocolatey
поддерживается сообществом.

Другой простой способ установки Git — установить GitHub для Windows. Его установщик включает в себя утилиты командной
строки и GUI Git. Он также корректно работает с Powershell, обеспечивает надёжное сохранение учётных данных и правильные
настройки CRLF. Вы познакомитесь с этими вещами подробнее несколько позже, здесь же отметим, что они будут вам
необходимы. Вы можете загрузить GitHub для Windows с вебсайта GitHub Desktop.
***

## Клонирование репозитория

Операция **clone** создаёт экземпляр удалённого репозитория.

```
git clone https://gitlab.com/ari10000krat/homework2
```

В результате выполнения данной команды мы создадим копию удалённого репозитория в нужной нам директории.
***

## Установка виртуального окружения

Установка утилиты управляющей виртуальными окружениями в Python:

```
sudo apt install python3-venv
```

Создаем или переходи в уже имеющуюся директорию проекта

Создание виртуального окружения

```
python3 -m venv env_name
```

Активация виртуального окружения

```
source env_name/bin/activate
```

Проверяем перечень пакетов Python установленных в системе

```
pip3 list
```

Определяем откуда именно запускается интерпретатор Python и утилита pip

```
which python3
which pip3
```

Для выхода из виртуального окружения нужно выполнить команду:

```
deactivate
```

***

## Установка необходимых библиотек

Чтобы установить весь перечень библиотек из файла requirements.txt в текущее окружение, то нужно выполнить следующую
команду:

```
pip install -r requirements.txt
```

***

# Запуск программы

### Для того, чтобы запустить сервер необходимо запустить файл app.py После этого в командной строке коректно вводить запросы