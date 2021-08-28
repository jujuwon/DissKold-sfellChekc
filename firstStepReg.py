import re
import csv
import os

def checkReg(msg):
    currentPath = os.path.dirname(__file__)
    fileName = currentPath + '\data\data1.csv'

    flag = False
    # 파일 읽기
    with open(fileName, 'r', encoding='utf-8') as f:
        data = csv.reader(f)
        for line in data:
            if re.findall(line[0], msg):
                msg = msg.replace(line[0], line[1])
                flag = True

        '''
        if re.findall(r"되(?=[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9])$|되$", msg):
            msg = re.sub('되(?=[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]$)|되$',"돼",msg)
            flag = True
        '''

    return msg, flag
