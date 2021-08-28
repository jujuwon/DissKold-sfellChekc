import re
import csv
import os

# 2단계 SEARCH 유형
regs = [
    '(?<=[^(지)]\s)않|^않',
    '돼(?=[어었다는])', '됀', '됌', '됄', '됍', '됬',
    '되(?=[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]$)|되$|되(?=[요여유])|되(?=[서도]\s[^않])|되(?=\s*[있야가버줘먹보])',
    '어떻게(?=[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]*$)',
    '어떡해(?=[\s]*[ㄱ-ㅎ|ㅏ-ㅣ|가-힣|]+)',
    '(?<=뭐)던',
    '안절부절(?!\s*못)',
    '뵈(?=요?[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]*$)',
    '봬(?=[가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9])(?=[^요])',
    '(?<=\d)연도|(?<=몇\s)연도', '(?<!\d)(?<!몇\s)년도'
]
corrects = [
    '안', '되', '된', '됨', '될', '됩', '됐', '돼',
    '어떡해', '어떻게', '든', '안절부절못', '봬', '뵈', '년도', '연도'
]
patterns = []
legnth = len(corrects)

# 2단계 ONE TIME 유형
oneTimeReg = '(?<!뭐)든'

# 2단계 종성 유형
jsRegs = [
    '껄', '께'
]
jsPatterns = []


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

    global oneTimePattern
    oneTimePattern = re.compile(oneTimeReg)

    for reg in jsRegs:
        jsPatterns.append(re.compile(reg))


# 종성 체크 함수
def chk_jongseong(word):
    flag = 0
    if '가'<=word<='힣':
        ch1 = (ord(word) - ord('가'))//588
        ch2 = ((ord(word) - ord('가')) - (588*ch1)) // 28
        ch3 = (ord(word) - ord('가')) - (588*ch1) - 28*ch2
        if ch3 == 8: # ㄹ
            flag += 1
        elif ch3 == 4: # ㄴ
            flag += 2
        elif ch3 == 0: # 종성 없음
            flag += 3
    
    return flag


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

    # 2단계 SEARCH 유형 체크
    searchPatternFlag = False
    length = len(patterns)
    for i in range(length):
        if re.search(patterns[i], msg):
            msg = re.sub(patterns[i], corrects[i], msg)
            searchPatternFlag = True

    # 2단계 ONE TIME 유형 체크
    oneTimePatternFlag = False
    if len(oneTimePattern.findall(msg)) == 1:
        msg = re.sub(oneTimePattern, '던', msg)
        oneTimePatternFlag = True

    # 2단계 종성 유형 체크

    

    flag = csvFlag or searchPatternFlag or oneTimePatternFlag

    return msg, flag