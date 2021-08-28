from spellcheck import firstStepReg

def check(msg):

    flag = False
    msg, fStepCount = firstStepReg.checkWord(msg)

    if fStepCount > 0 :
        flag = True

    return msg, flag