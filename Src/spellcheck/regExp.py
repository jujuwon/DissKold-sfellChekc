from spellcheck import matchWord

def init():
    matchWord.init()

def check(msg):

    flag = False
    msg, matchCount = matchWord.checkWord(msg)

    if matchCount > 0 :
        flag = True

    return msg, flag