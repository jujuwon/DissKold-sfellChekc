import re
import csv
import os

def init():
    absPath = os.path.abspath(__file__)
    fileDir = os.path.dirname(absPath)
    parentDir = os.path.dirname(fileDir)
    parentDir = os.path.dirname(parentDir)

    dataPath = os.path.join(parentDir, 'Data')
    global fileName
    fileName = dataPath + '\data1.csv'

def checkWord(msg):

    count = 0
    # 파일 읽기
    with open(fileName, 'r', encoding='utf-8') as f:
        data = csv.reader(f)
        
        for line in data:
            if re.findall(line[0], msg):
                msg = msg.replace(line[0], line[1])
                count += 1

        '''
        if re.findall(r"되(?=[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9])$|되$", msg):
            msg = re.sub('되(?=[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]$)|되$',"돼",msg)
            flag = True
        '''

    return msg, count
