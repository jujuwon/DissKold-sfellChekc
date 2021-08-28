import re
import csv
import os

'''
if re.findall(r"되(?=[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9])$|되$", msg):
    msg = re.sub('되(?=[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]$)|되$',"돼",msg)
    flag = True
'''

patterns = [
    "되(?=[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]$)|되$"
]
regs = []

def init():
    # 1단계 init
    # 파일 경로 설정
    absPath = os.path.abspath(__file__)
    fileDir = os.path.dirname(absPath)
    parentDir = os.path.dirname(fileDir)
    parentDir = os.path.dirname(parentDir)

    dataPath = os.path.join(parentDir, 'Data')
    global fileName
    fileName = dataPath + '\data1.csv'

    for pattern in patterns:
        regs.append(re.compile(patterns))
    


def check(msg):
    
    flag = False

    # 1단계 csv 파일 패턴 체크
    matchFlag = False
    # 파일 읽기
    with open(fileName, 'r', encoding='utf-8') as f:
        data = csv.reader(f)       
        for line in data:
            if re.findall(line[0], msg):
                msg = msg.replace(line[0], line[1])
                matchFlag = True


    # 2단계 유형 체크



    return msg, flag