from datetime import timedelta
import webbrowser, os

def parseuptime(uptime):
    seconds = int(uptime) / 100
    return str(timedelta(seconds=seconds))


def checkemptystrings(*args):
    for string in args:
        if string == "":
            return True
    return False


def openhelp():
    webbrowser.open('file://' + os.path.realpath('SNMPToolHelp.html'))
