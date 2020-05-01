def wizard():
    userInput = input()


def checkYesNo(string):
    string = string.lower()
    if string == 'y' or string == 'yes': return True
    elif string == 'n' or string == 'no': return False
    else: return
