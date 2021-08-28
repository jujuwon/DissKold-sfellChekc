import discord
import os
from dotenv import load_dotenv
from spellcheck import regExp

class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        game = discord.Game("마춤뻡 검사")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)
        regExp.init()

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None
        
        '''
        # message.content = message의 내용
        if message.content == "안녕":
            # 현재 채널을 받아옴
            channel = message.channel
            # 발신자 태그 + 답변 내용 구성
            msg = "<@{}> ".format(message.author.id) + "안녕~~"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        '''

        flag = False
        
        msg, flag = regExp.check(message.content)
        if flag:
            channel = message.channel
            msg = "<@{}> ".format(message.author.id) + '"' + msg + '"(이)가 정확한 표현입니다'
            await channel.send(msg)
            return None


# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # 토큰 불러오기
    load_dotenv()
    token = os.getenv("TOKEN")
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run(token)
