import re
import csv
import os

# 2단계 SEARCH 유형
regs = [
    '(?<=[^(지)]\s)않|^않', '돼(?=[어었다는])', '됀', '됌', '됄', '됍', '됬',
    '되(?=[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]$)|되$|되(?=[요여유])|되(?=[서도]\s[^않])|되(?=\s*[있야가버줘먹보])',
    '어떡해(?=[\s]*[가-힣ㄱ-ㅎa-zA-Z0-9])', '어떻게(?=[[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]*[ㅏ-ㅣ\s]*$)|어떻게$',
    '(?<=뭐)던', '안절부절(?!\s*못)',
    '뵈(?=요?[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]*$)', '봬(?=[가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9])(?=[^요])',
    '(?<=\d)연도|(?<=몇\s)연도', '(?<!\d)(?<!몇\s)년도',
    '불리우', '불리운', '(?<![이가])(\s)피(?![우워웠운])'
]
corrects = [
    '안', '되', '된', '됨', '될', '됩', '됐', '돼',
    '어떻게', '어떡해', '든', '안절부절못', '봬', '뵈', '년도', '연도',
    '불리', '불린', ' 피우'
]
patterns = []
legnth = len(corrects)

# 2단계 종성 유형
jsRegs = [
    '(?<=[ㄱ-ㅎ|ㅏ-ㅣ|가-힣])[률]', '(?<=[ㄱ-ㅎ|ㅏ-ㅣ|가-힣])[율]', '(?<!껄)껄(?!껄)', '께'
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
    fileName = dataPath + '\data.csv'

    for reg in regs:
        patterns.append(re.compile(reg))

    for reg in jsRegs:
        jsPatterns.append(re.compile(reg))


# 종성 체크 함수
def chk_jongseong(word):
    flag = 0
    if '가'<=word<='힣':
        ch1 = (ord(word) - ord('가'))//588
        ch2 = ((ord(word) - ord('가')) - (588*ch1)) // 28
        ch3 = (ord(word) - ord('가')) - (588*ch1) - 28*ch2
        if ch3 == 8: # ㄹ 종성
            flag += 1
        elif ch3 == 4: # ㄴ 종성
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


    # 2단계 종성 유형 체크 - 률
    jsPatternsFlag = False
    res1 = jsPatterns[0].search(msg)
    resIter1 = jsPatterns[0].finditer(msg)
    lst = []
    _msg = list(msg)

    if res1:
        for r in resIter1:
            if r.start() != 0:
                lst.append(r.start())

        for i in lst:
            wd = msg[i-1]
            if (chk_jongseong(wd) == 2) or (chk_jongseong(wd) == 3):
                _msg[i] = '율'
                jsPatternsFlag = True

        msg = ''.join(_msg)
        
    # 2단계 종성 유형 체크 - 율
    res2 = jsPatterns[1].search(msg)
    resIter2 = jsPatterns[1].finditer(msg)
    lst = []
    _msg = list(msg)

    if res2:
        for r in resIter2:
            if r.start() != 0:
                lst.append(r.start())

        for i in lst:
            wd = msg[i-1]
            if (chk_jongseong(wd) != 2) and (chk_jongseong(wd) != 3):
                _msg[i] = '률'
                jsPatternsFlag = True

        msg = ''.join(_msg)

    # 2단계 종성 유형 체크 - -ㄹ껄
    res3 = jsPatterns[2].search(msg)
    resIter3 = jsPatterns[2].finditer(msg)
    lst = []

    if res3: 
        for r in resIter3:
            if r.start() != 0:
                lst.append(r.start())
    
        for i in lst:
            wd = msg[i-1]
            if chk_jongseong(wd) == 1 :
                jsPatternsFlag = True
                msg = list(msg)
                msg[i] = '걸'
        
        msg = ''.join(msg)

    # 2단계 종성 유형 체크 - -ㄹ께
    res4= jsPatterns[3].search(msg)
    resIter4 = jsPatterns[3].finditer(msg)

    lst = []

    if res4: 
        for r in resIter4:
            if r.start() != 0:
                lst.append(r.start())
    
        for i in lst:
            wd = msg[i-1]
            if chk_jongseong(wd) == 1 :
                jsPatternsFlag = True
                msg = list(msg)
                msg[i] = '게'
        
        msg = ''.join(msg)


    flag = csvFlag or searchPatternFlag or jsPatternsFlag

    return msg, flag