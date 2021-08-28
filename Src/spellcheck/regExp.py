import re
import csv
import os

regs = [
    '(?<=[^(지)]\s)않',
    '되(?=[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]$)|되$',
    '어떻게(?=[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]*$)',
    '어떡해(?=[\s]*[ㄱ-ㅎ|ㅏ-ㅣ|가-힣|]+)'
]

corrects = [
    '안',
    '돼',
    '어떡해',
    '어떻게'
]

patterns = []

legnth = len(corrects)

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

    for reg in regs:
        patterns.append(re.compile(reg))


def check(msg):
    
    flag = False

    # 1단계 csv 파일 패턴 체크
    csvFlag = False
    # 파일 읽기
    with open(fileName, 'r', encoding='utf-8') as f:
        data = csv.reader(f)       
        for line in data:
            if re.findall(line[0], msg):
                msg = msg.replace(line[0], line[1])
                csvFlag = True


    # 2단계 유형 체크
    patternFlag = False
    length = len(patterns)
    for i in range(length):
        if re.search(patterns[i], msg):
            msg = re.sub(patterns[i], corrects[i], msg)
            patternFlag = True

    flag = csvFlag or patternFlag

    return msg, flag