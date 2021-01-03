import webbrowser
from datetime import timedelta


def parseuptime(uptime):
    seconds = int(uptime) / 100
    return str(timedelta(seconds=seconds))


def checkemptystrings(*args):
    for string in args:
        if string == "":
            return True
    return False


def openhelp():
    webbrowser.open('https://therealdanjo.github.io/SNMP_Tool/docs/SNMPToolHelp.html')
