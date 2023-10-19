# -*- coding: utf-8 -*-
import asyncio
import random
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"[!] 키킼..소녀와... 함께하시겠습니까...?")
    print(f"[!] 다음 : {bot.user.name}")
    print(f"[!] 다음 : {bot.user.id}")
    print(f"[!] 참가 중인 서버 : {len(bot.guilds)}개의 서버에 참여 중\n")  # 참여 중인 서버 수
    await bot.change_presence(activity=discord.Game(name="!명령어 "))


@bot.event
async def on_member_join(member):
    embed = discord.Embed(title='환영합니다, 저는 그냥 설녀입니다~\r\n제작자: 단덕래',
                          description='명령어 목록은 언제든지 !명령어 를 이용하여 확인하실 수 있습니다.',
                          colour=800000)
    embed.set_thumbnail(url='https://www.pojo.com/wp-content/uploads/2022/05/Tri-Brigade-Mercourier.jpg')
    embed.set_footer(text='다음에 또 봐요~')
    await member.send(embed=embed)
    channel = bot.get_channel()
    await channel.send("<@{}>님이 서버에 들어오셨어요. 환영합니다~".format(str(member.id)))


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel()
    await channel.send("<@{}>님이 나가셨습니다... 언젠가 다시 만날 수 있으려나요? 키킼".format(str(member.id)))
#겟 채널 오른쪽 괄호에 채널아이디 붙여넣기.

@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title='명령어를 사용하셨군요~',
                          description='궁금해하실 것 같은 항목들을 미리 준비해놓았습니다~',
                          colour=0x206694)
    embed.set_thumbnail(url='https://i.postimg.cc/QC7bmV5B/yuki-onna-the-ice-mayakashi-by-726312107-dd5fd22222-fullview.jpg')
    embed.add_field(name='!(카드이름)',value='해당카드의 발매명, 별명,\r\nㅤ▶빈칸/기호없이◀', inline=True)
    embed.add_field(name='!테마',value='해당테마의\r\n공식이름\r\n별칭', inline=True)
    embed.add_field(name='유틸리티',value='!주사위\r\n!홀짝\r\n!가위바위보\r\n!투표\r\n!요일투표\r\n!모집', inline=True)
    embed.add_field(name='이모지',value='!이모지 명령어로 확인가능', inline=True)
    embed.set_footer(text='명령어는 언제든지 명령어를 통해서 확인하실 수 있습니다~')
    embed.set_footer(text='도움이 되셨다면 다행이네요~ 이 창은 2분 뒤에 삭제됩니다~ 펑~')
    await ctx.channel.send(embed=embed, delete_after = 120)
    await ctx.message.delete()







#유틸리티






@bot.command()
async def 가위바위보(ctx):
    rsp = ['가위', '바위', '보']
    embed = discord.Embed(title="가위바위보", description="가위바위보를 합니다.. 20초내로 (가위 | 바위 | 보)를 써주세요~", color=0x0066cc)
    await ctx.message.delete()
    channel = ctx.channel
    msg1 = await ctx.channel.send(embed=embed)

    def check(m):
        return m.author == ctx.author and m.channel == channel

    try:
        msg2 = await bot.wait_for('message', timeout=20.0, check=check)
    except asyncio.TimeoutError:
        await msg1.delete()
        embed = discord.Embed(title="가위바위보", description="20초가 지났네요...", color=800000)
        await ctx.channel.send(embed=embed)
        return
    else:
        await msg1.delete()
        bot_rsp = str(random.choice(rsp))
        user_rsp = str(msg2.content)
        answer = ""
        if bot_rsp == user_rsp:
            answer = "저는 " + bot_rsp + "를 냈고, 당신은 " + user_rsp + "를 내셨내요.\n" + "어이쿠~ 아쉽지만 비겼습니다~"
            answer = answer.replace('가위', '✌️').replace('바위', '✊️').replace('보', '✋')
        elif (bot_rsp == "가위" and user_rsp == "바위") or (bot_rsp == "보" and user_rsp == "가위") or (
                bot_rsp == "바위" and user_rsp == "보"):
            answer = "저는 " + bot_rsp + "를 냈고, 당신은 " + user_rsp + "를 내셨내요.\n" + "우으... 아쉽지만 제가 졌습니다~"
            answer = answer.replace('가위', '✌️').replace('바위', '✊️').replace('보', '✋')
        elif (bot_rsp == "바위" and user_rsp == "가위") or (bot_rsp == "가위" and user_rsp == "보") or (
                bot_rsp == "보" and user_rsp == "바위"):
            answer = "저는 " + bot_rsp + "를 냈고, 당신은 " + user_rsp + "를 내셨내요.\n" + "우효~ 제가 이겼어요~"
            answer = answer.replace('가위', '✌️').replace('바위', '✊️').replace('보', '✋')
        else:
            embed = discord.Embed(title="가위바위보 실패...", description="가위, 바위, 보 중에서만 내셔야죠...", color=800000)
            await ctx.channel.send(embed=embed)
            return
        embed = discord.Embed(title="가위바위보 결과!", description=answer, color=800000)
        await ctx.channel.send(embed=embed)
        return


@bot.command()
async def 홀짝(ctx):
    import random
    dice = random.randint(1, 6)

    embed = discord.Embed(title='홀, 짝중 하나를 골라주세요~',
                          description='선택 한 뒤 어떤 수가 나왔는지 알려드려요~')
    embed.add_field(name='🎲주사위의 눈🎲', value='???')
    embed.add_field(name='홀수', value='🔴')
    embed.add_field(name='짝수', value='🔵')
    await ctx.message.delete()
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("🔴")
    await msg.add_reaction('🔵')

    try:
        def check(reaction, user):
            return str(reaction) in ['🔴', '🔵'] and \
                user == ctx.author and reaction.message.id == msg.id

        reaction, user = await bot.wait_for('reaction_add', check=check)

        if (str(reaction) == '🔴' and dice % 2 == 1) or \
                (str(reaction) == '🔵' and dice % 2 == 0):
            embed = discord.Embed(title='운이 좋으시군요~',
                                  description='계속해서 도전해보세요~')
            embed.add_field(name='🎲', value=str(dice))
            await msg.clear_reactions()
            await msg.edit(embed=embed)
            await ctx.message.delete()

        else:
            embed = discord.Embed(title='허접~',
                                  description='심각하네요~')
            embed.add_field(name='🎲', value=str(dice))
            await msg.clear_reactions()
            await msg.edit(embed=embed)
            await ctx.message.delete()
    except:
        pass

@bot.command()
async def 투표(ctx):
    embed = discord.Embed(title='찬성, 반대중 하나를 골라주세요.',
                          description='신중하게 투표해주세요~')
    embed.add_field(name='찬성', value='😀')
    embed.add_field(name='반대', value='🥱')
    await ctx.message.delete()
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("😀")
    await msg.add_reaction('🥱')

@bot.command()
async def 요일투표(ctx):
    embed = discord.Embed(title='왼쪽부터 순서대로 월화수목금토일 입니다.',
                          description='신중하게 투표해주세요~')
    embed.add_field(name='', value='')
    embed.add_field(name='', value='')
    await ctx.message.delete()
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("🌙")
    await msg.add_reaction('🔥')
    await msg.add_reaction("🌊")
    await msg.add_reaction("🪵")
    await msg.add_reaction("⚔️")
    await msg.add_reaction("⏳")
    await msg.add_reaction("🌞")

@bot.command()
async def 주사위(ctx):
    # https://kr.piliapp.com/symbol/dice/
    dice0 = {1: '⚀-1', 2: '⚁-2', 3: '⚂-3', 4: '⚃-4', 5: '⚄-5', 6: '⚅-6'}
    embed = discord.Embed(title="ㅤㅤ주사위게임 결과", color=0x4432a8)
    dice1 = random.randrange(1, 7)
    dice11 = dice0[dice1]
    dice2 = random.randrange(1, 7)
    dice22 = dice0[dice2]
    embed.add_field(name="🎲굴린사람🎲", value=f"ㅤㅤ{dice11}", inline=True)
    embed.add_field(name="🎲상대방🎲", value=f"ㅤㅤ{dice22}", inline=True)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def 모집(ctx):
    embed = discord.Embed(title='참여할 사람은 반응 누르셈!',
                          description='언제든지 변경 가능함!')
    embed.add_field(name='', value='')
    embed.add_field(name='', value='')
    await ctx.message.delete()
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("🥳")























# 유희왕 카드 데이터베이스
@bot.command()
async def 테마(ctx):
    embed = discord.Embed(title='등록된 테마 이름입니다.',
                          colour=0xE67E22)
    embed.add_field(name='아래와 같습니다.', value='트라이브리게이드\r\n트브게\r\nㅤ\r\n트라게\r\nㅤ\r\n섬도희\r\n섬도\r\nㅤ\r\n상검\r\nㅤ\r\n루닉\r\nㅤ\r\n미캉코\r\n캉코\r\nㅤ\r\nTG\r\n테크지너스\r\n티지\r\n티쥐\r\ntg\r\nㅤ\r\n엑소시스터\r\n엑소\r\nㅤ\r\n샐러맨그레이트\r\n샐그\r\n샐러맨')
    embed.set_footer(text='원하는 카드를 찾으시길..')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5 * 2)
    await ctx.message.delete()

#트라이브리게이드

@bot.command()
async def 트라이브리게이드(ctx):
    embed = discord.Embed(title='등록된 트라이브리게이드 카드 검색 키워드입니다.',
                          colour=0x206694)
    embed.set_thumbnail(url='https://i.ibb.co/CMcGgV2/20230310221851.png')
    embed.add_field(name='아래와 같습니다.', value='트라이브리게이드흉조슈라이그\r\n슈라이그\r\n트라이브리게이드키트\r\n키트\r\n트라이브리게이드괴격베어브룸\r\n베어브룸\r\n괴격\r\n트라이브리게이드너벨\r\n너벨\r\n트라이브리게이드케라스\r\n케라스\r\n트라이브리게이드프랙탈\r\n프랙탈\r\n트라이브리게이드도화페리지트\r\n페리지트\r\n트라이브리게이드은탄루갈\r\n루갈\r\n트라이브리게이드메르쿠리에\r\n메르쿠리에\r\n트라이브리게이드암즈부케팔로스2\r\n부케팔로스2\r\n트브게링크5\r\n트라이브리게이드라인\r\n트라이브리게이드에어본\r\n트라이브리게이드랑데부\r\n랑데부\r\n트라이브리게이드데드라인\r\n트라이브리게이드로어\r\n트라이브리게이드리볼트\r\n리볼트\r\n트라이브리게이드오스\r\n트라이브리게이드토큰\r\n혼식룡브리간드\r\n격철룡린드블룸', inline=True)
    embed.set_footer(text='부족간의 벽을 초월하여 손을 잡은 동료들의 모습, 평화를 얻기 위해, 트라이브리게이드의 포효를 울리는 당신에게.')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라게(ctx):
    embed = discord.Embed(title='등록된 트라이브리게이드 카드 검색 키워드입니다.',
                          colour=0x206694)
    embed.set_thumbnail(url='https://i.ibb.co/CMcGgV2/20230310221851.png')
    embed.add_field(name='아래와 같습니다.', value='트라이브리게이드흉조슈라이그\r\n슈라이그\r\n트라이브리게이드키트\r\n키트\r\n트라이브리게이드괴격베어브룸\r\n베어브룸\r\n괴격\r\n트라이브리게이드너벨\r\n너벨\r\n트라이브리게이드케라스\r\n케라스\r\n트라이브리게이드프랙탈\r\n프랙탈\r\n트라이브리게이드도화페리지트\r\n페리지트\r\n트라이브리게이드은탄루갈\r\n루갈\r\n트라이브리게이드메르쿠리에\r\n메르쿠리에\r\n트라이브리게이드암즈부케팔로스2\r\n부케팔로스2\r\n트브게링크5\r\n트라이브리게이드라인\r\n트라이브리게이드에어본\r\n트라이브리게이드랑데부\r\n랑데부\r\n트라이브리게이드데드라인\r\n트라이브리게이드로어\r\n트라이브리게이드리볼트\r\n리볼트\r\n트라이브리게이드오스\r\n트라이브리게이드토큰\r\n혼식룡브리간드\r\n격철룡린드블룸', inline=True)
    embed.set_footer(text='부족간의 벽을 초월하여 손을 잡은 동료들의 모습, 평화를 얻기 위해, 트라이브리게이드의 포효를 울리는 당신에게.')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5 * 2)
    await ctx.message.delete()

@bot.command()
async def 트브게(ctx):
    embed = discord.Embed(title='등록된 트라이브리게이드 카드 검색 키워드입니다.',
                          colour=0x206694)
    embed.set_thumbnail(url='https://i.ibb.co/CMcGgV2/20230310221851.png')
    embed.add_field(name='아래와 같습니다.', value='트라이브리게이드흉조슈라이그\r\n슈라이그\r\n트라이브리게이드키트\r\n키트\r\n트라이브리게이드괴격베어브룸\r\n베어브룸\r\n괴격\r\n트라이브리게이드너벨\r\n너벨\r\n트라이브리게이드케라스\r\n케라스\r\n트라이브리게이드프랙탈\r\n프랙탈\r\n트라이브리게이드도화페리지트\r\n페리지트\r\n트라이브리게이드은탄루갈\r\n루갈\r\n트라이브리게이드메르쿠리에\r\n메르쿠리에\r\n트라이브리게이드암즈부케팔로스2\r\n부케팔로스2\r\n트브게링크5\r\n트라이브리게이드라인\r\n트라이브리게이드에어본\r\n트라이브리게이드랑데부\r\n랑데부\r\n트라이브리게이드데드라인\r\n트라이브리게이드로어\r\n트라이브리게이드리볼트\r\n리볼트\r\n트라이브리게이드오스\r\n트라이브리게이드토큰\r\n혼식룡브리간드\r\n격철룡린드블룸', inline=True)
    embed.set_footer(text='부족간의 벽을 초월하여 손을 잡은 동료들의 모습, 평화를 얻기 위해, 트라이브리게이드의 포효를 울리는 당신에게.')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5 * 2)
    await ctx.message.delete()



@bot.command()
async def 트라이브리게이드흉조슈라이그(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/99726621.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='비행야수족 / 링크 / 효과\r\n야수족 / 야수전사족 / 비행야수족 몬스터 2장 이상', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 이 카드가 특수 소환에 성공했을 경우, 또는 자신 필드에 이 카드 이외의 야수족 / 야수전사족 / 비행야수족 몬스터가 특수 소환되었을 경우에 발동할 수 있다.\r\n필드의 카드 1장을 고르고 제외한다.\r\nㅤ\r\n②: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다. 제외되어 있는 자신의 야수족 / 야수전사족 / 비행야수족 몬스터의 수 이하의 레벨을 가지는 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 덱에서 패에 넣는다.', inline=True)
    embed.set_footer(text='부족을 넘어 결속하는 의용군, 트라이브리게이드의 리더. 강철 무장을 몸에 설치고, 전장에 내려온다.')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 슈라이그(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/99726621.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='비행야수족 / 링크 / 효과\r\n야수족 / 야수전사족 / 비행야수족 몬스터 2장 이상', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 이 카드가 특수 소환에 성공했을 경우, 또는 자신 필드에 이 카드 이외의 야수족 / 야수전사족 / 비행야수족 몬스터가 특수 소환되었을 경우에 발동할 수 있다.\r\n필드의 카드 1장을 고르고 제외한다.\r\nㅤ\r\n②: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다. 제외되어 있는 자신의 야수족 / 야수전사족 / 비행야수족 몬스터의 수 이하의 레벨을 가지는 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 덱에서 패에 넣는다.', inline=True)
    embed.set_footer(text='부족을 넘어 결속하는 의용군, 트라이브리게이드의 리더. 강철 무장을 몸에 설치고, 전장에 내려온다.')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드키트(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/56196385.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='야수족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 묘지에서 야수족 / 야수전사족 / 비행야수족 몬스터를 임의의 수만큼 제외하고 발동할 수 있다.\r\n제외한수와 같은 수의 링크 마커를 가지는 야수족 / 야수전사족 / 비행야수족 링크 몬스터 1장을 엑스트라 덱에서 특수 소환한다.\r\n이 턴에, 자신은 야수족 / 야수전사족 / 비행야수족 몬스터 밖에 링크 소재로 할 수 없다.\r\nㅤ\r\n②: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다.\r\n덱에서 "트라이브리게이드" 키트 이외의 "트라이브리게이드" 카드 1장을 묘지로 보낸다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 키트(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/56196385.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='야수족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 묘지에서 야수족 / 야수전사족 / 비행야수족 몬스터를 임의의 수만큼 제외하고 발동할 수 있다.\r\n제외한수와 같은 수의 링크 마커를 가지는 야수족 / 야수전사족 / 비행야수족 링크 몬스터 1장을 엑스트라 덱에서 특수 소환한다.\r\n이 턴에, 자신은 야수족 / 야수전사족 / 비행야수족 몬스터 밖에 링크 소재로 할 수 없다.\r\nㅤ\r\n②: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다.\r\n덱에서 "트라이브리게이드" 키트 이외의 "트라이브리게이드" 카드 1장을 묘지로 보낸다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 베어브룸(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/47163170.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='야수족 / 링크 / 효과 "트라이브리게이드" 몬스터 2장', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 패를 2장 버리고, 제외되어 있는 자신의 레벨 4 이하의 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 대상으로 하여 발동할 수 있다.\r\n그 몬스터를 특수 소환한다.\r\nㅤ\r\n②: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다.\r\n덱에서 "트라이브리게이드" 마법 / 함정 카드 1장을 패에 넣는다.\r\n그 후, 패를 1장 고르고 덱 맨 아래로 되돌린다.\r\n이 효과의 발동 후, 턴 종료시까지 자신은 "트라이브리게이드" 몬스터밖에 특수 소환할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 괴격(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/47163170.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='야수족 / 링크 / 효과 "트라이브리게이드" 몬스터 2장', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 패를 2장 버리고, 제외되어 있는 자신의 레벨 4 이하의 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 대상으로 하여 발동할 수 있다.\r\n그 몬스터를 특수 소환한다.\r\nㅤ\r\n②: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다.\r\n덱에서 "트라이브리게이드" 마법 / 함정 카드 1장을 패에 넣는다.\r\n그 후, 패를 1장 고르고 덱 맨 아래로 되돌린다.\r\n이 효과의 발동 후, 턴 종료시까지 자신은 "트라이브리게이드" 몬스터밖에 특수 소환할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드괴격베어브룸(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/47163170.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='야수족 / 링크 / 효과 "트라이브리게이드" 몬스터 2장', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 패를 2장 버리고, 제외되어 있는 자신의 레벨 4 이하의 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 대상으로 하여 발동할 수 있다.\r\n그 몬스터를 특수 소환한다.\r\nㅤ\r\n②: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다.\r\n덱에서 "트라이브리게이드" 마법 / 함정 카드 1장을 패에 넣는다.\r\n그 후, 패를 1장 고르고 덱 맨 아래로 되돌린다.\r\n이 효과의 발동 후, 턴 종료시까지 자신은 "트라이브리게이드" 몬스터밖에 특수 소환할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드너벨(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/14816857.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='비행야수족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 자신 묘지에서 야수족 / 야수전사족 / 비행야수족 몬스터를 임의의 수만큼 제외하고 발동할 수 있다.\r\n제외한 수와 같은 수의 링크 마커를 가지는 야수족 / 야수전사족 / 비행야수족 링크 몬스터 1장을 엑스트라 덱에서 특수 소환한다.\r\n이 턴에 자신은 야수족 / 야수전사족 / 비행야수족 몬스터밖에 링크 소재로 할 수 없다.\r\nㅤ\r\n②: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다.\r\n덱에서 "트라이브리게이드 너벨" 이외의 "트라이브리게이드" 몬스터 1장을 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 너벨(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/14816857.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='비행야수족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 자신 묘지에서 야수족 / 야수전사족 / 비행야수족 몬스터를 임의의 수만큼 제외하고 발동할 수 있다.\r\n제외한 수와 같은 수의 링크 마커를 가지는 야수족 / 야수전사족 / 비행야수족 링크 몬스터 1장을 엑스트라 덱에서 특수 소환한다.\r\n이 턴에 자신은 야수족 / 야수전사족 / 비행야수족 몬스터밖에 링크 소재로 할 수 없다.\r\nㅤ\r\n②: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다.\r\n덱에서 "트라이브리게이드 너벨" 이외의 "트라이브리게이드" 몬스터 1장을 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드케라스(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/50810455.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='야수족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 패에서 이 카드 이외의 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 버리고 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\nㅤ\r\n②: 자신 묘지에서 야수족 / 야수전사족 / 비행야수족 몬스터를 임의의 수만큼 제외하고 발동할 수 있다.\r\n제외한 수와 같은 수의 링크 마커를 가지는 야수족 / 야수전사족 / 비행야수족 링크 몬스터 1장을 엑스트라 덱에서 특수 소환한다.\r\n이 턴에 자신은 야수족 / 야수전사족 / 비행야수족 몬스터밖에 링크 소재로 할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 케라스(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/50810455.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='야수족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 패에서 이 카드 이외의 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 버리고 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\nㅤ\r\n②: 자신 묘지에서 야수족 / 야수전사족 / 비행야수족 몬스터를 임의의 수만큼 제외하고 발동할 수 있다.\r\n제외한 수와 같은 수의 링크 마커를 가지는 야수족 / 야수전사족 / 비행야수족 링크 몬스터 1장을 엑스트라 덱에서 특수 소환한다.\r\n이 턴에 자신은 야수족 / 야수전사족 / 비행야수족 몬스터밖에 링크 소재로 할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드프랙탈(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/87209160 * 5.jpg', delete_after=60 * 5)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://img.game8.co/3480493/0341495be9a8b691e5ed09d1bb339db1.png/show')
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='야수전사족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 패 / 필드의 이 카드를 묘지로 보내고 발동할 수 있다. 덱에서 레벨 3 이하의 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 묘지로 보낸다.\r\nㅤ\r\n②: 자신 묘지에서 야수족 / 야수전사족 / 비행야수족 몬스터를 임의의 수만큼 제외하고 발동할 수 있다.\r\n제외한 수와 같은 수의 링크 마커를 가지는 야수족 / 야수전사족 / 비행야수족 링크 몬스터 1장을 엑스트라 덱에서 특수 소환한다.\r\n이 턴에 자신은 야수족 / 야수전사족 / 비행야수족 몬스터밖에 링크 소재로 할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 프랙탈(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/87209160 * 5.jpg', delete_after=60 * 5)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://img.game8.co/3480493/0341495be9a8b691e5ed09d1bb339db1.png/show')
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='야수전사족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 패 / 필드의 이 카드를 묘지로 보내고 발동할 수 있다. 덱에서 레벨 3 이하의 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 묘지로 보낸다.\r\nㅤ\r\n②: 자신 묘지에서 야수족 / 야수전사족 / 비행야수족 몬스터를 임의의 수만큼 제외하고 발동할 수 있다.\r\n제외한 수와 같은 수의 링크 마커를 가지는 야수족 / 야수전사족 / 비행야수족 링크 몬스터 1장을 엑스트라 덱에서 특수 소환한다.\r\n이 턴에 자신은 야수족 / 야수전사족 / 비행야수족 몬스터밖에 링크 소재로 할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드도화페리지트(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/26847978.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='야수족 / 링크 / 효과\r\n야수족 / 야수전사족 / 비행야수족 몬스터 2장', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 메인 페이즈에 발동할 수 있다. 패에서 레벨 4 이하의 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 특수 소환한다.\r\n이 효과의 발동 후, 턴 종료시까지 자신은 야수족 / 야수전사족 / 비행야수족 몬스터밖에 링크 소재로 할 수 없다.\r\nㅤ\r\n②: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다. 자신은 덱에서 1장 드로우하고, 그 후 패를 1장 골라 덱 맨 아래로 되돌린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 페리지트(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/26847978.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='야수족 / 링크 / 효과\r\n야수족 / 야수전사족 / 비행야수족 몬스터 2장', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 메인 페이즈에 발동할 수 있다. 패에서 레벨 4 이하의 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 특수 소환한다.\r\n이 효과의 발동 후, 턴 종료시까지 자신은 야수족 / 야수전사족 / 비행야수족 몬스터밖에 링크 소재로 할 수 없다.\r\nㅤ\r\n②: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다. 자신은 덱에서 1장 드로우하고, 그 후 패를 1장 골라 덱 맨 아래로 되돌린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드은탄루갈(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/52331012.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='야수전사족 / 링크 / 효과\r\n야수족 / 야수전사족 / 비행야수족 몬스터 2장 이상', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 상대 메인 페이즈에 발동할 수 있다. 자신의 패 / 묘지에서 레벨 4 이하의 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 고르고 특수 소환한다.\r\n이 효과로 특수 소환한 몬스터의 효과는 무효화되고, 엔드 페이즈에 주인의 패로 되돌아간다.\r\nㅤ\r\n②: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다. 상대 필드의 모든 몬스터의 공격력은 턴 종료시까지, 자신 필드 몬스터 종족의 종류 × 300 내린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 루갈(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/52331012.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='야수전사족 / 링크 / 효과\r\n야수족 / 야수전사족 / 비행야수족 몬스터 2장 이상', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 상대 메인 페이즈에 발동할 수 있다. 자신의 패 / 묘지에서 레벨 4 이하의 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 고르고 특수 소환한다.\r\n이 효과로 특수 소환한 몬스터의 효과는 무효화되고, 엔드 페이즈에 주인의 패로 되돌아간다.\r\nㅤ\r\n②: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다. 상대 필드의 모든 몬스터의 공격력은 턴 종료시까지, 자신 필드 몬스터 종족의 종류 × 300 내린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드메르쿠리에(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/19096726.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='비행야수족 / 효과\r\n야수족 / 야수전사족 / 비행야수족 몬스터 2장 이상', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 자신 필드에 "알버스의 낙윤"을 융합 소재로 하는 융합 몬스터가 존재하고, 상대가 몬스터의 효과를 발동했을 때, 패 / 필드의 이 카드를 묘지로 보내고 발동할 수 있다. 그 효과를 무효로 한다.\r\nㅤ\r\n②: 이 카드가 제외되었을 경우에 발동할 수 있다. "트라이브리게이드 메르쿠리에"가 아닌, "알버스의 낙윤" 1장 또는 그 카드명이 쓰여진 몬스터 1장을 덱에서 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 메르쿠리에(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/19096726.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='비행야수족 / 효과\r\n야수족 / 야수전사족 / 비행야수족 몬스터 2장 이상', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 자신 필드에 "알버스의 낙윤"을 융합 소재로 하는 융합 몬스터가 존재하고, 상대가 몬스터의 효과를 발동했을 때, 패 / 필드의 이 카드를 묘지로 보내고 발동할 수 있다. 그 효과를 무효로 한다.\r\nㅤ\r\n②: 이 카드가 제외되었을 경우에 발동할 수 있다. "트라이브리게이드 메르쿠리에"가 아닌, "알버스의 낙윤" 1장 또는 그 카드명이 쓰여진 몬스터 1장을 덱에서 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 트라이브리게이드암즈부케팔로스2(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/10019086.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='비행야수족 / 링크 / 효과\r\n야수족 / 야수전사족 / 비행야수족 몬스터 3장 이상', value='자신 묘지의 "트라이브리게이드" 마법 / 함정 카드가 2장 이하일 경우, 이 카드는 엑스트라 덱에서 특수 소환할 수 없다.이 카드명의 ③의 효과는 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 자신이 몬스터의 특수 소환에 성공했을 때에는, 상대는 효과를 발동할 수 없다.\r\nㅤ\r\n②: 몬스터의 공격 선언시에 발동할 수 있다. 이 카드 및 상대 필드의 카드를 전부 제외한다.\r\nㅤ\r\n③: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다. 엑스트라 덱에서 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 묘지로 보낸다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 부케팔로스2(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/10019086.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='비행야수족 / 링크 / 효과\r\n야수족 / 야수전사족 / 비행야수족 몬스터 3장 이상', value='자신 묘지의 "트라이브리게이드" 마법 / 함정 카드가 2장 이하일 경우, 이 카드는 엑스트라 덱에서 특수 소환할 수 없다.이 카드명의 ③의 효과는 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 자신이 몬스터의 특수 소환에 성공했을 때에는, 상대는 효과를 발동할 수 없다.\r\nㅤ\r\n②: 몬스터의 공격 선언시에 발동할 수 있다. 이 카드 및 상대 필드의 카드를 전부 제외한다.\r\nㅤ\r\n③: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다. 엑스트라 덱에서 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 묘지로 보낸다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트브게링크5(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/10019086.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='비행야수족 / 링크 / 효과\r\n야수족 / 야수전사족 / 비행야수족 몬스터 3장 이상', value='자신 묘지의 "트라이브리게이드" 마법 / 함정 카드가 2장 이하일 경우, 이 카드는 엑스트라 덱에서 특수 소환할 수 없다.이 카드명의 ③의 효과는 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 자신이 몬스터의 특수 소환에 성공했을 때에는, 상대는 효과를 발동할 수 없다.\r\nㅤ\r\n②: 몬스터의 공격 선언시에 발동할 수 있다. 이 카드 및 상대 필드의 카드를 전부 제외한다.\r\nㅤ\r\n③: 이 카드가 묘지로 보내졌을 경우에 발동할 수 있다. 엑스트라 덱에서 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 묘지로 보낸다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 트라이브리게이드라인(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/25908748.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 지속', value='이 카드명의 ②의 효과는 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 이 카드가 마법 & 함정 존에 존재하는 한, 자신은 야수족 / 야수전사족 / 비행야수족 몬스터밖에 엑스트라 덱에서 특수 소환할 수 없다.\r\nㅤ\r\n②: 자신의 패 / 필드에서 몬스터 1장을 묘지로 보내고 발동할 수 있다. 묘지로 보낸 몬스터와는 원래의 종족이 다른 "트라이브리게이드" 몬스터 1장을 덱에서 패에 넣는다.\r\nㅤ\r\n③: 마법 & 함정 존의 이 카드가 상대 효과로 파괴되었을 경우에 발동할 수 있다. 이 턴에 상대는 공격 선언할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드에어본(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/51097887.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='①: 자신 필드의 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터의 공격력 이하로 종족이 다른 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 덱에서 수비 표시로 특수 소환한다. 이 효과로 특수 소환한 몬스터의 효과는 턴 종료시까지 무효화된다. 이 효과의 발동 후, 턴 종료시까지 자신은 링크 몬스터밖에 엑스트라 덱에서 특수 소환할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드랑데부(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/96378317.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 자신 필드의 링크 상태의 야수족 / 야수전사족 / 비행야수족 몬스터를 임의의 수만큼 대상으로 하고 발동할 수 있다. 그 몬스터의 공격력은 턴 종료시까지 700 올린다.\r\nㅤ\r\n②: 자신 필드의 링크 상태의 야수족 / 야수전사족 / 비행야수족 몬스터가 전투 / 효과로 파괴될 경우, 대신에 묘지의 이 카드를 제외할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 랑데부(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/96378317.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 자신 필드의 링크 상태의 야수족 / 야수전사족 / 비행야수족 몬스터를 임의의 수만큼 대상으로 하고 발동할 수 있다. 그 몬스터의 공격력은 턴 종료시까지 700 올린다.\r\nㅤ\r\n②: 자신 필드의 링크 상태의 야수족 / 야수전사족 / 비행야수족 몬스터가 전투 / 효과로 파괴될 경우, 대신에 묘지의 이 카드를 제외할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 트라이브리게이드데드라인(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/7889323.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 지속', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 자신 필드에 야수족 / 야수전사족 / 비행야수족 몬스터가 특수 소환되었을 경우, 제외되어 있는 자신의 "트라이브리게이드" 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터를 패에 넣는다.\r\nㅤ\r\n②: 자신의 "트라이브리게이드" 몬스터가 상대 몬스터와 전투를 실행한 데미지 계산 후에 발동할 수 있다. 그 상대 몬스터를 주인의 패로 되돌린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 데드라인(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/7889323.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 지속', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 자신 필드에 야수족 / 야수전사족 / 비행야수족 몬스터가 특수 소환되었을 경우, 제외되어 있는 자신의 "트라이브리게이드" 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터를 패에 넣는다.\r\nㅤ\r\n②: 자신의 "트라이브리게이드" 몬스터가 상대 몬스터와 전투를 실행한 데미지 계산 후에 발동할 수 있다. 그 상대 몬스터를 주인의 패로 되돌린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드로어(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/7889323.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\nㅤ\r\n①: 자신 필드에 링크 몬스터가 존재할 경우, 덱 / 엑스트라 덱에서 "트라이브리게이드" 카드 1장을 묘지로 보내고, 필드의 효과 몬스터 1장을 대상으로 하여 발동할 수 있다. 묘지로 보낸 카드의 종류에 따라 이하의 효과를 적용한다.\r\n●몬스터: 대상 몬스터의 공격력은 턴 종료시까지 0 이 된다.\r\n●마법: 대상 몬스터의 효과를 턴 종료시까지 무효로 한다.\r\n●함정: 대상 몬스터를 주인의 패로 되돌린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드리볼트(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/40975243.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\nㅤ\r\n이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.①: 자신 묘지의 몬스터 및 제외되어 있는 자신 몬스터 중에서, 야수족 / 야수전사족 / 비행야수족 몬스터를 임의의 수만큼 골라 효과를 무효로 하여 특수 소환하고, 그 몬스터만을 소재로서 "트라이브리게이드" 링크 몬스터 1장을 링크 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 리볼트(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/40975243.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\nㅤ\r\n이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.①: 자신 묘지의 몬스터 및 제외되어 있는 자신 몬스터 중에서, 야수족 / 야수전사족 / 비행야수족 몬스터를 임의의 수만큼 골라 효과를 무효로 하여 특수 소환하고, 그 몬스터만을 소재로서 "트라이브리게이드" 링크 몬스터 1장을 링크 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드오스(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/86379342.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 ①②의 효과는 1턴에 1번, 어느 쪽이든 1개밖에 사용할 수 없다.\r\nㅤ\r\n①: 자신 필드의 링크 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터와는 종족이 다른 야수족 / 야수전사족 / 비행야수족 몬스터 1장을 자신의 패 / 묘지에서 고르고 특수 소환한다.\r\nㅤ\r\n②: 자신 필드에 야수족 / 야수전사족 / 비행야수족 몬스터가 각각 1장 이상 존재할 경우, 묘지의 이 카드를 제외하고, 상대 필드의 앞면 표시의 마법 / 함정 카드 1장을 대상으로 하여 발동할 수 있다. 그 카드의 효과를 턴 종료시까지 무효로 한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이브리게이드토큰(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://i.ibb.co/pvrc5rd/20230317232428.png', delete_after=60 * 5)
    embed = discord.Embed(colour=0x95A5A6)
    embed.add_field(name='토큰', value='이 카드는 토큰 또는 카운터로 사용할 수 있다.', inline=True)
    embed.set_footer(text='사격 준비를 하라─')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 혼식룡브리간드(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/34848821.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x71368A)
    embed.add_field(name='야수족 / 융합 / 효과\r\n"알버스의 낙윤" + 레벨 8 이상의 몬스터', value='이 카드명의 ③의 효과는 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 이 카드는 전투로는 파괴되지 않는다.\r\nㅤ\r\n②: 융합 소환한 이 카드가 몬스터 존에 존재하는 한, 상대는 자신 필드의 다른 몬스터를 몬스터 효과의 대상으로 할 수 없다.\r\nㅤ\r\n③: 이 카드가 묘지로 보내진 턴의 엔드 페이즈에 발동할 수 있다. 덱에서 "트라이브리게이드" 몬스터 또는 "알버스의 낙윤" 1장을 고르고, 패에 넣거나 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 격철룡린드블룸(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/34848821.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x71368A)
    embed.add_field(name='비행야수족 / 융합 / 효과\r\n"알버스의 낙윤" ＋ 야수족 / 야수전사족 / 비행야수족 몬스터', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\nㅤ\r\n①: 융합 / 싱크로 / 엑시즈 / 링크 몬스터의 효과가 발동했을 때에 발동할 수 있다. 그 효과를 무효로 한다. 그 후, 필드의 몬스터 1장을 고르고 주인의 패로 되돌릴 수 있다.\r\nㅤ\r\n②: 상대 턴에, 이 카드가 묘지에 존재할 경우, 자신 묘지의 "알버스의 낙윤" 1장을 대상으로 하고 발동할 수 있다. 그 몬스터와 이 카드 중, 1장을 특수 소환하고, 나머지 1장을 제외한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()
















#섬도희
@bot.command()
async def 섬도희(ctx):
    embed = discord.Embed(title='등록된 섬도희 카드 검색 키워드입니다.',
                          colour=0x206694)
    embed.set_thumbnail(url='https://i.ibb.co/BCWVj9g/df0778f-7eab0ebe-2bd2-42a2-92cc-fde5360 * 5cce71.png')
    embed.add_field(name='아래와 같습니다.',value='엘론\r\n섬도희레이\r\n레이\r\n섬도희로제\r\n로제\r\n무의현자아카스\r\n아카스\r\n지의현자힘멜\r\n힘멜\r\n자애의현자시에라\r\n시에라\r\n섬술병기HAMP\r\n함프\r\n섬술병기\r\n섬도희카가리\r\n카가리\r\n섬도희시즈쿠\r\n시즈쿠\r\n섬도희하야테\r\n하야테\r\n섬도희카이나\r\n카이나\r\n섬도희지크\r\n지크\r\n섬도희아자레아\r\n아자레아\r\n섬도기동인게이지\r\n인게이지\r\n섬도술식애프터버너\r\n애프터버너\r\n섬도술식재밍웨이브\r\n재밍웨이브\r\n섬도술식백터드블래스트\r\n섬도블래스트\r\n백터드블래스트\r\n섬도술식시저즈크로스\r\n시저즈크로스\r\n섬도기호넷비트\r\n호넷비트\r\n호넷\r\n섬도기위도우앵커\r\n앵커\r\n위도우앵커\r\n섬도기이글부스터\r\n이글부스터\r\n섬도기샤크캐논\r\n샤크캐논\r\n섬도기동링케이지\r\n링케이지\r\n섬도기구허큘리베이스\r\n허큘리베이스\r\n섬도기관멀티롤\r\n멀티롤\r\n섬도공역에리어제로\r\n에리어제로\r\n섬도희토큰',inline=True)
    embed.set_footer(text='섬도술식, 전개!! 섬멸하라!!')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5 * 2)
    await ctx.message.delete()

@bot.command()
async def 섬도(ctx):
    embed = discord.Embed(title='등록된 섬도희 카드 검색 키워드입니다.',
                          colour=0x206694)
    embed.set_thumbnail(url='https://i.ibb.co/BCWVj9g/df0778f-7eab0ebe-2bd2-42a2-92cc-fde5360 * 5cce71.png')
    embed.add_field(name='아래와 같습니다.', value='엘론\r\n섬도희레이\r\n레이\r\n섬도희로제\r\n로제\r\n무의현자아카스\r\n아카스\r\n지의현자힘멜\r\n힘멜\r\n자애의현자시에라\r\n시에라\r\n섬술병기HAMP\r\n함프\r\n섬술병기\r\n섬도희카가리\r\n카가리\r\n섬도희시즈쿠\r\n시즈쿠\r\n섬도희하야테\r\n하야테\r\n섬도희카이나\r\n카이나\r\n섬도희지크\r\n지크\r\n섬도희아자레아\r\n아자레아\r\n섬도기동인게이지\r\n인게이지\r\n섬도술식애프터버너\r\n애프터버너\r\n섬도술식재밍웨이브\r\n재밍웨이브\r\n섬도술식백터드블래스트\r\n섬도블래스트\r\n백터드블래스트\r\n섬도술식시저즈크로스\r\n시저즈크로스\r\n섬도기호넷비트\r\n호넷비트\r\n호넷\r\n섬도기위도우앵커\r\n앵커\r\n위도우앵커\r\n섬도기이글부스터\r\n이글부스터\r\n섬도기샤크캐논\r\n샤크캐논\r\n섬도기동링케이지\r\n링케이지\r\n섬도기구허큘리베이스\r\n허큘리베이스\r\n섬도기관멀티롤\r\n멀티롤\r\n섬도공역에리어제로\r\n에리어제로\r\n섬도희토큰', inline=True)
    embed.set_footer(text='섬도술식, 전개!! 섬멸하라!!')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5 * 2)
    await ctx.message.delete()

@bot.command()
async def 엘론(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/960 * 584564.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='기계족 / 효과', value='이 카드명은 룰상 "섬도" 카드로도 취급한다. 이 카드명의 ①③의 효과는 1턴에 1번, 어느 쪽이든 1개밖에 사용할 수 없다.\r\n①: 자신 / 상대의 메인 페이즈에, 자신 필드의 "섬도희" 몬스터 1장을 대상으로 하고 발동할 수 있다. 자신의 패 / 필드에서 이 카드를 장착 카드로 취급하여 그 몬스터에 장착한다.\r\n②: 이 카드를 장착한 "섬도희" 몬스터의 공격력은 400 올린다.\r\n③: 필드의 이 카드가 파괴되었을 경우에 발동할 수 있다. 덱에서 "섬도" 마법 카드 1장을 묘지로 보낸다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도희레이(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/260 * 577387.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='전사족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드를 릴리스하고 발동할 수 있다. 엑스트라 덱에서 "섬도희" 몬스터 1장을 엑스트라 몬스터 존에 특수 소환한다. 이 효과는 상대 턴에도 발동할 수 있다.\r\n②: 이 카드가 묘지에 존재하는 상태에서, 자신 필드의 앞면 표시의 "섬도희" 링크 몬스터가 상대 효과로 필드에서 벗어났을 경우, 또는 전투로 파괴되었을 경우에 발동할 수 있다. 이 카드를 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 레이(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/260 * 577387.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='전사족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드를 릴리스하고 발동할 수 있다. 엑스트라 덱에서 "섬도희" 몬스터 1장을 엑스트라 몬스터 존에 특수 소환한다. 이 효과는 상대 턴에도 발동할 수 있다.\r\n②: 이 카드가 묘지에 존재하는 상태에서, 자신 필드의 앞면 표시의 "섬도희" 링크 몬스터가 상대 효과로 필드에서 벗어났을 경우, 또는 전투로 파괴되었을 경우에 발동할 수 있다. 이 카드를 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도희로제(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/37351133.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='전사족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 필드에 "섬도희-로제" 이외의 "섬도희" 몬스터가 일반 소환 / 특수 소환되었을 경우에 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 이 카드가 묘지에 존재하는 상태에서, 엑스트라 몬스터 존의 상대 몬스터가 전투로 파괴되었을 경우, 또는 자신의 카드의 효과로 필드에서 벗어났을 경우에 발동할 수 있다. 이 카드를 특수 소환한다. 그 후, 상대 필드의 앞면 표시 몬스터 1장을 고르고, 턴 종료시까지 그 효과를 무효로 할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 로제(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/37351133.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='전사족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 필드에 "섬도희-로제" 이외의 "섬도희" 몬스터가 일반 소환 / 특수 소환되었을 경우에 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 이 카드가 묘지에 존재하는 상태에서, 엑스트라 몬스터 존의 상대 몬스터가 전투로 파괴되었을 경우, 또는 자신의 카드의 효과로 필드에서 벗어났을 경우에 발동할 수 있다. 이 카드를 특수 소환한다. 그 후, 상대 필드의 앞면 표시 몬스터 1장을 고르고, 턴 종료시까지 그 효과를 무효로 할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 무의현자아카스(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/96795312.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='기계족 / 효과', value='이 카드명은 룰상 "섬도" 카드로도 취급한다. 이 카드명의 ①②③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 패에서 마법 카드 1장을 버리고 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 자신 필드의 링크 몬스터가 전투 / 효과로 파괴될 경우, 대신에 자신 묘지의 마법 카드 1장을 제외할 수 있다.\r\n③: 이 카드가 전투 / 효과로 파괴되어 묘지로 보내졌을 경우, 제외되어 있는 자신의 "섬도" 마법 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 아카스(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/96795312.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='기계족 / 효과', value='이 카드명은 룰상 "섬도" 카드로도 취급한다. 이 카드명의 ①②③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 패에서 마법 카드 1장을 버리고 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 자신 필드의 링크 몬스터가 전투 / 효과로 파괴될 경우, 대신에 자신 묘지의 마법 카드 1장을 제외할 수 있다.\r\n③: 이 카드가 전투 / 효과로 파괴되어 묘지로 보내졌을 경우, 제외되어 있는 자신의 "섬도" 마법 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 지의현자힘멜(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/22790910.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='기계족 / 효과', value='이 카드명은 룰상 "섬도" 카드로도 취급한다. 이 카드명의 ①②③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 패에서 마법 카드 1장을 버리고 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n①: 패에서 마법 카드 1장을 버리고 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 자신 필드의 링크 몬스터를 대상으로 하는 효과를 상대가 발동했을 때, 자신 묘지에서 마법 카드 2장을 제외하고 발동할 수 있다. 그 효과를 무효로 한다.\r\n③: 이 카드가 전투 / 효과로 파괴되어 묘지로 보내졌을 경우, 제외되어 있는 자신의 "섬도" 마법 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 힘멜(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/22790910.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='기계족 / 효과', value='이 카드명은 룰상 "섬도" 카드로도 취급한다. 이 카드명의 ①②③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 패에서 마법 카드 1장을 버리고 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n①: 패에서 마법 카드 1장을 버리고 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 자신 필드의 링크 몬스터를 대상으로 하는 효과를 상대가 발동했을 때, 자신 묘지에서 마법 카드 2장을 제외하고 발동할 수 있다. 그 효과를 무효로 한다.\r\n③: 이 카드가 전투 / 효과로 파괴되어 묘지로 보내졌을 경우, 제외되어 있는 자신의 "섬도" 마법 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 자애의현자시애라(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/34456146.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='기계족 / 효과', value='이 카드명은 룰상 "섬도" 카드로도 취급한다. 이 카드명의 ①②③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 패에서 마법 카드 1장을 버리고 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 자신 묘지에서 마법 카드 1장을 제외하고 발동할 수 있다. 이 카드의 컨트롤을 상대에게 넘기고, 자신 묘지에서 "섬도희" 몬스터 1장을 골라 특수 소환한다.\r\n③: 이 카드가 전투 / 효과로 파괴되어 묘지로 보내졌을 경우, 제외되어 있는 자신의 섬도 마법 카드 1장을 대상으로 발동할 수 있다. 그 카드를 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 시애라(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/34456146.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='기계족 / 효과', value='이 카드명은 룰상 "섬도" 카드로도 취급한다. 이 카드명의 ①②③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 패에서 마법 카드 1장을 버리고 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 자신 묘지에서 마법 카드 1장을 제외하고 발동할 수 있다. 이 카드의 컨트롤을 상대에게 넘기고, 자신 묘지에서 "섬도희" 몬스터 1장을 골라 특수 소환한다.\r\n③: 이 카드가 전투 / 효과로 파괴되어 묘지로 보내졌을 경우, 제외되어 있는 자신의 섬도 마법 카드 1장을 대상으로 발동할 수 있다. 그 카드를 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬술병기HAMP(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/33331231.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='기계족 / 효과', value='이 카드명은 룰 상 "섬도" 카드로도 취급한다. 이 카드명의 ①의 방법에 의한 특수 소환은 1턴에 1번밖에 할 수 없다.\r\n①: 자신 필드에 "섬도희" 몬스터가 존재할 경우, 이 카드는 자신 또는 상대 필드의 몬스터 1장을 릴리스하고, 그 컨트롤러의 필드에 패에서 특수 소환할 수 있다.\r\n②: 이 카드가 전투로 파괴되었을 때, 상대 필드의 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬술병기(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/33331231.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='기계족 / 효과', value='이 카드명은 룰 상 "섬도" 카드로도 취급한다. 이 카드명의 ①의 방법에 의한 특수 소환은 1턴에 1번밖에 할 수 없다.\r\n①: 자신 필드에 "섬도희" 몬스터가 존재할 경우, 이 카드는 자신 또는 상대 필드의 몬스터 1장을 릴리스하고, 그 컨트롤러의 필드에 패에서 특수 소환할 수 있다.\r\n②: 이 카드가 전투로 파괴되었을 때, 상대 필드의 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 함프(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/33331231.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='기계족 / 효과', value='이 카드명은 룰 상 "섬도" 카드로도 취급한다. 이 카드명의 ①의 방법에 의한 특수 소환은 1턴에 1번밖에 할 수 없다.\r\n①: 자신 필드에 "섬도희" 몬스터가 존재할 경우, 이 카드는 자신 또는 상대 필드의 몬스터 1장을 릴리스하고, 그 컨트롤러의 필드에 패에서 특수 소환할 수 있다.\r\n②: 이 카드가 전투로 파괴되었을 때, 상대 필드의 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도희카가리(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/63288574.jpg', delete_after=60 * 5)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://i.ibb.co/MPK2rj9/show.png', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n화염 속성 이외의 "섬도희" 몬스터 1장', value='자신은 "섬도희-카가리"를 1턴에 1번밖에 특수 소환할 수 없다.\r\n①: 이 카드가 특수 소환에 성공했을 경우, 자신 묘지의 "섬도" 마법 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 패에 넣는다.\r\n②: 이 카드의 공격력은 자신 묘지의 마법 카드의 수 × 100 올린다.', inline=True)
    embed.set_footer(text='적을 섬멸하는 붉은 무장을 몸에 두른 소녀. 타오르는 칼이 수 많은 군세를 베어 넘긴다.')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 카가리(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/63288574.jpg', delete_after=60 * 5)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://i.ibb.co/MPK2rj9/show.png', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n화염 속성 이외의 "섬도희" 몬스터 1장', value='자신은 "섬도희-카가리"를 1턴에 1번밖에 특수 소환할 수 없다.\r\n①: 이 카드가 특수 소환에 성공했을 경우, 자신 묘지의 "섬도" 마법 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 패에 넣는다.\r\n②: 이 카드의 공격력은 자신 묘지의 마법 카드의 수 × 100 올린다.', inline=True)
    embed.set_footer(text='적을 섬멸하는 붉은 무장을 몸에 두른 소녀. 타오르는 칼이 수 많은 군세를 베어 넘긴다.')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도희시즈쿠(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/90673288.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n물 속성 이외의 "섬도희" 몬스터 1장', value='자신은 "섬도희-시즈쿠"를 1턴에 1번밖에 특수 소환할 수 없다.\r\n①: 상대 필드의 몬스터의 공격력 / 수비력은, 자신 묘지의 마법 카드의 수 × 100 내린다.\r\n②: 이 카드를 특수 소환한 턴의 엔드 페이즈에 발동할 수 있다. 덱에서, 같은 이름의 카드가 자신 묘지에 존재하지 않는 "섬도" 마법 카드 1장을 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 시즈쿠(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/90673288.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n물 속성 이외의 "섬도희" 몬스터 1장', value='자신은 "섬도희-시즈쿠"를 1턴에 1번밖에 특수 소환할 수 없다.\r\n①: 상대 필드의 몬스터의 공격력 / 수비력은, 자신 묘지의 마법 카드의 수 × 100 내린다.\r\n②: 이 카드를 특수 소환한 턴의 엔드 페이즈에 발동할 수 있다. 덱에서, 같은 이름의 카드가 자신 묘지에 존재하지 않는 "섬도" 마법 카드 1장을 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도희하야테(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/8491308.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n바람 속성 이외의 "섬도희" 몬스터 1장', value='자신은 "섬도희-하야테"를 1턴에 1번밖에 특수 소환할 수 없다.\r\n①: 이 카드는 직접 공격할 수 있다.\r\n②: 이 카드가 전투를 실행한 데미지 계산 후에 발동할 수 있다. 덱에서 "섬도" 카드 1장을 묘지로 보낸다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 하야테(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/8491308.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n바람 속성 이외의 "섬도희" 몬스터 1장', value='자신은 "섬도희-하야테"를 1턴에 1번밖에 특수 소환할 수 없다.\r\n①: 이 카드는 직접 공격할 수 있다.\r\n②: 이 카드가 전투를 실행한 데미지 계산 후에 발동할 수 있다. 덱에서 "섬도" 카드 1장을 묘지로 보낸다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도희카이나(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/12421694.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n땅 속성 이외의 "섬도희" 몬스터 1장', value='자신은 "섬도희-카이나"를 1턴에 1번밖에 특수 소환할 수 없다.\r\n①: 이 카드가 특수 소환에 성공했을 경우, 상대 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터는 상대 턴 종료시까지 공격할 수 없다.\r\n②: 이 카드가 몬스터 존에 존재하는 한, 자신이 "섬도" 마법 카드의 효과를 발동할 때마다, 자신은 100 LP 회복한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()



@bot.command()
async def 카이나(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/12421694.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n땅 속성 이외의 "섬도희" 몬스터 1장', value='자신은 "섬도희-카이나"를 1턴에 1번밖에 특수 소환할 수 없다.\r\n①: 이 카드가 특수 소환에 성공했을 경우, 상대 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터는 상대 턴 종료시까지 공격할 수 없다.\r\n②: 이 카드가 몬스터 존에 존재하는 한, 자신이 "섬도" 마법 카드의 효과를 발동할 때마다, 자신은 100 LP 회복한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도희지크(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/75147529.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n"섬도희" 몬스터를 포함하는 몬스터 2장', value='이 카드는 링크 소환으로밖에 특수 소환할 수 없으며, 자신은 "섬도희-지크"를 1턴에 1번밖에 특수 소환할 수 없다.\r\n①: 이 카드가 링크 소환에 성공했을 경우, 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터를 다음 상대 엔드 페이즈까지 제외한다.\r\n②: 1턴에 1번, 이 카드 이외의 자신 필드의 카드 1장을 대상으로 하고 발동할 수 있다. 이 카드의 공격력은 1000 올린다. 추가로, 대상의 카드는 묘지로 보내진다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 지크(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/75147529.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n"섬도희" 몬스터를 포함하는 몬스터 2장', value='이 카드는 링크 소환으로밖에 특수 소환할 수 없으며, 자신은 "섬도희-지크"를 1턴에 1번밖에 특수 소환할 수 없다.\r\n①: 이 카드가 링크 소환에 성공했을 경우, 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터를 다음 상대 엔드 페이즈까지 제외한다.\r\n②: 1턴에 1번, 이 카드 이외의 자신 필드의 카드 1장을 대상으로 하고 발동할 수 있다. 이 카드의 공격력은 1000 올린다. 추가로, 대상의 카드는 묘지로 보내진다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도희아자레아(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/98462037.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n빛 / 어둠 속성 몬스터 2장', value='이 카드는 링크 소환으로밖에 특수 소환할 수 없으며, 자신은 "섬도희－아자레아"를 1턴에 1장밖에 특수 소환할 수 없다.\r\n①: 이 카드가 특수 소환에 성공했을 경우, 필드의 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 파괴한다. 그 후, 자신 묘지의 마법 카드가 3장 이하일 경우, 이 카드를 묘지로 보낸다.\r\n②: 1턴에 1번, 이 카드가 상대 몬스터와 전투를 실행하는 데미지 스텝 개시시, 자신 묘지에서 마법 카드 1장을 제외하고 발동할 수 있다. 그 상대 몬스터를 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 아자레아(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/98462037.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n빛 / 어둠 속성 몬스터 2장', value='이 카드는 링크 소환으로밖에 특수 소환할 수 없으며, 자신은 "섬도희－아자레아"를 1턴에 1장밖에 특수 소환할 수 없다.\r\n①: 이 카드가 특수 소환에 성공했을 경우, 필드의 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 파괴한다. 그 후, 자신 묘지의 마법 카드가 3장 이하일 경우, 이 카드를 묘지로 보낸다.\r\n②: 1턴에 1번, 이 카드가 상대 몬스터와 전투를 실행하는 데미지 스텝 개시시, 자신 묘지에서 마법 카드 1장을 제외하고 발동할 수 있다. 그 상대 몬스터를 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도기동인게이지(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/631660 * 595.jpg', delete_after=60 * 5)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://i.ibb.co/MPK2rj9/show.png', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우에 발동할 수 있다. 덱에서 "섬도기동-인게이지" 이외의 "섬도" 카드 1장을 패에 넣는다. 그 후, 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 자신은 덱에서 1장 드로우할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 인게이지(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/631660 * 595.jpg', delete_after=60 * 5)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://i.ibb.co/MPK2rj9/show.png', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우에 발동할 수 있다. 덱에서 "섬도기동-인게이지" 이외의 "섬도" 카드 1장을 패에 넣는다. 그 후, 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 자신은 덱에서 1장 드로우할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 섬도술식애프터버너(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/99550630.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우, 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터를 파괴한다. 그 후, 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 필드의 마법 / 함정 카드 1장을 고르고 파괴할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 애프터버너(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/99550630.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우, 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터를 파괴한다. 그 후, 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 필드의 마법 / 함정 카드 1장을 고르고 파괴할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도술식재밍웨이브(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/25955749.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우, 필드에 세트된 마법 / 함정 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 파괴한다. 그 후, 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 필드의 몬스터 1장을 고르고 파괴할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 재밍웨이브(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/25955749.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우, 필드에 세트된 마법 / 함정 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 파괴한다. 그 후, 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 필드의 몬스터 1장을 고르고 파괴할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도술식백터드블래스트(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/21623008.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우에 발동할 수 있다. 서로의 덱 위에서 카드를 2장 묘지로 보낸다. 그 후, 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 엑스트라 몬스터 존의 상대 몬스터를 전부 주인의 덱으로 되돌릴 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 백터드블래스트(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/21623008.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우에 발동할 수 있다. 서로의 덱 위에서 카드를 2장 묘지로 보낸다. 그 후, 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 엑스트라 몬스터 존의 상대 몬스터를 전부 주인의 덱으로 되돌릴 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도블래스트(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/21623008.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우에 발동할 수 있다. 서로의 덱 위에서 카드를 2장 묘지로 보낸다. 그 후, 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 엑스트라 몬스터 존의 상대 몬스터를 전부 주인의 덱으로 되돌릴 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도술식시저즈크로스(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/46271408.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우, 자신 묘지의 레벨 4의 "섬도희" 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터를 패에 넣는다. 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 패에 넣지 않고 특수 소환할 수도 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 시저즈크로스(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/46271408.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우, 자신 묘지의 레벨 4의 "섬도희" 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터를 패에 넣는다. 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 패에 넣지 않고 특수 소환할 수도 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도기호넷비트(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://i.ibb.co/8zSR48F/show-1.png', delete_after=60 * 5)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/52340444.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우에 발동할 수 있다. 자신 필드에 "섬도희 토큰"(전사족 / 어둠 / 레벨 1 / 공 0 / 수 0) 1장을 수비 표시로 특수 소환한다. 이 토큰은 릴리스할 수 없다. 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 그 토큰의 공격력 / 수비력은 1500 이 된다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 호넷비트(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://i.ibb.co/8zSR48F/show-1.png', delete_after=60 * 5)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/52340444.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우에 발동할 수 있다. 자신 필드에 "섬도희 토큰"(전사족 / 어둠 / 레벨 1 / 공 0 / 수 0) 1장을 수비 표시로 특수 소환한다. 이 토큰은 릴리스할 수 없다. 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 그 토큰의 공격력 / 수비력은 1500 이 된다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 호넷(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://i.ibb.co/8zSR48F/show-1.png', delete_after=60 * 5)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/52340444.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우에 발동할 수 있다. 자신 필드에 "섬도희 토큰"(전사족 / 어둠 / 레벨 1 / 공 0 / 수 0) 1장을 수비 표시로 특수 소환한다. 이 토큰은 릴리스할 수 없다. 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 그 토큰의 공격력 / 수비력은 1500 이 된다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도기위도우앵커(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/98338152.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우, 필드의 효과 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터의 효과를 턴 종료시까지 무효로 한다. 그 후, 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 그 몬스터의 컨트롤을 엔드 페이즈까지 얻을 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 위도우앵커(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/98338152.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우, 필드의 효과 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터의 효과를 턴 종료시까지 무효로 한다. 그 후, 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 그 몬스터의 컨트롤을 엔드 페이즈까지 얻을 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 앵커(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/98338152.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우, 필드의 효과 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터의 효과를 턴 종료시까지 무효로 한다. 그 후, 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 그 몬스터의 컨트롤을 엔드 페이즈까지 얻을 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도기이글부스터(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/25733157.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우, 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다. 이 턴에, 그 앞면 표시 몬스터는 자신 이외의 카드의 효과를 받지 않는다. 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 추가로 이 턴에, 그 몬스터는 전투로는 파괴되지 않는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 이글부스터(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/25733157.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우, 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다. 이 턴에, 그 앞면 표시 몬스터는 자신 이외의 카드의 효과를 받지 않는다. 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 추가로 이 턴에, 그 몬스터는 전투로는 파괴되지 않는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도기샤크캐논(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/51227866.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우, 상대 묘지의 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터를 제외한다. 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 제외하지 않고 그 몬스터를 자신 필드에 특수 소환할 수 있다. 이 효과로 특수 소환한 몬스터는 공격할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 샤크캐논(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/51227866.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='①: 자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우, 상대 묘지의 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터를 제외한다. 자신 묘지에 마법 카드가 3장 이상 존재할 경우, 제외하지 않고 그 몬스터를 자신 필드에 특수 소환할 수 있다. 이 효과로 특수 소환한 몬스터는 공격할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도기동링케이지(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/9726840.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='①: 자신의 메인 몬스터 존에 몬스터가 존재하지 않는 경우에 발동할 수 있다. 이 카드 이외의 자신 필드의 카드 1장을 골라 묘지로 보내고, 엑스트라 덱에서 "섬도희" 몬스터 1장을 엑스트라 몬스터 존에 특수 소환한다. 자신의 필드 / 묘지에, 빛 속성과 어둠 속성의 "섬도희" 몬스터가 각각 1장 이상 존재하는 경우, 이 효과로 특수 소환한 몬스터의 공격력은 1000 오른다. 이 카드의 발동 후, 턴 종료시까지 자신은 "섬도희" 몬스터 밖에 엑스트라 덱에서 특수 소환할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 링케이지(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/9726840.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='①: 자신의 메인 몬스터 존에 몬스터가 존재하지 않는 경우에 발동할 수 있다. 이 카드 이외의 자신 필드의 카드 1장을 골라 묘지로 보내고, 엑스트라 덱에서 "섬도희" 몬스터 1장을 엑스트라 몬스터 존에 특수 소환한다. 자신의 필드 / 묘지에, 빛 속성과 어둠 속성의 "섬도희" 몬스터가 각각 1장 이상 존재하는 경우, 이 효과로 특수 소환한 몬스터의 공격력은 1000 오른다. 이 카드의 발동 후, 턴 종료시까지 자신은 "섬도희" 몬스터 밖에 엑스트라 덱에서 특수 소환할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도기구허큘리베이스(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/97616504.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 장착', value='자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우에 이 카드를 발동할 수 있다.\r\n①: 장착 몬스터는 직접 공격할 수 없으며, 1번의 배틀 페이즈 중에 몬스터에 2회 공격할 수 있다.\r\n②: 자신 묘지에 마법 카드가 3장 이상 존재하고, 장착 몬스터가 공격으로 몬스터를 파괴했을 경우에 발동한다. 자신은 덱에서 1장 드로우한다.\r\n③: 이 카드가 효과로 필드에서 묘지로 보내졌을 경우, "섬도기구-허큘리베이스" 이외의 자신 묘지의 "섬도" 카드를 3장까지 대상으로 하고 발동할 수 있다. 그 카드를 덱으로 되돌린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 허큘리베이스(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/97616504.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 장착', value='자신 메인 몬스터 존에 몬스터가 존재하지 않을 경우에 이 카드를 발동할 수 있다.\r\n①: 장착 몬스터는 직접 공격할 수 없으며, 1번의 배틀 페이즈 중에 몬스터에 2회 공격할 수 있다.\r\n②: 자신 묘지에 마법 카드가 3장 이상 존재하고, 장착 몬스터가 공격으로 몬스터를 파괴했을 경우에 발동한다. 자신은 덱에서 1장 드로우한다.\r\n③: 이 카드가 효과로 필드에서 묘지로 보내졌을 경우, "섬도기구-허큘리베이스" 이외의 자신 묘지의 "섬도" 카드를 3장까지 대상으로 하고 발동할 수 있다. 그 카드를 덱으로 되돌린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도기관멀티롤(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/2401060 * 59.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 지속', value='①: 1턴에 1번, 이 카드 이외의 자신 필드의 카드 1장을 대상으로 하고 발동할 수 있다. 이 턴에, 자신의 마법 카드의 발동에 대하여 상대는 마법 / 함정 / 몬스터의 효과를 발동할 수 없다. 추가로, 대상의 카드는 묘지로 보내진다.\r\n②: 자신 / 상대의 엔드 페이즈에 발동할 수 있다. 이 턴에, 이 카드가 앞면 표시로 존재하는 동안에 자신이 발동한 "섬도" 마법 카드의 수까지 자신 묘지의 "섬도" 마법 카드를 고르고, 자신 필드에 세트한다(같은 이름의 카드는 1장까지). 이 효과로 세트한 카드는 필드에서 벗어났을 경우에 제외된다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 멀티롤(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/2401060 * 59.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 지속', value='①: 1턴에 1번, 이 카드 이외의 자신 필드의 카드 1장을 대상으로 하고 발동할 수 있다. 이 턴에, 자신의 마법 카드의 발동에 대하여 상대는 마법 / 함정 / 몬스터의 효과를 발동할 수 없다. 추가로, 대상의 카드는 묘지로 보내진다.\r\n②: 자신 / 상대의 엔드 페이즈에 발동할 수 있다. 이 턴에, 이 카드가 앞면 표시로 존재하는 동안에 자신이 발동한 "섬도" 마법 카드의 수까지 자신 묘지의 "섬도" 마법 카드를 고르고, 자신 필드에 세트한다(같은 이름의 카드는 1장까지). 이 효과로 세트한 카드는 필드에서 벗어났을 경우에 제외된다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 섬도공역에리어제로(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/50005218.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 필드', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드 이외의 자신 필드의 카드 1장을 대상으로 하고 발동할 수 있다. 자신의 덱 위에서 카드를 3장 넘긴다. 그 중에서 "섬도" 카드 1장을 고르고 패에 넣을 수 있다. 남은 카드는 덱으로 되돌린다. "섬도" 카드가 넘겨졌을 경우, 추가로 대상의 카드를 묘지로 보낸다.\r\n②: 이 카드가 효과로 필드 존에서 묘지로 보내졌을 경우에 발동할 수 있다. 덱에서 "섬도희" 몬스터 1장을 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 에리어제로(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/50005218.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 필드', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드 이외의 자신 필드의 카드 1장을 대상으로 하고 발동할 수 있다. 자신의 덱 위에서 카드를 3장 넘긴다. 그 중에서 "섬도" 카드 1장을 고르고 패에 넣을 수 있다. 남은 카드는 덱으로 되돌린다. "섬도" 카드가 넘겨졌을 경우, 추가로 대상의 카드를 묘지로 보낸다.\r\n②: 이 카드가 효과로 필드 존에서 묘지로 보내졌을 경우에 발동할 수 있다. 덱에서 "섬도희" 몬스터 1장을 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 섬도희토큰(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/52340445.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x95A5A6)
    embed.add_field(name='전사족 / 일반\r\n이 카드는 "섬도희 토큰"으로 사용할 수 있다.', value='※"섬도희 토큰" 이외의 토큰으로 사용할 경우, 그 토큰의 종족 / 속성 / 레벨 / 공격력 / 수비력을 적용한다.', inline=True)
    embed.set_footer(text='※부연설명: 한 때 한판카드가 30만원을 호가했던 카드이다. 이유: 대회판 한정 배포')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()






#상검

@bot.command()
async def 상검(ctx):
    embed = discord.Embed(title='등록된 상검 카드 검색 키워드입니다.',
                          colour=0xEEEFF1)
    embed.set_thumbnail(url='https://i.postimg.cc/qMs0YvN9/chrome-h9o-RRvqk-TB.jpg')
    embed.add_field(name='아래와 같습니다.', value='TG사이버매지션\r\n사이버매지션\r\nTG탱크러바\r\n탱크러바\r\nTG기어좀비\r\n기어좀비\r\nTG스트라이커\r\nTG제트팔콘\r\n제트팔콘\r\nTG스크류서펜트\r\n스크류서펜트\r\nTG부스터랩토르\r\n부스터랩토르\r\nTG드릴피시\r\n드릴피시\r\nTG로캣샐러맨더\r\n로켓샐러맨더\r\nTG중장갑드래곤\r\n중장갑드래곤\r\nTG메탈스켈리턴\r\n메탈스켈리턴\r\n스켈리턴\r\nTG워울프\r\n워울프\r\nTG러시라이노\r\n러시라이노\r\nTG할버드캐논버스터\r\n할버드캐논버스터\r\nTG레시프로드래곤플라이\r\n레시프로\r\n레시프로드래곤\r\n레시프로플라이\r\n레시프로드래곤플라이\r\n드래곤플라이\r\nTG마이티스트라이커\r\n마이티스트라이커\r\nTG파워글래디에이터\r\n파워글래디에이터\r\nTG하이퍼라이브러리언\r\n하이퍼라이브러리언\r\n라이브러리언\r\nTG원더매지션\r\n원더매지션\r\nTG스타가디언\r\n스타가디언\r\nTG오버드래그너\r\n오버드래그너\r\nTG블레이드건맨\r\n블레이드건맨\r\n슈팅스타드래곤TGEX\r\nTG할버드캐논\r\n할버드캐논\r\nTG글레이브블래스터\r\n글레이브블래스터\r\nTG트라이든트런처\r\n트라이든트\r\nTG브레이크리미터\r\n브레이크리미터\r\nTG올클리어\r\n올클리어\TG클로즈\r\n클로즈\r\nTGX1HL\r\nTGX300\r\nTG1EM1\r\nTGSX1\r\nTGX3DX2\r\n배틀스턴소닉\r\n배틀스턴', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5 * 2)
    await ctx.message.delete()

@bot.command()
async def 상검사막야(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/20001443.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='환룡족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 일반 소환 / 특수 소환에 성공했을 경우, 패의 "상검" 카드 1장 또는 환룡족 몬스터 1장을 상대에게 보여주고 발동할 수 있다.\r\n자신 필드에 "상검 토큰"(환룡족 / 튜너 / 물 / 레벨 4 / 공 0 / 수 0) 1장을 특수 소환한다.\r\n이 효과로 특수 소환한 토큰이 존재하는 한, 자신은 싱크로 몬스터밖에 엑스트라 덱에서 특수 소환할 수 없다.\r\n②: 이 카드가 싱크로 소재로서 묘지로 보내졌을 경우에 발동할 수 있다.\r\n자신은 덱에서 1장 드로우한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 막야(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/20001443.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='환룡족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 일반 소환 / 특수 소환에 성공했을 경우, 패의 "상검" 카드 1장 또는 환룡족 몬스터 1장을 상대에게 보여주고 발동할 수 있다.\r\n자신 필드에 "상검 토큰"(환룡족 / 튜너 / 물 / 레벨 4 / 공 0 / 수 0) 1장을 특수 소환한다.\r\n이 효과로 특수 소환한 토큰이 존재하는 한, 자신은 싱크로 몬스터밖에 엑스트라 덱에서 특수 소환할 수 없다.\r\n②: 이 카드가 싱크로 소재로서 묘지로 보내졌을 경우에 발동할 수 있다.\r\n자신은 덱에서 1장 드로우한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 상검사태아(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/56495147.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='환룡족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 묘지에서 "상검" 카드 1장 또는 환룡족 몬스터 1장을 제외하고 발동할 수 있다. 자신 필드에 "상검 토큰"(환룡족 / 튜너 / 물 / 레벨 4 / 공 0 / 수 0) 1장을 특수 소환한다. 이 효과로 특수 소환한 토큰이 존재하는 한, 자신은 싱크로 몬스터밖에 엑스트라 덱에서 특수 소환할 수 없다.\r\n②: 이 카드가 싱크로 소재로서 묘지로 보내졌을 경우에 발동할 수 있다. 덱에서 "상검" 카드 1장 또는 환룡족 몬스터 1장을 묘지로 보낸다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()



@bot.command()
async def 태아(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/56495147.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='환룡족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 묘지에서 "상검" 카드 1장 또는 환룡족 몬스터 1장을 제외하고 발동할 수 있다. 자신 필드에 "상검 토큰"(환룡족 / 튜너 / 물 / 레벨 4 / 공 0 / 수 0) 1장을 특수 소환한다. 이 효과로 특수 소환한 토큰이 존재하는 한, 자신은 싱크로 몬스터밖에 엑스트라 덱에서 특수 소환할 수 없다.\r\n②: 이 카드가 싱크로 소재로서 묘지로 보내졌을 경우에 발동할 수 있다. 덱에서 "상검" 카드 1장 또는 환룡족 몬스터 1장을 묘지로 보낸다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 상검서수순균(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/29884951.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='환룡족 / 효과', value='이 카드명의 ①③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 / 상대의 메인 페이즈에, 자신 필드의 몬스터 1장을 릴리스하고 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 자신의 환룡족 몬스터가, 엑스트라 덱에서 특수 소환된 상대 몬스터와 전투를 실행하는 데미지 계산 전에 발동할 수 있다. 그 상대 몬스터와 이 카드를 파괴한다.\r\n③: 이 카드가 싱크로 소재로서 묘지로 보내졌을 경우, 자신 또는 상대의, 필드 / 묘지의 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 제외한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 요안의상검사(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/62849088.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='마법사족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 효과가 무효화되어 있는 몬스터가 필드에 존재할 경우, 자신 / 상대의 메인 페이즈에 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 상대가 몬스터를 특수 소환했을 경우, 그 몬스터를 어디에서 특수 소환했는지에 따라 이하의 효과에서 1개를 선택하여 발동할 수 있다.\r\n●패: 패에서 몬스터 1장을 특수 소환한다.\r\n●덱: 자신은 덱에서 2장 드로우한다.\r\n●엑스트라 덱: 엑스트라 덱에서 특수 소환된 그 몬스터 1장을 고르고 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 요안(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/62849088.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='마법사족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 효과가 무효화되어 있는 몬스터가 필드에 존재할 경우, 자신 / 상대의 메인 페이즈에 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 상대가 몬스터를 특수 소환했을 경우, 그 몬스터를 어디에서 특수 소환했는지에 따라 이하의 효과에서 1개를 선택하여 발동할 수 있다.\r\n●패: 패에서 몬스터 1장을 특수 소환한다.\r\n●덱: 자신은 덱에서 2장 드로우한다.\r\n●엑스트라 덱: 엑스트라 덱에서 특수 소환된 그 몬스터 1장을 고르고 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 심연의상검룡(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/5141117.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='환룡족 / 특수 소환 / 효과', value='이 카드는 통상 소환할 수 없으며, 환룡족 몬스터의 효과로만 특수 소환할 수 있다.\r\n이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 패 / 묘지에 존재하고, 카드의 효과로 몬스터가 제외되었을 경우에 발동할 수 있다. 이 카드를 특수 소환한다. 이 효과로 특수 소환한 이 카드는, 필드에서 벗어났을 경우에 제외된다.\r\n②: 이 카드가 특수 소환에 성공했을 경우, 필드 존의 카드 1장과 상대의 필드 / 묘지의 몬스터 1장를 대상으로 하고 발동할 수 있다. 그 카드를 제외한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 상검대사적소(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/69248256.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='환룡족 / 싱크로 / 효과\r\n튜너 ＋ 튜너 이외의 환룡족 몬스터 1장 이상', value='이 카드명의 ①②의 효과는 1턴에 1번, 어느 쪽이든 1개밖에 사용할 수 없다.\r\n①: 이 카드가 싱크로 소환에 성공했을 경우에 발동할 수 있다. 덱에서 "상검" 카드 1장을 패에 넣거나 제외한다.\r\n②: 자신의 패 / 묘지에서 "상검" 카드 1장 또는 환룡족 몬스터 1장을 제외하고, 이 카드 이외의 필드의 효과 몬스터 1장을 대상으로 하여 발동할 수 있다. 그 몬스터의 효과를 턴 종료시까지 무효로 한다. 이 효과는 상대 턴에도 발동할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 적소(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/69248256.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='환룡족 / 싱크로 / 효과\r\n튜너 ＋ 튜너 이외의 환룡족 몬스터 1장 이상', value='이 카드명의 ①②의 효과는 1턴에 1번, 어느 쪽이든 1개밖에 사용할 수 없다.\r\n①: 이 카드가 싱크로 소환에 성공했을 경우에 발동할 수 있다. 덱에서 "상검" 카드 1장을 패에 넣거나 제외한다.\r\n②: 자신의 패 / 묘지에서 "상검" 카드 1장 또는 환룡족 몬스터 1장을 제외하고, 이 카드 이외의 필드의 효과 몬스터 1장을 대상으로 하여 발동할 수 있다. 그 몬스터의 효과를 턴 종료시까지 무효로 한다. 이 효과는 상대 턴에도 발동할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 상검대공승영(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/96633955.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='환룡족 / 싱크로 / 효과\r\n튜너 ＋ 튜너 이외의 몬스터 1장 이상', value='이 카드명의 ③의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 제외되어 있는 카드의 수 × 100만큼, 이 카드의 공격력 / 수비력은 올리고, 상대 필드의 몬스터의 공격력 / 수비력은 내린다.\r\n②: 이 카드가 효과로 파괴될 경우, 대신에 자신 묘지의 카드 1장을 제외할 수 있다.\r\n③: 카드가 제외되었을 경우에 발동할 수 있다. 상대의 필드 및 묘지의 카드를 각각 1장씩 고르고 제외한다.', inline=True)
    embed.set_footer(text='그 거대한 체구와 검은, 영봉을 계속 지켜냈다는 무엇보다 확실한 증거이다.')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 승영(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/96633955.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='환룡족 / 싱크로 / 효과\r\n튜너 ＋ 튜너 이외의 몬스터 1장 이상', value='이 카드명의 ③의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 제외되어 있는 카드의 수 × 100만큼, 이 카드의 공격력 / 수비력은 올리고, 상대 필드의 몬스터의 공격력 / 수비력은 내린다.\r\n②: 이 카드가 효과로 파괴될 경우, 대신에 자신 묘지의 카드 1장을 제외할 수 있다.\r\n③: 카드가 제외되었을 경우에 발동할 수 있다. 상대의 필드 및 묘지의 카드를 각각 1장씩 고르고 제외한다.', inline=True)
    embed.set_footer(text='그 거대한 체구와 검은, 영봉을 계속 지켜냈다는 무엇보다 확실한 증거이다.')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 용상검현(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/56465981.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 덱에서 "상검" 몬스터 1장을 패에 넣는다. 자신 필드에 싱크로 몬스터가 존재할 경우, 대신에 환룡족 몬스터 1장을 패에 넣을 수도 있다.\r\n②: 이 카드가 제외되었을 경우, 자신 필드의, "상검" 몬스터 또는 환룡족 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터의 레벨을 턴 종료시까지 1개 올리거나, 또는 내린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 대령봉상검문(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/93850690.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 묘지의 "상검" 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터를 특수 소환한다. 자신 필드에 싱크로 몬스터가 존재할 경우, 대신에 환룡족 몬스터 1장을 대상으로 할 수도 있다.\r\n②: 이 카드가 제외되었을 경우, 자신 필드의, "상검" 몬스터 또는 환룡족 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터의 레벨을 턴 종료시까지 1개 올리거나, 또는 내린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 혁성의상검(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://i.ibb.co/mzK3Q3p/20230319213107.png', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드에 싱크로 몬스터가 존재할 경우, 자신 또는 상대의, 필드 / 묘지의 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 제외한다.\r\n②: 상대 필드에 의식 / 융합 / 싱크로 / 엑시즈 / 링크 몬스터 중 어느 하나가 존재할 경우, 자신 묘지에서 싱크로 몬스터 1장을 제외하고 발동할 수 있다. 묘지의 이 카드를 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 서상검구(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/78836195.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다. 자신 묘지에서 "상검" 카드 또는 환룡족 몬스터를 5장까지 제외하고, 대상 몬스터의 공격력은 제외한 수 × 300 올린다.\r\n②: 이 카드가 제외되었을 경우에 발동할 수 있다. 자신 필드에 "상검 토큰"(환룡족 / 튜너 / 물 / 레벨 4 / 공 0 / 수 0) 1장을 특수 소환한다. 이 효과로 특수 소환한 토큰이 존재하는 한, 자신은 싱크로 몬스터밖에 엑스트라 덱에서 특수 소환할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 상검암전(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/14821890.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드의 환룡족 몬스터 1장과 상대 필드의 카드 2장을 대상으로 하고 발동할 수 있다. 그 카드를 파괴한다.\r\n②: 이 카드가 제외되었을 경우에 발동할 수 있다. 자신 필드에 "상검 토큰"(환룡족 / 튜너 / 물 / 레벨 4 / 공 0 / 수 0) 1장을 특수 소환한다. 이 효과로 특수 소환한 토큰이 존재하는 한, 자신은 싱크로 몬스터밖에 엑스트라 덱에서 특수 소환할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 암전(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/14821890.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드의 환룡족 몬스터 1장과 상대 필드의 카드 2장을 대상으로 하고 발동할 수 있다. 그 카드를 파괴한다.\r\n②: 이 카드가 제외되었을 경우에 발동할 수 있다. 자신 필드에 "상검 토큰"(환룡족 / 튜너 / 물 / 레벨 4 / 공 0 / 수 0) 1장을 특수 소환한다. 이 효과로 특수 소환한 토큰이 존재하는 한, 자신은 싱크로 몬스터밖에 엑스트라 덱에서 특수 소환할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 억념의상검(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/99137266.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 지속', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 카드가 제외되었을 경우에 발동할 수 있다. 자신의 패 / 덱 / 묘지 및 자신 / 상대 필드의 앞면 표시의 카드 중에서, 환룡족 싱크로 몬스터 1장 또는 "상검" 카드 1장을 고르고 제외한다.\r\n②: 이 카드가 제외되었을 경우에 발동할 수 있다. 자신 필드에 "상검 토큰"(환룡족 / 튜너 / 물 / 레벨 4 / 공 0 / 수 0) 1장을 특수 소환한다. 이 효과로 특수 소환한 토큰이 존재하는 한, 자신은 싱크로 몬스터밖에 엑스트라 덱에서 특수 소환할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 순백의성녀에클레시아(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://i.postimg.cc/TYyykVFG/chrome-9-Xzi-VOp-Yfk.png', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='마법사족 / 튜너 / 효과', value='이 카드명의, ①의 방법에 의한 특수 소환은 1턴에 1번밖에 할 수 없으며, ②③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 상대 필드의 몬스터의 수가 자신 필드의 몬스터보다 많을 경우, 이 카드는 패에서 특수 소환할 수 있다.\r\n②: 자신 / 상대의 메인 페이즈에, 이 카드를 릴리스하고 발동할 수 있다. 패 / 덱에서 "상검" 몬스터 또는 "알버스의 낙윤" 1장을 특수 소환한다.\r\n③: 이 턴에 융합 몬스터가 자신 묘지로 보내지고 있을 경우, 엔드 페이즈에 발동할 수 있다. 묘지의 이 카드를 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 순백(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://i.postimg.cc/TYyykVFG/chrome-9-Xzi-VOp-Yfk.png', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='마법사족 / 튜너 / 효과', value='이 카드명의, ①의 방법에 의한 특수 소환은 1턴에 1번밖에 할 수 없으며, ②③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 상대 필드의 몬스터의 수가 자신 필드의 몬스터보다 많을 경우, 이 카드는 패에서 특수 소환할 수 있다.\r\n②: 자신 / 상대의 메인 페이즈에, 이 카드를 릴리스하고 발동할 수 있다. 패 / 덱에서 "상검" 몬스터 또는 "알버스의 낙윤" 1장을 특수 소환한다.\r\n③: 이 턴에 융합 몬스터가 자신 묘지로 보내지고 있을 경우, 엔드 페이즈에 발동할 수 있다. 묘지의 이 카드를 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 빙검룡미라제이드(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/44146295.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x71368A)
    embed.add_field(name='환룡족 / 융합 / 효과\r\n"알버스의 낙윤" ＋ 융합 / 싱크로 / 엑시즈 / 링크 몬스터', value='①: "빙검룡 미라제이드"는 자신 필드에 1장밖에 앞면 표시로 존재할 수 없다.\r\n②: 자신 / 상대 턴에 1번, "알버스의 낙윤"을 융합 소재로 하는 융합 몬스터 1장을 엑스트라 덱에서 묘지로 보내고 발동할 수 있다. 필드의 몬스터 1장을 고르고 제외한다. 다음 턴에, 이 카드는 이 효과를 사용할 수 없다.\r\n③: 융합 소환한 이 카드가 상대에 의해 필드에서 벗어났을 경우에 발동할 수 있다. 이 턴의 엔드 페이즈에 상대 필드의 몬스터를 전부 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 빙검룡(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/44146295.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x71368A)
    embed.add_field(name='환룡족 / 융합 / 효과\r\n"알버스의 낙윤" ＋ 융합 / 싱크로 / 엑시즈 / 링크 몬스터', value='①: "빙검룡 미라제이드"는 자신 필드에 1장밖에 앞면 표시로 존재할 수 없다.\r\n②: 자신 / 상대 턴에 1번, "알버스의 낙윤"을 융합 소재로 하는 융합 몬스터 1장을 엑스트라 덱에서 묘지로 보내고 발동할 수 있다. 필드의 몬스터 1장을 고르고 제외한다. 다음 턴에, 이 카드는 이 효과를 사용할 수 없다.\r\n③: 융합 소환한 이 카드가 상대에 의해 필드에서 벗어났을 경우에 발동할 수 있다. 이 턴의 엔드 페이즈에 상대 필드의 몬스터를 전부 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 미라제이드(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/44146295.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x71368A)
    embed.add_field(name='환룡족 / 융합 / 효과\r\n"알버스의 낙윤" ＋ 융합 / 싱크로 / 엑시즈 / 링크 몬스터', value='①: "빙검룡 미라제이드"는 자신 필드에 1장밖에 앞면 표시로 존재할 수 없다.\r\n②: 자신 / 상대 턴에 1번, "알버스의 낙윤"을 융합 소재로 하는 융합 몬스터 1장을 엑스트라 덱에서 묘지로 보내고 발동할 수 있다. 필드의 몬스터 1장을 고르고 제외한다. 다음 턴에, 이 카드는 이 효과를 사용할 수 없다.\r\n③: 융합 소환한 이 카드가 상대에 의해 필드에서 벗어났을 경우에 발동할 수 있다. 이 턴의 엔드 페이즈에 상대 필드의 몬스터를 전부 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 데스피아안루루와릴리스(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/53971455.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='마법사족 / 싱크로 / 효과\r\n레벨 4 튜너 ＋ 튜너 이외의 몬스터 1장 이상', value='이 카드명의 ②의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 1턴에 1번, 자신 / 상대의 카드가 엑스트라 덱에서 벗어났을 경우에 발동할 수 있다. 자신 필드의 모든 몬스터의 공격력은 500 올린다. 그 후, 필드의 앞면 표시의 카드 1장을 고르고 그 효과를 턴 종료시까지 무효로 할 수 있다.\r\n②: 이 카드가 묘지로 보내진 턴의 엔드 페이즈에 발동할 수 있다. 패 / 덱에서 공격력과 수비력의 수치가 같은 마법사족 / 빛 속성 몬스터 1장을 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 루루와릴리스(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/53971455.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='마법사족 / 싱크로 / 효과\r\n레벨 4 튜너 ＋ 튜너 이외의 몬스터 1장 이상', value='이 카드명의 ②의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 1턴에 1번, 자신 / 상대의 카드가 엑스트라 덱에서 벗어났을 경우에 발동할 수 있다. 자신 필드의 모든 몬스터의 공격력은 500 올린다. 그 후, 필드의 앞면 표시의 카드 1장을 고르고 그 효과를 턴 종료시까지 무효로 할 수 있다.\r\n②: 이 카드가 묘지로 보내진 턴의 엔드 페이즈에 발동할 수 있다. 패 / 덱에서 공격력과 수비력의 수치가 같은 마법사족 / 빛 속성 몬스터 1장을 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()








#루닉
@bot.command()
async def 루닉(ctx):
    embed = discord.Embed(title='등록된 루닉 카드 검색 키워드입니다.',
                          colour=0x71368A)
    embed.set_thumbnail(url='https://i.ibb.co/1bBC5CR/20230322222206.png')
    embed.add_field(name='아래와 같습니다.', value='루닉의날개후긴\r\n후긴\r\n루닉의날개무닌\r\n루닉의이빨게리\r\n루닉의이빨프레키\r\n루닉의샘\r\n루닉의날끝\r\n빛나는화염의루닉\r\n파괴의루닉\r\n해주의루닉\r\n얼어붙은저주의루닉\r\n졸음의루닉\r\n황금물방울의루닉\r\n성난폭풍의루닉', inline=True)
    embed.set_footer(text='세계의 신비에 「루닉」으로 도전하라!!')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5 * 2)
    await ctx.message.delete()

@bot.command()
async def 루닉의날개후긴(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/55990317.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x71368A)
    embed.add_field(name='천사족 / 융합 / 효과\r\n"루닉" 몬스터 × 2', value='①: 이 카드가 엑스트라 덱에서의 특수 소환에 성공했을 경우, 패를 1장 버리고 발동할 수 있다. 덱에서 "루닉" 필드 마법 카드 1장을 패에 넣는다.\r\n②: 이 카드 이외의 자신 필드의 카드가 효과로 파괴될 경우, 대신에 필드의 이 카드를 제외할 수 있다.\r\n③: 필드의 이 카드가 전투 / 효과로 파괴되었을 경우에 발동한다. 이 카드를 주인의 엑스트라 덱으로 되돌린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 후긴(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/55990317.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x71368A)
    embed.add_field(name='천사족 / 융합 / 효과\r\n"루닉" 몬스터 × 2', value='①: 이 카드가 엑스트라 덱에서의 특수 소환에 성공했을 경우, 패를 1장 버리고 발동할 수 있다. 덱에서 "루닉" 필드 마법 카드 1장을 패에 넣는다.\r\n②: 이 카드 이외의 자신 필드의 카드가 효과로 파괴될 경우, 대신에 필드의 이 카드를 제외할 수 있다.\r\n③: 필드의 이 카드가 전투 / 효과로 파괴되었을 경우에 발동한다. 이 카드를 주인의 엑스트라 덱으로 되돌린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 루닉의날개무긴(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/92385016.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x71368A)
    embed.add_field(name='천사족 / 융합 / 효과\r\n"루닉" 몬스터 × 2', value='①: 이 카드가 엑스트라 덱에서의 특수 소환에 성공했을 경우, 패를 1장 버리고 발동할 수 있다. 덱에서 "루닉" 지속 마법 카드 1장을 패에 넣는다.\r\n②: 자신 필드의, "루닉" 카드 또는 세트된 카드를 대상으로 하는 마법 / 함정 / 몬스터의 효과를 상대가 발동했을 때, 필드의 이 카드를 제외하고 발동할 수 있다. 그 발동을 무효로 하고 파괴한다.\r\n③: 자신 / 상대의 엔드 페이즈에 발동한다. 자신은 1000 LP 회복한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 무긴(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/92385016.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x71368A)
    embed.add_field(name='천사족 / 융합 / 효과\r\n"루닉" 몬스터 × 2', value='①: 이 카드가 엑스트라 덱에서의 특수 소환에 성공했을 경우, 패를 1장 버리고 발동할 수 있다. 덱에서 "루닉" 지속 마법 카드 1장을 패에 넣는다.\r\n②: 자신 필드의, "루닉" 카드 또는 세트된 카드를 대상으로 하는 마법 / 함정 / 몬스터의 효과를 상대가 발동했을 때, 필드의 이 카드를 제외하고 발동할 수 있다. 그 발동을 무효로 하고 파괴한다.\r\n③: 자신 / 상대의 엔드 페이즈에 발동한다. 자신은 1000 LP 회복한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 루닉의이빨게리(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/28373620.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x71368A)
    embed.add_field(name='야수족 / 융합 / 효과\r\n"루닉" 몬스터 × 2', value='①: 이 카드가 엑스트라 덱에서의 특수 소환에 성공했을 경우, 속공 마법 카드 이외의 자신 묘지의 "루닉" 마법 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 패에 넣는다.\r\n②: 필드의 이 카드는 효과로는 파괴되지 않는다.\r\n③: 이 카드가 전투로 파괴되었을 때, 필드의 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 루닉의이빨프레키(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/47219274.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x71368A)
    embed.add_field(name='야수족 / 융합 / 효과\r\n"루닉" 몬스터 × 2', value='이 카드명의 ③의 효과는 1턴에 1번밖에 사용할 수 없다\r\n①: 엑스트라 몬스터 존의 이 카드가 전투를 실행하는 공격 선언시에 발동할 수 있다. 상대의 덱 위에서 카드를 2장 제외한다.\r\n②: 이 카드의 전투로 발생하는 서로의 전투 데미지는 0이 된다.\r\n③: 필드의 이 카드가 전투 / 효과로 파괴되었을 경우, 자신의 묘지의 "루닉" 속공 마법 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 루닉의샘(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/9210760 * 54.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 필드', value='①: 이 카드가 필드 존에 존재하는 한, 자신은 상대 턴에 "루닉" 속공 마법 카드를 패에서 발동할 수 있다.\r\n②: 1턴에 1번, 자신이 "루닉" 속공 마법 카드를 발동했을 경우, 자신 묘지의 "루닉" 속공 마법 카드를 3장까지 대상으로 하고 발동할 수 있다. 그 카드를 좋아하는 순서대로 덱 아래로 되돌린다. 그 후, 되돌린 수만큼 자신은 덱에서 드로우한다.', inline=True)
    embed.set_footer(text='불길하게 빛나는 붉은 눈을 가진 마신상이 있는 샘, 지금까지의 여정을 되돌아보고, 잠시 쉬어가고 싶은 당신에게.')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 루닉의속임수(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/29595202.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 지속', value='①: "루닉의 속임수"는 자신 필드에 1장밖에 앞면 표시로 존재할 수 없다.\r\n②: 자신 또는 상대가 속공 마법 카드를 발동할 때마다 발동한다. 상대의 덱 위에서 카드를 1장 제외한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 루닉의날끝(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/31562086.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 속공', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 이하의 효과에서 1개를 선택하고 발동할 수 있다. 이 카드의 발동 후, 다음 자신 배틀 페이즈를 스킵한다.\r\n●덱에서 "루닉의 날끝" 이외의 "루닉" 카드 1장을 패에 넣는다. 그 후, 상대의 덱 위에서 카드를 1장 제외한다.\r\n●엑스트라 덱에서 "루닉" 몬스터 1장을 엑스트라 몬스터 존에 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 빛나는화염의루닉(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/68957034.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 속공', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 이하의 효과에서 1개를 선택하고 발동할 수 있다. 이 카드의 발동 후, 다음 자신 배틀 페이즈를 스킵한다.\r\n●특수 소환된 상대 필드의 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터를 파괴한다. 그 후, 상대의 덱 위에서 카드를 2장 제외한다.\r\n●엑스트라 덱에서 "루닉" 몬스터 1장을 엑스트라 몬스터 존에 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 파괴의루닉(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/94445733.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 속공', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 이하의 효과에서 1개를 선택하고 발동할 수 있다. 이 카드의 발동 후, 다음 자신 배틀 페이즈를 스킵한다.\r\n●상대 필드의 마법 / 함정 카드 1장을 대상으로 하고 발동할 수 있다. 그 카드를 파괴한다. 그 후, 상대의 덱 위에서 카드를 4장 제외한다.\r\n●엑스트라 덱에서 "루닉" 몬스터 1장을 엑스트라 몬스터 존에 특수 소환한다.', inline=True)
    await ctx.send('마스터듀얼 한정 준제한', delete_after=60 * 5)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 해주의루닉(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/66712905.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 속공', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 이하의 효과에서 1개를 선택하고 발동할 수 있다. 이 카드의 발동 후, 다음 자신 배틀 페이즈를 스킵한다.\r\n●상대가 드로우 페이즈 이외로 덱에서 카드를 패에 넣었을 경우에 발동할 수 있다. 상대의 패를 무작위로 1장 고르고 버린다. 그 후, 상대의 덱 위에서 카드를 2장 제외한다.\r\n●엑스트라 덱에서 "루닉" 몬스터 1장을 엑스트라 몬스터 존에 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 얼어붙은저주의루닉(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/30430448.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 속공', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 이하의 효과에서 1개를 선택하고 발동할 수 있다. 이 카드의 발동 후, 다음 자신 배틀 페이즈를 스킵한다.\r\n●상대 필드의 효과 몬스터 1장을 대상으로 하고 발동할 수 있다. 그 몬스터의 효과를 턴 종료시까지 무효로 한다. 그 후, 상대의 덱 위에서 카드를 3장 제외한다.\r\n●엑스트라 덱에서 "루닉" 몬스터 1장을 엑스트라 몬스터 존에 특수 소환한다.', inline=True)
    await ctx.send('마스터듀얼 한정 준제한',delete_after=60 * 5)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 졸음의루닉(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/67835547.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 속공', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 이하의 효과에서 1개를 선택하고 발동할 수 있다. 이 카드의 발동 후, 다음 자신 배틀 페이즈를 스킵한다.\r\n●필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다. 이 턴에, 그 몬스터는 1번만 전투 / 효과로는 파괴되지 않으며, 공격할 수 없다. 그 후, 상대의 덱 위에서 카드를 3장 제외한다.\r\n●엑스트라 덱에서 "루닉" 몬스터 1장을 엑스트라 몬스터 존에 특수 소환한다.', inline=True)
    await ctx.send('마스터듀얼 한정 준제한',delete_after=60 * 5)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 황금물방울의루닉(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/20618850.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 속공', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 이하의 효과에서 1개를 선택하고 발동할 수 있다. 이 카드의 발동 후, 다음 자신 배틀 페이즈를 스킵한다.\r\n●상대는 덱에서 1장 드로우한다. 그 후, 상대의 덱 위에서 카드를 4장 제외한다.\r\n●엑스트라 덱에서 "루닉" 몬스터 1장을 엑스트라 몬스터 존에 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 성난폭풍의루닉(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/93229151.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 속공', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 이하의 효과에서 1개를 선택하고 발동할 수 있다. 이 카드의 발동 후, 다음 자신 배틀 페이즈를 스킵한다.\r\n●상대 필드의 카드의 수까지 상대의 덱 위에서 카드를 제외한다.\r\n●엑스트라 덱에서 "루닉" 몬스터 1장을 엑스트라 몬스터 존에 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()






#미캉코
@bot.command()
async def 미캉코(ctx):
    embed = discord.Embed(title='등록된 미캉코 카드 검색 키워드입니다.',
                          colour=0x00AFFF)
    embed.set_thumbnail(url='https://i.postimg.cc/25Y6ydsK/20230623134357.png')
    embed.add_field(name='아래와 같습니다.',value='검의미캉코하레\r\n하레\r\n거울의미캉코니니\r\n니니\r\n구슬의미캉코후우리\r\n후우리\r\n후리\r\n아라히메의미캉코\r\n아라히메\r\n오오히메의미캉코\r\n오오히메\r\n전승의대미캉코\r\n전승\r\n미캉코의화총무\r\n화총무\r\n미캉코의불무\r\n불무\r\n미캉코의유혹하는론도\r\n론도\r\n미캉코의아라베스크\r\n아라베스크\r\n미캉코무용미혹의새\r\n미혹의새\r\n천미캉코의합\r\n천미캉코\r\n미캉코카구라\r\n카구라\r\n미캉코의약속\r\n약속\r\n미캉코카미카쿠시\r\n카미카쿠시\r\n미캉코카미쿠라베\r\n카미쿠라베\r\n쿠라베',inline=True)
    embed.set_footer(text='경쟁하며 갈고 닦은 미캉코 카구라. 무희들의 화려한 무대!')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5 * 2)
    await ctx.message.delete()

@bot.command()
async def 캉코(ctx):
    embed = discord.Embed(title='등록된 미캉코 카드 검색 키워드입니다.',
                          colour=0x00AFFF)
    embed.set_thumbnail(url='https://i.postimg.cc/25Y6ydsK/20230623134357.png')
    embed.add_field(name='아래와 같습니다.',value='검의 미캉코 하레\r\n하레\r\n거울의 미캉코 니니\r\n니니\r\n구슬의 미캉코 후우리\r\n후우리\r\n아라히메의 미캉코\r\n아라히메\r\n오오히메의 미캉코\r\n오오히메\r\n전승의 대미캉코\r\n미캉코의 화총무\r\n화총무\r\n미캉코의 불무\r\n불무\r\n미캉코의 유혹하는 론도\r\n론도\r\n미캉코의 아라베스크\r\n아라베스크\r\n미캉코무용-미혹의 새\r\n미혹의 새\r\n천 미캉코의 합\r\n미캉코 카구라\r\n카구라\r\n미캉코의 약속\r\n미캉코 카미카쿠시\r\n카미카쿠시\r\n미캉코 카미쿠라베\r\n카미쿠라베',inline=True)
    embed.set_footer(text='경쟁하며 갈고 닦은 미캉코 카구라. 무희들의 화려한 무대!')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5 * 2)
    await ctx.message.delete()


@bot.command()
async def 아라히메의미캉코(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/75771170.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x00AFFF)
    embed.add_field(name='천사족 / 의식 / 효과', value='"미캉코 카구라"에 의해 의식 소환.\r\n이 카드명의 ①의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 패 / 묘지에 존재하고, 자신 묘지에 다른 "미캉코" 카드가 존재할 경우, 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n이 카드를 장착 마법 카드로 취급하여 그 몬스터에 장착한다.\r\nㅤ\r\n②: 이 카드가 장착되어있을 경우, 자신 / 상대의 엔드 페이즈에 발동할 수 있다.\r\n이 카드와 장착 몬스터를 패로 되돌린다.\r\nㅤ\r\n③: 이 카드는 전투로는 파괴되지 않으며, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 대신에 상대가 받는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 아라히메(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/75771170.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x00AFFF)
    embed.add_field(name='천사족 / 의식 / 효과', value='"미캉코 카구라"에 의해 의식 소환.\r\n이 카드명의 ①의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 패 / 묘지에 존재하고, 자신 묘지에 다른 "미캉코" 카드가 존재할 경우, 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n이 카드를 장착 마법 카드로 취급하여 그 몬스터에 장착한다.\r\nㅤ\r\n②: 이 카드가 장착되어있을 경우, 자신 / 상대의 엔드 페이즈에 발동할 수 있다.\r\n이 카드와 장착 몬스터를 패로 되돌린다.\r\nㅤ\r\n③: 이 카드는 전투로는 파괴되지 않으며, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 대신에 상대가 받는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 미캉코카미카쿠시(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/53174748.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 상대 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 앞면 표시 몬스터를 자신 필드의 "미캉코" 몬스터 1장에 장착 마법 카드로 취급하고 장착한다.\r\n필드에 의식 몬스터가 존재할 경우, 추가로 자신 필드의 장착 마법 카드의 수 × 500 데미지를 상대에게 줄 수 있다.\r\nㅤ\r\n②: 묘지의 이 카드를 제외하고 발동할 수 있다. 자신의 패 / 제외 상태의 "미캉코" 몬스터 1장을 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 카미카쿠시(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/53174748.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 상대 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 앞면 표시 몬스터를 자신 필드의 "미캉코" 몬스터 1장에 장착 마법 카드로 취급하고 장착한다.\r\n필드에 의식 몬스터가 존재할 경우, 추가로 자신 필드의 장착 마법 카드의 수 × 500 데미지를 상대에게 줄 수 있다.\r\nㅤ\r\n②: 묘지의 이 카드를 제외하고 발동할 수 있다. 자신의 패 / 제외 상태의 "미캉코" 몬스터 1장을 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()
# 여기서부터 시작 10/11
@bot.command()
async def 미캉코카미쿠라베(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/78199891.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드에 "미캉코" 몬스터가 존재할 경우, 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터가 장착 가능한 장착 마법 카드 1장을 덱에서 고르고, 그 몬스터에 장착한다.\r\n②: 이 카드가 묘지에 존재하는 상태에서, 장착 마법 카드가 자신 묘지로 보내졌을 경우, 이 카드를 제외하고, 자신 묘지의 장착 마법 카드 1장을 대상으로 하여 발동할 수 있다.\r\n그 카드를 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 카미쿠라베(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/78199891.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드에 "미캉코" 몬스터가 존재할 경우, 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터가 장착 가능한 장착 마법 카드 1장을 덱에서 고르고, 그 몬스터에 장착한다.\r\n②: 이 카드가 묘지에 존재하는 상태에서, 장착 마법 카드가 자신 묘지로 보내졌을 경우, 이 카드를 제외하고, 자신 묘지의 장착 마법 카드 1장을 대상으로 하여 발동할 수 있다.\r\n그 카드를 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 쿠라베(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/78199891.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드에 "미캉코" 몬스터가 존재할 경우, 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터가 장착 가능한 장착 마법 카드 1장을 덱에서 고르고, 그 몬스터에 장착한다.\r\n②: 이 카드가 묘지에 존재하는 상태에서, 장착 마법 카드가 자신 묘지로 보내졌을 경우, 이 카드를 제외하고, 자신 묘지의 장착 마법 카드 1장을 대상으로 하여 발동할 수 있다.\r\n그 카드를 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 미캉코의약속(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/42705243.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 패 / 덱에서 "미캉코" 몬스터 1장을 특수 소환한다. 그 후, 그 몬스터가 장착 가능한 장착 마법 카드 1장을 자신의 패 / 묘지에서 고르고 그 몬스터에 장착할 수 있다.\r\n이 효과로 특수 소환한 몬스터는, 필드에서 벗어났을 경우에 제외된다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 약속(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/42705243.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 패 / 덱에서 "미캉코" 몬스터 1장을 특수 소환한다. 그 후, 그 몬스터가 장착 가능한 장착 마법 카드 1장을 자신의 패 / 묘지에서 고르고 그 몬스터에 장착할 수 있다.\r\n이 효과로 특수 소환한 몬스터는, 필드에서 벗어났을 경우에 제외된다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 검의미캉코하레(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/18377261.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='전사족 / 효과', value='이 카드명의 ②의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 장착 카드를 장착하고 있지 않을 경우, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 0이 되고,\r\n장착하고 있을 경우, 이 카드는 전투로는 파괴되지 않으며, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 대신에 상대가 받는다.\r\n②: 이 카드에 장착 카드가 장착되었을 경우에 발동할 수 있다.\r\n덱에서 "미캉코" 장착 마법 카드 1장을 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 하레(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/18377261.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='전사족 / 효과', value='이 카드명의 ②의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 장착 카드를 장착하고 있지 않을 경우, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 0이 되고,\r\n장착하고 있을 경우, 이 카드는 전투로는 파괴되지 않으며, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 대신에 상대가 받는다.\r\n②: 이 카드에 장착 카드가 장착되었을 경우에 발동할 수 있다.\r\n덱에서 "미캉코" 장착 마법 카드 1장을 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 거울의미캉코니니(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/54862960 * 5.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='마법사족 / 효과', value='이 카드명의 ②의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 장착 카드를 장착하고 있지 않을 경우, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 0이 되고,\r\n장착하고 있을 경우, 이 카드는 전투로는 파괴되지 않으며, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 대신에 상대가 받는다.\r\n②: 이 카드가 장착 카드를 장착하고 있을 경우, 상대 턴에, 상대 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터의 컨트롤을 엔드 페이즈까지 얻는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 니니(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/54862960 * 5.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='마법사족 / 효과', value='이 카드명의 ②의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 장착 카드를 장착하고 있지 않을 경우, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 0이 되고,\r\n장착하고 있을 경우, 이 카드는 전투로는 파괴되지 않으며, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 대신에 상대가 받는다.\r\n②: 이 카드가 장착 카드를 장착하고 있을 경우, 상대 턴에, 상대 필드의 앞면 표시 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터의 컨트롤을 엔드 페이즈까지 얻는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 구슬의미캉코후우리(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/6327734.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='사이킥족 / 효과', value='이 카드명의 ③의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 장착 카드를 장착하고 있지 않을 경우, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 0 이 되고,\r\n장착하고 있을 경우, 이 카드는 전투로는 파괴되지 않으며, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 대신에 상대가 받는다.\r\n②: 자신 필드에 장착 카드가 존재하는 한, 자신 필드의 "미캉코" 카드는 상대 효과의 대상이 되지 않는다.\r\n③: 이 카드에 장착 카드가 장착되었을 경우에 발동할 수 있다. 덱에서 "미캉코" 함정 카드 1장을 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 후우리(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/6327734.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='사이킥족 / 효과', value='이 카드명의 ③의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 장착 카드를 장착하고 있지 않을 경우, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 0 이 되고,\r\n장착하고 있을 경우, 이 카드는 전투로는 파괴되지 않으며, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 대신에 상대가 받는다.\r\n②: 자신 필드에 장착 카드가 존재하는 한, 자신 필드의 "미캉코" 카드는 상대 효과의 대상이 되지 않는다.\r\n③: 이 카드에 장착 카드가 장착되었을 경우에 발동할 수 있다. 덱에서 "미캉코" 함정 카드 1장을 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 후리(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/6327734.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='사이킥족 / 효과', value='이 카드명의 ③의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 장착 카드를 장착하고 있지 않을 경우, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 0 이 되고,\r\n장착하고 있을 경우, 이 카드는 전투로는 파괴되지 않으며, 이 카드의 전투로 발생하는 자신에게로의 전투 데미지는 대신에 상대가 받는다.\r\n②: 자신 필드에 장착 카드가 존재하는 한, 자신 필드의 "미캉코" 카드는 상대 효과의 대상이 되지 않는다.\r\n③: 이 카드에 장착 카드가 장착되었을 경우에 발동할 수 있다. 덱에서 "미캉코" 함정 카드 1장을 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 전승의대미캉코(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/44649322.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 속공', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 패에서 "미캉코" 몬스터 1장을 소환 조건을 무시하고 특수 소환한다.\r\n이 효과로 특수 소환한 몬스터는 상대 엔드 페이즈에 주인의 패로 되돌아간다.\r\n②: 자신 메인 페이즈에 묘지의 이 카드를 제외하고 발동할 수 있다.\r\n덱에서 "전승의 대미캉코" 이외의 "미캉코" 카드 1장을 묘지로 보낸다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 전승(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/44649322.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 속공', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 패에서 "미캉코" 몬스터 1장을 소환 조건을 무시하고 특수 소환한다.\r\n이 효과로 특수 소환한 몬스터는 상대 엔드 페이즈에 주인의 패로 되돌아간다.\r\n②: 자신 메인 페이즈에 묘지의 이 카드를 제외하고 발동할 수 있다.\r\n덱에서 "전승의 대미캉코" 이외의 "미캉코" 카드 1장을 묘지로 보낸다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 미캉코의화총무(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/80044027.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 장착', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 자신의 패 / 묘지에서 "미캉코" 몬스터 1장을 골라 특수 소환하고, 이 카드를 장착한다.\r\n그 후, 상대 묘지에서 몬스터 1장을 골라 효과를 무효로 하고 상대 필드에 특수 소환할 수 있다.\r\n②: 장착 몬스터는 효과로는 파괴되지 않는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 화총무(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/80044027.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 장착', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 자신의 패 / 묘지에서 "미캉코" 몬스터 1장을 골라 특수 소환하고, 이 카드를 장착한다.\r\n그 후, 상대 묘지에서 몬스터 1장을 골라 효과를 무효로 하고 상대 필드에 특수 소환할 수 있다.\r\n②: 장착 몬스터는 효과로는 파괴되지 않는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 미캉코의불무(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/16433136.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 장착', value='"미캉코" 몬스터에만 장착 가능. 이 카드명의 ②의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 장착 몬스터는 효과로는 파괴되지 않는다.\r\n②: 상대 필드에 몬스터가 특수 소환되었을 경우, 자신 및 상대 필드의 몬스터를 1장씩 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 주인의 패로 되돌린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 불무(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/16433136.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 장착', value='"미캉코" 몬스터에만 장착 가능. 이 카드명의 ②의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 장착 몬스터는 효과로는 파괴되지 않는다.\r\n②: 상대 필드에 몬스터가 특수 소환되었을 경우, 자신 및 상대 필드의 몬스터를 1장씩 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 주인의 패로 되돌린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 미캉코의아라베스크(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/43527730.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 장착', value='이 카드명의 ②의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 장착 몬스터는 효과로는 파괴되지 않는다.\r\n②: 자신 메인 페이즈에 발동할 수 있다. 장착 몬스터와는 원래의 카드명이 다른 "미캉코" 몬스터 1장을 패 / 덱에서 특수 소환하고,\r\n이 카드를 그 몬스터에 장착한다.\r\n그 후, 이 카드를 장착하고 있던 몬스터를 주인의 패로 되돌린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 아라베스크(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/43527730.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 장착', value='이 카드명의 ②의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 장착 몬스터는 효과로는 파괴되지 않는다.\r\n②: 자신 메인 페이즈에 발동할 수 있다. 장착 몬스터와는 원래의 카드명이 다른 "미캉코" 몬스터 1장을 패 / 덱에서 특수 소환하고,\r\n이 카드를 그 몬스터에 장착한다.\r\n그 후, 이 카드를 장착하고 있던 몬스터를 주인의 패로 되돌린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 미캉코의유혹하는론도(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/79912449.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 장착', value='상대 필드의 몬스터에 장착할 수 있다. 이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: "미캉코의 유혹하는 론도"는 자신 필드에 1장밖에 앞면 표시로 존재할 수 있다.\r\n②: 자신 필드에 "미캉코" 몬스터가 존재하는 한, 장착 몬스터의 컨트롤을 얻는다.\r\n③: 장착 몬스터는 자신 필드에 존재하는 한, 효과를 발동할 수 없다.\r\n④: 이 카드가 필드에서 벗어났을 때에 장착 몬스터는 묘지로 보내진다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 론도(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/79912449.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 장착', value='상대 필드의 몬스터에 장착할 수 있다. 이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: "미캉코의 유혹하는 론도"는 자신 필드에 1장밖에 앞면 표시로 존재할 수 있다.\r\n②: 자신 필드에 "미캉코" 몬스터가 존재하는 한, 장착 몬스터의 컨트롤을 얻는다.\r\n③: 장착 몬스터는 자신 필드에 존재하는 한, 효과를 발동할 수 없다.\r\n④: 이 카드가 필드에서 벗어났을 때에 장착 몬스터는 묘지로 보내진다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 미캉코무용미혹의새(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/57736667.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 장착', value='이 카드명의 ②③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 장착 몬스터는 효과로는 파괴되지 않는다.\r\n②: 자신의 "미캉코" 몬스터가 전투를 실행한 데미지 스텝 종료시, 필드의 카드 1장을 대상으로 하고 발동할 수 있다.\r\n그 카드를 주인의 패로 되돌린다.\r\n③: 이 카드가 묘지에 존재할 경우, 자신 묘지의 "미캉코" 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 특수 소환하고, 이 카드를 그 몬스터에 장착한다. 이 효과로 특수 소환한 몬스터는, 필드에서 벗어났을 경우에 제외된다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 미혹의새(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/57736667.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 장착', value='이 카드명의 ②③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 장착 몬스터는 효과로는 파괴되지 않는다.\r\n②: 자신의 "미캉코" 몬스터가 전투를 실행한 데미지 스텝 종료시, 필드의 카드 1장을 대상으로 하고 발동할 수 있다.\r\n그 카드를 주인의 패로 되돌린다.\r\n③: 이 카드가 묘지에 존재할 경우, 자신 묘지의 "미캉코" 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 특수 소환하고, 이 카드를 그 몬스터에 장착한다. 이 효과로 특수 소환한 몬스터는, 필드에서 벗어났을 경우에 제외된다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 천미캉코의합(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/17255673.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 필드', value='①: 장착 카드를 장착한 몬스터가 자신 필드에 존재하는 한, 공격 가능한 상대 몬스터는 장착 카드를 장착한 몬스터를 공격해야 한다.\r\n②: 자신의 "미캉코" 몬스터가 전투를 실행할 경우, 상대는 데미지 스텝 종료시까지 마법 / 함정 / 몬스터의 효과를 발동할 수 없다.\r\n③: 자신의 "미캉코" 몬스터가 전투를 실행한 데미지 스텝 종료시, 자신 필드의 장착 카드 1장을 묘지로 보내고 발동할 수 있다.\r\n그 몬스터는 1번 더 이어서 몬스터에 공격할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 천미캉코(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/17255673.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 필드', value='①: 장착 카드를 장착한 몬스터가 자신 필드에 존재하는 한, 공격 가능한 상대 몬스터는 장착 카드를 장착한 몬스터를 공격해야 한다.\r\n②: 자신의 "미캉코" 몬스터가 전투를 실행할 경우, 상대는 데미지 스텝 종료시까지 마법 / 함정 / 몬스터의 효과를 발동할 수 없다.\r\n③: 자신의 "미캉코" 몬스터가 전투를 실행한 데미지 스텝 종료시, 자신 필드의 장착 카드 1장을 묘지로 보내고 발동할 수 있다.\r\n그 몬스터는 1번 더 이어서 몬스터에 공격할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 미캉코카구라(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/16310544.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 의식', value='"미캉코" 의식 몬스터의 의식 소환에 필요. 이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 레벨의 합계가 의식 소환할 몬스터의 레벨 이상이 되도록, 자신의 패 / 필드의 몬스터를 릴리스하고, 패에서 "미캉코" 의식 몬스터 1장을 의식 소환한다.\r\n그 후, 이하의 효과를 적용할 수 있다.\r\n●자신 묘지의 장착 마법 카드의 종류의 수까지 상대 필드의 카드를 골라 파괴하고, 파괴한 수 × 1000 데미지를 상대에게 준다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 카구라(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/16310544.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법카드 / 의식', value='"미캉코" 의식 몬스터의 의식 소환에 필요. 이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 레벨의 합계가 의식 소환할 몬스터의 레벨 이상이 되도록, 자신의 패 / 필드의 몬스터를 릴리스하고, 패에서 "미캉코" 의식 몬스터 1장을 의식 소환한다.\r\n그 후, 이하의 효과를 적용할 수 있다.\r\n●자신 묘지의 장착 마법 카드의 종류의 수까지 상대 필드의 카드를 골라 파괴하고, 파괴한 수 × 1000 데미지를 상대에게 준다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()



#TG
@bot.command()
async def TG(ctx):
    embed = discord.Embed(title='등록된 테크지너스 카드 검색 키워드입니다.',colour=0xEEEFF1)
    embed.set_thumbnail(url='https://i.postimg.cc/qMs0YvN9/chrome-h9o-RRvqk-TB.jpg')
    embed.add_field(name='아래와 같습니다.', value='TG사이버매지션\r\n사이버매지션\r\nTG탱크러바\r\n탱크러바\r\nTG기어좀비\r\n기어좀비\r\nTG스트라이커\r\nTG제트팔콘\r\n제트팔콘\r\nTG스크류서펜트\r\n스크류서펜트\r\nTG부스터랩토르\r\n부스터랩토르\r\nTG드릴피시\r\n드릴피시\r\nTG로캣샐러맨더\r\n로켓샐러맨더\r\nTG중장갑드래곤\r\n중장갑드래곤\r\nTG메탈스켈리턴\r\n메탈스켈리턴\r\n스켈리턴\r\nTG워울프\r\n워울프\r\nTG러시라이노\r\n러시라이노\r\nTG할버드캐논버스터\r\n할버드캐논버스터\r\nTG레시프로드래곤플라이\r\n레시프로\r\n레시프로드래곤\r\n레시프로플라이\r\n레시프로드래곤플라이\r\n드래곤플라이\r\nTG마이티스트라이커\r\n마이티스트라이커\r\nTG파워글래디에이터\r\n파워글래디에이터\r\nTG하이퍼라이브러리언\r\n하이퍼라이브러리언\r\n라이브러리언\r\nTG원더매지션\r\n원더매지션\r\nTG스타가디언\r\n스타가디언\r\nTG오버드래그너\r\n오버드래그너\r\nTG블레이드건맨\r\n블레이드건맨\r\n슈팅스타드래곤TGEX\r\nTG할버드캐논\r\n할버드캐논\r\nTG글레이브블래스터\r\n글레이브블래스터\r\nTG트라이든트런처\r\n트라이든트\r\nTG브레이크리미터\r\n브레이크리미터\r\nTG올클리어\r\n올클리어\TG클로즈\r\n클로즈\r\nTGX1HL\r\nTGX300\r\nTG1EM1\r\nTGSX1\r\nTGX3DX2\r\n배틀스턴소닉\r\n배틀스턴', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5 * 2)
    await ctx.message.delete()


@bot.command()
async def 테크지너스(ctx):
    embed = discord.Embed(title='등록된 테크지너스 카드 검색 키워드입니다.',colour=0xEEEFF1)
    embed.set_thumbnail(url='https://i.postimg.cc/qMs0YvN9/chrome-h9o-RRvqk-TB.jpg')
    embed.add_field(name='아래와 같습니다.', value='TG사이버매지션\r\n사이버매지션\r\nTG탱크러바\r\n탱크러바\r\nTG기어좀비\r\n기어좀비\r\nTG스트라이커\r\nTG제트팔콘\r\n제트팔콘\r\nTG스크류서펜트\r\n스크류서펜트\r\nTG부스터랩토르\r\n부스터랩토르\r\nTG드릴피시\r\n드릴피시\r\nTG로캣샐러맨더\r\n로켓샐러맨더\r\nTG중장갑드래곤\r\n중장갑드래곤\r\nTG메탈스켈리턴\r\n메탈스켈리턴\r\n스켈리턴\r\nTG워울프\r\n워울프\r\nTG러시라이노\r\n러시라이노\r\nTG할버드캐논버스터\r\n할버드캐논버스터\r\nTG레시프로드래곤플라이\r\n레시프로\r\n레시프로드래곤\r\n레시프로플라이\r\n레시프로드래곤플라이\r\n드래곤플라이\r\nTG마이티스트라이커\r\n마이티스트라이커\r\nTG파워글래디에이터\r\n파워글래디에이터\r\nTG하이퍼라이브러리언\r\n하이퍼라이브러리언\r\n라이브러리언\r\nTG원더매지션\r\n원더매지션\r\nTG스타가디언\r\n스타가디언\r\nTG오버드래그너\r\n오버드래그너\r\nTG블레이드건맨\r\n블레이드건맨\r\n슈팅스타드래곤TGEX\r\nTG할버드캐논\r\n할버드캐논\r\nTG글레이브블래스터\r\n글레이브블래스터\r\nTG트라이든트런처\r\n트라이든트\r\nTG브레이크리미터\r\n브레이크리미터\r\nTG올클리어\r\n올클리어\TG클로즈\r\n클로즈\r\nTGX1HL\r\nTGX300\r\nTG1EM1\r\nTGSX1\r\nTGX3DX2\r\n배틀스턴소닉\r\n배틀스턴', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5 * 2)
    await ctx.message.delete()


@bot.command()
async def 티지(ctx):
    embed = discord.Embed(title='등록된 테크지너스 카드 검색 키워드입니다.',colour=0xEEEFF1)
    embed.set_thumbnail(url='https://i.postimg.cc/qMs0YvN9/chrome-h9o-RRvqk-TB.jpg')
    embed.add_field(name='아래와 같습니다.',value='TG사이버매지션\r\n사이버매지션\r\nTG탱크러바\r\n탱크러바\r\nTG기어좀비\r\n기어좀비\r\nTG스트라이커\r\nTG제트팔콘\r\n제트팔콘\r\nTG스크류서펜트\r\n스크류서펜트\r\nTG부스터랩토르\r\n부스터랩토르\r\nTG드릴피시\r\n드릴피시\r\nTG로캣샐러맨더\r\n로켓샐러맨더\r\nTG중장갑드래곤\r\n중장갑드래곤\r\nTG메탈스켈리턴\r\n메탈스켈리턴\r\n스켈리턴\r\nTG워울프\r\n워울프\r\nTG러시라이노\r\n러시라이노\r\nTG할버드캐논버스터\r\n할버드캐논버스터\r\nTG레시프로드래곤플라이\r\n레시프로\r\n레시프로드래곤\r\n레시프로플라이\r\n레시프로드래곤플라이\r\n드래곤플라이\r\nTG마이티스트라이커\r\n마이티스트라이커\r\nTG파워글래디에이터\r\n파워글래디에이터\r\nTG하이퍼라이브러리언\r\n하이퍼라이브러리언\r\n라이브러리언\r\nTG원더매지션\r\n원더매지션\r\nTG스타가디언\r\n스타가디언\r\nTG오버드래그너\r\n오버드래그너\r\nTG블레이드건맨\r\n블레이드건맨\r\n슈팅스타드래곤TGEX\r\nTG할버드캐논\r\n할버드캐논\r\nTG글레이브블래스터\r\n글레이브블래스터\r\nTG트라이든트런처\r\n트라이든트\r\nTG브레이크리미터\r\n브레이크리미터\r\nTG올클리어\r\n올클리어\TG클로즈\r\n클로즈\r\nTGX1HL\r\nTGX300\r\nTG1EM1\r\nTGSX1\r\nTGX3DX2\r\n배틀스턴소닉\r\n배틀스턴',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5 * 2)
    await ctx.message.delete()


@bot.command()
async def 티쥐(ctx):
    embed = discord.Embed(title='등록된 테크지너스 카드 검색 키워드입니다.',colour=0xEEEFF1)
    embed.set_thumbnail(url='https://i.postimg.cc/qMs0YvN9/chrome-h9o-RRvqk-TB.jpg')
    embed.add_field(name='아래와 같습니다.',value='TG사이버매지션\r\n사이버매지션\r\nTG탱크러바\r\n탱크러바\r\nTG기어좀비\r\n기어좀비\r\nTG스트라이커\r\nTG제트팔콘\r\n제트팔콘\r\nTG스크류서펜트\r\n스크류서펜트\r\nTG부스터랩토르\r\n부스터랩토르\r\nTG드릴피시\r\n드릴피시\r\nTG로캣샐러맨더\r\n로켓샐러맨더\r\nTG중장갑드래곤\r\n중장갑드래곤\r\nTG메탈스켈리턴\r\n메탈스켈리턴\r\n스켈리턴\r\nTG워울프\r\n워울프\r\nTG러시라이노\r\n러시라이노\r\nTG할버드캐논버스터\r\n할버드캐논버스터\r\nTG레시프로드래곤플라이\r\n레시프로\r\n레시프로드래곤\r\n레시프로플라이\r\n레시프로드래곤플라이\r\n드래곤플라이\r\nTG마이티스트라이커\r\n마이티스트라이커\r\nTG파워글래디에이터\r\n파워글래디에이터\r\nTG하이퍼라이브러리언\r\n하이퍼라이브러리언\r\n라이브러리언\r\nTG원더매지션\r\n원더매지션\r\nTG스타가디언\r\n스타가디언\r\nTG오버드래그너\r\n오버드래그너\r\nTG블레이드건맨\r\n블레이드건맨\r\n슈팅스타드래곤TGEX\r\nTG할버드캐논\r\n할버드캐논\r\nTG글레이브블래스터\r\n글레이브블래스터\r\nTG트라이든트런처\r\n트라이든트\r\nTG브레이크리미터\r\n브레이크리미터\r\nTG올클리어\r\n올클리어\TG클로즈\r\n클로즈\r\nTGX1HL\r\nTGX300\r\nTG1EM1\r\nTGSX1\r\nTGX3DX2\r\n배틀스턴소닉\r\n배틀스턴',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5 * 2)
    await ctx.message.delete()

@bot.command()
async def tg(ctx):
    embed = discord.Embed(title='등록된 테크지너스 카드 검색 키워드입니다.',colour=0xEEEFF1)
    embed.set_thumbnail(url='https://i.postimg.cc/qMs0YvN9/chrome-h9o-RRvqk-TB.jpg')
    embed.add_field(name='아래와 같습니다.',value='TG사이버매지션\r\n사이버매지션\r\nTG탱크러바\r\n탱크러바\r\nTG기어좀비\r\n기어좀비\r\nTG스트라이커\r\nTG제트팔콘\r\n제트팔콘\r\nTG스크류서펜트\r\n스크류서펜트\r\nTG부스터랩토르\r\n부스터랩토르\r\nTG드릴피시\r\n드릴피시\r\nTG로캣샐러맨더\r\n로켓샐러맨더\r\nTG중장갑드래곤\r\n중장갑드래곤\r\nTG메탈스켈리턴\r\n메탈스켈리턴\r\n스켈리턴\r\nTG워울프\r\n워울프\r\nTG러시라이노\r\n러시라이노\r\nTG할버드캐논버스터\r\n할버드캐논버스터\r\nTG레시프로드래곤플라이\r\n레시프로\r\n레시프로드래곤\r\n레시프로플라이\r\n레시프로드래곤플라이\r\n드래곤플라이\r\nTG마이티스트라이커\r\n마이티스트라이커\r\nTG파워글래디에이터\r\n파워글래디에이터\r\nTG하이퍼라이브러리언\r\n하이퍼라이브러리언\r\n라이브러리언\r\nTG원더매지션\r\n원더매지션\r\nTG스타가디언\r\n스타가디언\r\nTG오버드래그너\r\n오버드래그너\r\nTG블레이드건맨\r\n블레이드건맨\r\n슈팅스타드래곤TGEX\r\nTG할버드캐논\r\n할버드캐논\r\nTG글레이브블래스터\r\n글레이브블래스터\r\nTG트라이든트런처\r\n트라이든트\r\nTG브레이크리미터\r\n브레이크리미터\r\nTG올클리어\r\n올클리어\TG클로즈\r\n클로즈\r\nTGX1HL\r\nTGX300\r\nTG1EM1\r\nTGSX1\r\nTGX3DX2\r\n배틀스턴소닉\r\n배틀스턴',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5 * 2)
    await ctx.message.delete()

@bot.command()
async def TG사이버매지션(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/64910482.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='마법사족 / 튜너 / 효과',value='자신 필드의 이 카드를 소재로서 "TG(테크지너스)" 싱크로 몬스터를 싱크로 소환할 경우, 패의 튜너 이외의 "TG(테크지너스)" 몬스터도 싱크로 소재로 할 수 있다.\r\n①: 필드의 이 카드가 파괴되어 묘지로 보내진 턴의 엔드 페이즈에 발동할 수 있다. 덱에서 "TG(테크지너스) 사이버 매지션" 이외의 "TG(테크지너스)" 몬스터 1장을 패에 넣는다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 사이버매지션(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/64910482.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='마법사족 / 튜너 / 효과',value='자신 필드의 이 카드를 소재로서 "TG(테크지너스)" 싱크로 몬스터를 싱크로 소환할 경우, 패의 튜너 이외의 "TG(테크지너스)" 몬스터도 싱크로 소재로 할 수 있다.\r\n①: 필드의 이 카드가 파괴되어 묘지로 보내진 턴의 엔드 페이즈에 발동할 수 있다. 덱에서 "TG(테크지너스) 사이버 매지션" 이외의 "TG(테크지너스)" 몬스터 1장을 패에 넣는다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()


@bot.command()
async def TG탱크러바(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/74627016.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='곤충족 / 튜너 / 효과', value='이 카드명의 ②의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드의 이 카드를 "TG(테크지너스)" 싱크로 몬스터의 싱크로 소재로 할 경우, 이 카드를 튜너 이외의 몬스터로서 취급할 수 있다.\r\n②: 이 카드가 "TG(테크지너스)" 싱크로 몬스터의 싱크로 소재로서 묘지로 보내졌을 경우에 발동할 수 있다. 자신 필드에 "TG(테크지너스) 토큰"(기계족 / 땅 / 레벨 1 / 공 0 / 수 0) 1장을 공격 표시로 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


@bot.command()
async def 탱크러바(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/74627016.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='곤충족 / 튜너 / 효과',value='이 카드명의 ②의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드의 이 카드를 "TG(테크지너스)" 싱크로 몬스터의 싱크로 소재로 할 경우, 이 카드를 튜너 이외의 몬스터로서 취급할 수 있다.\r\n②: 이 카드가 "TG(테크지너스)" 싱크로 몬스터의 싱크로 소재로서 묘지로 보내졌을 경우에 발동할 수 있다. 자신 필드에 "TG(테크지너스) 토큰"(기계족 / 땅 / 레벨 1 / 공 0 / 수 0) 1장을 공격 표시로 특수 소환한다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG기어좀비(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/94350039.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='언데드족 / 튜너 / 효과', value='이 카드명의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드의 "TG(테크지너스)" 몬스터 1장을 대상으로 하고 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n그 후, 대상 몬스터의 공격력을 1000 내린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 기어좀비(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/94350039.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='언데드족 / 튜너 / 효과',value='이 카드명의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드의 "TG(테크지너스)" 몬스터 1장을 대상으로 하고 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n그 후, 대상 몬스터의 공격력을 1000 내린다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG스트라이커(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/1315120.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='전사족 / 튜너 / 효과', value='①: 상대 필드에만 몬스터가 존재할 경우, 이 카드는 패에서 특수 소환할 수 있다.\r\n②: 필드의 이 카드가 파괴되어 묘지로 보내진 턴의 엔드 페이즈에 발동할 수 있다.\r\n자신의 덱에서 "TG(테크지너스) 스트라이커" 이외의 "TG(테크지너스)" 몬스터 1장을 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG제트팔콘(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/37300735.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='비행야수족 / 튜너 / 효과', value='이 카드가 싱크로 소환의 소재로서 묘지로 보내졌을 경우, 상대 라이프에 500 포인트 데미지를 준다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG스크류서펜트(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/11234702.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name=' 해룡족 / 튜너 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 일반 소환 / 특수 소환에 성공했을 경우, "TG(테크지너스) 스크류 서펜트" 이외의 자신 묘지의 레벨 4 이하의 "TG(테크지너스)" 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 효과를 무효로 하고 특수 소환한다.\r\n②: 묘지의 이 카드를 제외하고, 자신 필드의 "TG(테크지너스)" 몬스터 1장을 대상으로 하여 발동할 수 있다.\r\n그 몬스터의 레벨을 턴 종료시까지 1개 올리거나, 또는 내린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 스크류서펜트(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/11234702.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name=' 해룡족 / 튜너 / 효과',value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 일반 소환 / 특수 소환에 성공했을 경우, "TG(테크지너스) 스크류 서펜트" 이외의 자신 묘지의 레벨 4 이하의 "TG(테크지너스)" 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 효과를 무효로 하고 특수 소환한다.\r\n②: 묘지의 이 카드를 제외하고, 자신 필드의 "TG(테크지너스)" 몬스터 1장을 대상으로 하여 발동할 수 있다.\r\n그 몬스터의 레벨을 턴 종료시까지 1개 올리거나, 또는 내린다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG부스터랩토르(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/48633301.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='공룡족 / 효과', value='이 카드명의 ①의 방법에 의한 특수 소환은 1턴에 1번밖에 할 수 없다.\r\n①: 자신 필드에 "TG(테크지너스)" 몬스터가 존재할 경우, 이 카드는 패에서 특수 소환할 수 있다.\r\n②: 필드의 이 카드가 파괴되어 묘지로 보내진 턴의 엔드 페이즈에 발동할 수 있다.\r\n덱에서 "TG(테크지너스) 부스터 랩토르" 이외의 "TG(테크지너스)" 몬스터 1장을 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 부스터랩토르(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/48633301.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='공룡족 / 효과',value='이 카드명의 ①의 방법에 의한 특수 소환은 1턴에 1번밖에 할 수 없다.\r\n①: 자신 필드에 "TG(테크지너스)" 몬스터가 존재할 경우, 이 카드는 패에서 특수 소환할 수 있다.\r\n②: 필드의 이 카드가 파괴되어 묘지로 보내진 턴의 엔드 페이즈에 발동할 수 있다.\r\n덱에서 "TG(테크지너스) 부스터 랩토르" 이외의 "TG(테크지너스)" 몬스터 1장을 패에 넣는다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG드릴피시(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/30348744.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='어류족 / 효과', value='이 카드명의 ①③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드의 몬스터가 "TG(테크지너스)" 몬스터뿐일 경우에 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 이 카드는 직접 공격할 수 있다.\r\n③: 자신의 "TG(테크지너스)" 몬스터가 상대에게 전투 데미지를 주었을 때, 상대 필드의 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 드릴피시(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/30348744.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='어류족 / 효과',value='이 카드명의 ①③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드의 몬스터가 "TG(테크지너스)" 몬스터뿐일 경우에 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 이 카드는 직접 공격할 수 있다.\r\n③: 자신의 "TG(테크지너스)" 몬스터가 상대에게 전투 데미지를 주었을 때, 상대 필드의 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 파괴한다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG로켓샐러맨더(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/77392987.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='화염족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드의 "TG(테크지너스)" 몬스터 1장을 릴리스하고 발동할 수 있다.\r\n릴리스한 몬스터와는 원래 카드명이 다른 "TG(테크지너스)" 몬스터 1장을 덱에서 특수 소환한다.\r\n②: 자신 필드에 기계족인 "TG(테크지너스)" 몬스터가 존재할 경우, 자신 묘지의 레벨 4 이하의 "TG(테크지너스)" 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 수비 표시로 특수 소환한다. 이 효과로 특수 소환한 몬스터의 효과는 무효화된다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 로켓샐러맨더(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/77392987.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='화염족 / 효과',value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 자신 필드의 "TG(테크지너스)" 몬스터 1장을 릴리스하고 발동할 수 있다.\r\n릴리스한 몬스터와는 원래 카드명이 다른 "TG(테크지너스)" 몬스터 1장을 덱에서 특수 소환한다.\r\n②: 자신 필드에 기계족인 "TG(테크지너스)" 몬스터가 존재할 경우, 자신 묘지의 레벨 4 이하의 "TG(테크지너스)" 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 수비 표시로 특수 소환한다. 이 효과로 특수 소환한 몬스터의 효과는 무효화된다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG중장갑드래곤(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/64898834.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='드래곤족 / 효과', value='1턴에 1번, 패에서 레벨 3 이하의 "TG(테크지너스)"라는 이름이 붙은 튜너 1장을 특수 소환할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 중장갑드래곤(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/64898834.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='드래곤족 / 효과', value='1턴에 1번, 패에서 레벨 3 이하의 "TG(테크지너스)"라는 이름이 붙은 튜너 1장을 특수 소환할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG메탈스켈리턴(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/66733743.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='언데드족 / 효과', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 필드의 몬스터가 전투 또는 상대 효과로 파괴되었을 경우에 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 자신 필드의 "TG(테크지너스)" 몬스터가 전투 / 효과로 파괴될 경우, 대신에 필드 / 묘지의 이 카드를 제외할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 메탈스캘리턴(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/66733743.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='언데드족 / 효과',value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 필드의 몬스터가 전투 또는 상대 효과로 파괴되었을 경우에 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 자신 필드의 "TG(테크지너스)" 몬스터가 전투 / 효과로 파괴될 경우, 대신에 필드 / 묘지의 이 카드를 제외할 수 있다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG워울프(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/293542.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='야수전사족 / 효과', value='①: 자신 또는 상대가 레벨 4 이하 몬스터의 특수 소환에 성공했을 때에 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 필드의 이 카드가 파괴되어 묘지로 보내진 턴의 엔드 페이즈에 발동할 수 있다.\r\n덱에서 "TG(테크지너스) 워울프" 이외의 "TG(테크지너스)" 몬스터 1장을 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 워울프(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/293542.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='야수전사족 / 효과',value='①: 자신 또는 상대가 레벨 4 이하 몬스터의 특수 소환에 성공했을 때에 발동할 수 있다. 이 카드를 패에서 특수 소환한다.\r\n②: 필드의 이 카드가 파괴되어 묘지로 보내진 턴의 엔드 페이즈에 발동할 수 있다.\r\n덱에서 "TG(테크지너스) 워울프" 이외의 "TG(테크지너스)" 몬스터 1장을 패에 넣는다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG러시라이노(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/36687247.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='야수족 / 효과', value='①: 이 카드가 공격할 경우, 데미지 스텝 동안 이 카드의 공격력은 400 올린다.\r\n②: 필드의 이 카드가 파괴되어 묘지로 보내진 턴의 엔드 페이즈에 발동할 수 있다.\r\n덱에서 "TG(테크지너스) 러시 라이노" 이외의 "TG(테크지너스)" 몬스터 1장을 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 러시라이노(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/36687247.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='야수족 / 효과',value='①: 이 카드가 공격할 경우, 데미지 스텝 동안 이 카드의 공격력은 400 올린다.\r\n②: 필드의 이 카드가 파괴되어 묘지로 보내진 턴의 엔드 페이즈에 발동할 수 있다.\r\n덱에서 "TG(테크지너스) 러시 라이노" 이외의 "TG(테크지너스)" 몬스터 1장을 패에 넣는다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()


@bot.command()
async def TG할버드캐논버스터(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/47027714.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='기계족 / 특수 소환 / 효과', value='이 카드는 통상 소환할 수 없다. "버스터 모드"의 효과로만 특수 소환할 수 있다. 이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 상대가 몬스터를 일반 소환 / 반전 소환 / 특수 소환할 시기에 발동할 수 있다.\r\n그것을 무효로 하고, 그 몬스터 및 상대 필드의 특수 소환된 몬스터를 전부 제외한다.\r\n②: 필드의 이 카드가 파괴되었을 때, 자신 묘지의 "TG(테크지너스) 할 버드 캐논" 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 소환 조건을 무시하고 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 할버드캐논버스터(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/47027714.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xC27C0E)
    embed.add_field(name='기계족 / 특수 소환 / 효과',value='이 카드는 통상 소환할 수 없다. "버스터 모드"의 효과로만 특수 소환할 수 있다. 이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 상대가 몬스터를 일반 소환 / 반전 소환 / 특수 소환할 시기에 발동할 수 있다.\r\n그것을 무효로 하고, 그 몬스터 및 상대 필드의 특수 소환된 몬스터를 전부 제외한다.\r\n②: 필드의 이 카드가 파괴되었을 때, 자신 묘지의 "TG(테크지너스) 할 버드 캐논" 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 소환 조건을 무시하고 특수 소환한다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()


@bot.command()
async def TG레시프로드래곤플라이(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/62560 * 5742.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='곤충족 / 싱크로 / 효과\r\n튜너 ＋ 튜너 이외의 몬스터 1장', value='①: 1턴에 1번, 이 카드 이외의 자신 필드의 "TG(테크지너스)" 싱크로 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 묘지로 보낸다. 그 후, 묘지로 보낸 그 몬스터의 싱크로 소환에 사용한 싱크로 소재 몬스터 1세트가, 모두 싱크로 몬스터이고 자신 묘지에 모여 있으면,\r\n그 1세트를 자신 필드에 특수 소환할 수 있다.', inline=True)
    embed.set_footer(text="리미터 해제 레벨 2! 레귤레이터 오픈! 내비게이션, 올 클리어! GO! 싱크로 소환! Come on! TG 레시프로 드래곤 플라이!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 레시프로드래곤플라이(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/62560 * 5742.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='곤충족 / 싱크로 / 효과\r\n튜너 ＋ 튜너 이외의 몬스터 1장',value='①: 1턴에 1번, 이 카드 이외의 자신 필드의 "TG(테크지너스)" 싱크로 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 묘지로 보낸다. 그 후, 묘지로 보낸 그 몬스터의 싱크로 소환에 사용한 싱크로 소재 몬스터 1세트가, 모두 싱크로 몬스터이고 자신 묘지에 모여 있으면,\r\n그 1세트를 자신 필드에 특수 소환할 수 있다.',inline=True)
    embed.set_footer(text="리미터 해제 레벨 2! 레귤레이터 오픈! 내비게이션, 올 클리어! GO! 싱크로 소환! Come on! TG 레시프로 드래곤 플라이!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 드래곤플라이(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/62560 * 5742.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='곤충족 / 싱크로 / 효과\r\n튜너 ＋ 튜너 이외의 몬스터 1장',value='①: 1턴에 1번, 이 카드 이외의 자신 필드의 "TG(테크지너스)" 싱크로 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 묘지로 보낸다. 그 후, 묘지로 보낸 그 몬스터의 싱크로 소환에 사용한 싱크로 소재 몬스터 1세트가, 모두 싱크로 몬스터이고 자신 묘지에 모여 있으면,\r\n그 1세트를 자신 필드에 특수 소환할 수 있다.',inline=True)
    embed.set_footer(text="리미터 해제 레벨 2! 레귤레이터 오픈! 내비게이션, 올 클리어! GO! 싱크로 소환! Come on! TG 레시프로 드래곤 플라이!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 레시프로드래곤(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/62560 * 5742.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='곤충족 / 싱크로 / 효과\r\n튜너 ＋ 튜너 이외의 몬스터 1장',value='①: 1턴에 1번, 이 카드 이외의 자신 필드의 "TG(테크지너스)" 싱크로 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 묘지로 보낸다. 그 후, 묘지로 보낸 그 몬스터의 싱크로 소환에 사용한 싱크로 소재 몬스터 1세트가, 모두 싱크로 몬스터이고 자신 묘지에 모여 있으면,\r\n그 1세트를 자신 필드에 특수 소환할 수 있다.',inline=True)
    embed.set_footer(text="리미터 해제 레벨 2! 레귤레이터 오픈! 내비게이션, 올 클리어! GO! 싱크로 소환! Come on! TG 레시프로 드래곤 플라이!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG마이티스트라이커(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/32480825.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='전사족 / 싱크로 / 튜너 / 효과\r\n튜너 ＋ 튜너 이외의 몬스터 1장', value='이 카드명의 ①③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드를 싱크로 소환했을 경우에 발동할 수 있다. 덱에서 "TG(테크지너스)" 마법 / 함정 카드 1장을 패에 넣는다.\r\n②: 상대 메인 페이즈에 1번, 발동할 수 있다. 이 카드를 포함하는 자신 필드의 몬스터를 소재로서 싱크로 소환을 실행한다.\r\n③: 이 카드가 몬스터 존에서 묘지로 보내졌을 경우에 발동할 수 있다. 덱에서 "TG(테크지너스)" 카드 1장을 묘지로 보낸다.', inline=True)
    embed.set_footer(text="리미터 해제 레벨 2! 부스터 주입 120%! 업스트림 컨트롤, All Clear! GO! 싱크로 소환! Come on! TG 마이티 스트라이커!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 마이티스트라이커(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/32480825.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='전사족 / 싱크로 / 튜너 / 효과\r\n튜너 ＋ 튜너 이외의 몬스터 1장',value='이 카드명의 ①③의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드를 싱크로 소환했을 경우에 발동할 수 있다. 덱에서 "TG(테크지너스)" 마법 / 함정 카드 1장을 패에 넣는다.\r\n②: 상대 메인 페이즈에 1번, 발동할 수 있다. 이 카드를 포함하는 자신 필드의 몬스터를 소재로서 싱크로 소환을 실행한다.\r\n③: 이 카드가 몬스터 존에서 묘지로 보내졌을 경우에 발동할 수 있다. 덱에서 "TG(테크지너스)" 카드 1장을 묘지로 보낸다.',inline=True)
    embed.set_footer(text="리미터 해제 레벨 2! 부스터 주입 120%! 업스트림 컨트롤, All Clear! GO! 싱크로 소환! Come on! TG 마이티 스트라이커!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG파워글래디에이터(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/24943456.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='전사족 / 싱크로 / 효과\r\n튜너 ＋ 튜너 이외의 "TG(테크지너스)"라는 이름이 붙은 몬스터 1장 이상', value='이 카드가 수비 표시 몬스터를 공격했을 때, 그 수비력을 공격력이 넘었으면, 그 수치만큼 상대 라이프에 전투 데미지를 준다.\r\n필드 위에 존재하는 이 카드가 파괴되었을 때, 자신의 덱에서 카드를 1장 드로우한다.', inline=True)
    embed.set_footer(text="싱크로 플라이트 컨트롤! 리미터 해제 레벨 5! 부스터 주입 120%! 리커버리 네트워크 레인지 수정! 올 클리어! GO! 싱크로 소환! Come on! TG-파워 글래디에이터!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 파워글래디에이터(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/24943456.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='전사족 / 싱크로 / 효과\r\n튜너 ＋ 튜너 이외의 "TG(테크지너스)"라는 이름이 붙은 몬스터 1장 이상',value='이 카드가 수비 표시 몬스터를 공격했을 때, 그 수비력을 공격력이 넘었으면, 그 수치만큼 상대 라이프에 전투 데미지를 준다.\r\n필드 위에 존재하는 이 카드가 파괴되었을 때, 자신의 덱에서 카드를 1장 드로우한다.',inline=True)
    embed.set_footer(text="싱크로 플라이트 컨트롤! 리미터 해제 레벨 5! 부스터 주입 120%! 리커버리 네트워크 레인지 수정! 올 클리어! GO! 싱크로 소환! Come on! TG-파워 글래디에이터!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG하이퍼라이브러리언(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/90953320.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='마법사족 / 싱크로 / 효과\r\n튜너 ＋ 튜너 이외의 몬스터 1장 이상', value='①: 이 카드가 필드에 존재하고, 자신 또는 상대가, 이 카드 이외의 싱크로 몬스터의 싱크로 소환에 성공했을 경우에 발동한다.\r\n이 카드가 필드에 앞면 표시로 존재할 경우, 자신은 덱에서 1장 드로우한다.', inline=True)
    embed.set_footer(text="리미터 해제, 레벨 5! 레귤레이터 오픈, 스러스터 웜 업, OK! 업 링크, All Clear! GO! 싱크로 소환! Come on! TG 하이퍼 라이브러리언!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 하이퍼라이브러리언(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/90953320.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='마법사족 / 싱크로 / 효과\r\n튜너 ＋ 튜너 이외의 몬스터 1장 이상',value='①: 이 카드가 필드에 존재하고, 자신 또는 상대가, 이 카드 이외의 싱크로 몬스터의 싱크로 소환에 성공했을 경우에 발동한다.\r\n이 카드가 필드에 앞면 표시로 존재할 경우, 자신은 덱에서 1장 드로우한다.',inline=True)
    embed.set_footer(text="리미터 해제, 레벨 5! 레귤레이터 오픈, 스러스터 웜 업, OK! 업 링크, All Clear! GO! 싱크로 소환! Come on! TG 하이퍼 라이브러리언!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 라이브러리언(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/90953320.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='마법사족 / 싱크로 / 효과\r\n튜너 ＋ 튜너 이외의 몬스터 1장 이상',value='①: 이 카드가 필드에 존재하고, 자신 또는 상대가, 이 카드 이외의 싱크로 몬스터의 싱크로 소환에 성공했을 경우에 발동한다.\r\n이 카드가 필드에 앞면 표시로 존재할 경우, 자신은 덱에서 1장 드로우한다.',inline=True)
    embed.set_footer(text="리미터 해제, 레벨 5! 레귤레이터 오픈, 스러스터 웜 업, OK! 업 링크, All Clear! GO! 싱크로 소환! Come on! TG 하이퍼 라이브러리언!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG원더매지션(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/98558751.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='마법사족 / 싱크로 / 튜너 / 효과\r\n튜너 ＋ 튜너 이외의 "TG(테크지너스)" 몬스터 1장 이상', value='①: 이 카드가 싱크로 소환에 성공했을 경우, 필드의 마법 / 함정 카드 1장을 대상으로 하고 발동한다. 그 카드를 파괴한다.\r\n②: 상대 메인 페이즈에 발동할 수 있다. 이 카드를 포함하는 자신 필드의 몬스터를 소재로서 싱크로 소환한다.\r\n③: 필드의 이 카드가 파괴되었을 경우에 발동한다. 자신은 덱에서 1장 드로우한다.',inline=True)
    embed.set_footer(text="리미터 해제 레벨 5! 부스터 런치 OK, 인클리네이션 OK, 그랜드 서포트, All Clear! GO, 싱크로 소환! Come on! TG 원더 매지션!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 원더매지션(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/98558751.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='마법사족 / 싱크로 / 튜너 / 효과\r\n튜너 ＋ 튜너 이외의 "TG(테크지너스)" 몬스터 1장 이상', value='①: 이 카드가 싱크로 소환에 성공했을 경우, 필드의 마법 / 함정 카드 1장을 대상으로 하고 발동한다. 그 카드를 파괴한다.\r\n②: 상대 메인 페이즈에 발동할 수 있다. 이 카드를 포함하는 자신 필드의 몬스터를 소재로서 싱크로 소환한다.\r\n③: 필드의 이 카드가 파괴되었을 경우에 발동한다. 자신은 덱에서 1장 드로우한다.', inline=True)
    embed.set_footer(text='리미터 해제 레벨 5! 부스터 런치 OK, 인클리네이션 OK, 그랜드 서포트, All Clear! GO, 싱크로 소환! Come on! TG 원더 매지션!')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG스타가디언(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/99937842.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='전사족 / 싱크로 / 튜너 / 효과\r\n튜너 + 튜너 이외의 "TG(테크지너스)" 몬스터 1장 이상', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 특수 소환에 성공했을 경우, 자신 묘지의 "TG(테크지너스)" 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 패에 넣는다.\r\n②: 자신 메인 페이즈에 발동할 수 있다. 패에서 "TG(테크지너스)" 몬스터 1장을 특수 소환한다.\r\n③: 상대 메인 페이즈에 발동할 수 있다. 이 카드를 포함하는 자신 필드의 몬스터를 싱크로 소재로서 싱크로 소환한다.', inline=True)
    embed.set_footer(text='리미터 해제 레벨 5! 레귤레이터 오픈! All Clear! GO! 싱크로 소환! Come on! TG 스타 가디언!')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 스타가디언(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/99937842.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='전사족 / 싱크로 / 튜너 / 효과\r\n튜너 + 튜너 이외의 "TG(테크지너스)" 몬스터 1장 이상', value='이 카드명의 ①②의 효과는 각각 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 특수 소환에 성공했을 경우, 자신 묘지의 "TG(테크지너스)" 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 패에 넣는다.\r\n②: 자신 메인 페이즈에 발동할 수 있다. 패에서 "TG(테크지너스)" 몬스터 1장을 특수 소환한다.\r\n③: 상대 메인 페이즈에 발동할 수 있다. 이 카드를 포함하는 자신 필드의 몬스터를 싱크로 소재로서 싱크로 소환한다.',inline=True)
    embed.set_footer(text='리미터 해제 레벨 5! 레귤레이터 오픈! All Clear! GO! 싱크로 소환! Come on! TG 스타 가디언!')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG오버드래그너(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/68989420.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='드래곤족 / 싱크로 / 효과\r\n튜너 + 튜너 이외의 몬스터 1장 이상', value='①: 이 카드를 싱크로 소환했을 경우에 발동할 수 있다. 자신 묘지에서 "TG(테크지너스)" 몬스터를 임의의 수만큼 수비 표시로 특수 소환한다.\r\n이 효과의 발동 후, 턴 종료시까지 자신은 "TG(테크지너스)" 몬스터밖에 특수 소환할 수 없다.\r\n②: 필드의 이 카드가 파괴되었을 경우에 발동한다. 자신은 1장 드로우한다.', inline=True)
    embed.set_footer(text="리미터 해제 레벨 5! 레귤레이터 오픈! 액셀러레이터, OK! 톱 서포트, All Clear! GO! 싱크로 소환! Come on! TG 오버 드래그너!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 오버드래그너(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/68989420.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='드래곤족 / 싱크로 / 효과\r\n튜너 + 튜너 이외의 몬스터 1장 이상', value='①: 이 카드를 싱크로 소환했을 경우에 발동할 수 있다. 자신 묘지에서 "TG(테크지너스)" 몬스터를 임의의 수만큼 수비 표시로 특수 소환한다.\r\n이 효과의 발동 후, 턴 종료시까지 자신은 "TG(테크지너스)" 몬스터밖에 특수 소환할 수 없다.\r\n②: 필드의 이 카드가 파괴되었을 경우에 발동한다. 자신은 1장 드로우한다.',inline=True)
    embed.set_footer(text="리미터 해제 레벨 5! 레귤레이터 오픈! 액셀러레이터, OK! 톱 서포트, All Clear! GO! 싱크로 소환! Come on! TG 오버 드래그너!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG블레이드건맨(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/51447164.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='기계족 / 싱크로 / 효과\r\n싱크로 몬스터의 튜너 1장 ＋ 튜너 이외의 싱크로 몬스터 1장 이상', value='이 카드를 대상으로 하는 상대의 마법 / 함정 카드가 발동했을 때, 패를 1장 묘지로 보내는 것으로, 그 효과를 무효로 한다.\r\n또한, 상대 턴에 1번, 자신의 묘지에 존재하는 "TG(테크지너스)"라는 이름이 붙은 몬스터 1장을 게임에서 제외하는 것으로,\r\n필드 위에 앞면 표시로 존재하는 이 카드를 게임에서 제외한다.\r\n다음 스텐바이 페이즈시, 이 효과로 제외한 이 카드를 특수 소환한다.', inline=True)
    embed.set_footer(text="리미터 해제, 레벨 10! 메인 베이스 부스터 컨트롤, All Clear! 무한한 힘! 지금 여기에 해방시켜, 차원의 저편으로 돌진하라! GO! 액셀 싱크로! Come on! TG 블레이드 거너!!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 블레이드건맨(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/51447164.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='기계족 / 싱크로 / 효과\r\n싱크로 몬스터의 튜너 1장 ＋ 튜너 이외의 싱크로 몬스터 1장 이상', value='이 카드를 대상으로 하는 상대의 마법 / 함정 카드가 발동했을 때, 패를 1장 묘지로 보내는 것으로, 그 효과를 무효로 한다.\r\n또한, 상대 턴에 1번, 자신의 묘지에 존재하는 "TG(테크지너스)"라는 이름이 붙은 몬스터 1장을 게임에서 제외하는 것으로,\r\n필드 위에 앞면 표시로 존재하는 이 카드를 게임에서 제외한다.\r\n다음 스텐바이 페이즈시, 이 효과로 제외한 이 카드를 특수 소환한다.', inline=True)
    embed.set_footer(text="리미터 해제, 레벨 10! 메인 베이스 부스터 컨트롤, All Clear! 무한한 힘! 지금 여기에 해방시켜, 차원의 저편으로 돌진하라! GO! 액셀 싱크로! Come on! TG 블레이드 거너!!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 슈팅스타드래곤TGEX(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/63180841.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='드래곤족 / 싱크로 / 효과\r\n싱크로 몬스터의 튜너 ＋ 튜너 이외의 싱크로 몬스터 1장 이상', value='①: 자신 필드의 몬스터를 대상으로 하는 몬스터의 효과가 발동했을 때, 자신 묘지에서 튜너 1장을 제외하고 발동할 수 있다.\r\n그 발동을 무효로 하고 파괴한다.\r\n②: 상대 몬스터의 공격 선언시에 발동할 수 있다. 그 공격을 무효로 한다.\r\n③: 상대 턴에, 이 카드가 묘지에 존재할 경우, 자신 필드의 싱크로 몬스터 2장을 릴리스하고 발동할 수 있다. 이 카드를 특수 소환한다.', inline=True)
    embed.set_footer(text="하나된 인연은 우리의 현재와 미래를 잇는다. 시공을 뛰어넘어 한 층 더 진화의 문을 열어라! 액셀 싱크로! 와라! 슈팅 스타 드래곤 TG테크지너스 - EX익스팬션!!!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG할버드캐논(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/97836203.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='기계족 / 싱크로 / 효과\r\n싱크로 몬스터의 튜너 1장 ＋ 튜너 이외의 싱크로 몬스터 2장 이상', value='이 카드는 싱크로 소환으로밖에 특수 소환할 수 없다.\r\n①: 1턴에 1번, 자신 또는 상대가 몬스터를 일반 소환 / 반전 소환 / 특수 소환할 시기에 발동할 수 있다.\r\n이 카드가 필드에 앞면 표시로 존재할 경우, 그것을 무효로 하고, 그 몬스터를 파괴한다.\r\n②: 이 카드가 필드에서 묘지로 보내졌을 때, 자신 묘지의 "TG(테크지너스)" 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 특수 소환한다.', inline=True)
    embed.set_footer(text="리미터 해제 레벨 MAX, 레귤레이터 오픈, All Clear! 무한한 힘이여, 시공을 뛰어넘어 미지의 세계를 열어라! GO! 델타 액셀! COME ON! TG 할 버드 캐논!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 할버드캐논(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/97836203.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='기계족 / 싱크로 / 효과\r\n싱크로 몬스터의 튜너 1장 ＋ 튜너 이외의 싱크로 몬스터 2장 이상',value='이 카드는 싱크로 소환으로밖에 특수 소환할 수 없다.\r\n①: 1턴에 1번, 자신 또는 상대가 몬스터를 일반 소환 / 반전 소환 / 특수 소환할 시기에 발동할 수 있다.\r\n이 카드가 필드에 앞면 표시로 존재할 경우, 그것을 무효로 하고, 그 몬스터를 파괴한다.\r\n②: 이 카드가 필드에서 묘지로 보내졌을 때, 자신 묘지의 "TG(테크지너스)" 몬스터 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 특수 소환한다.',inline=True)
    embed.set_footer(text="리미터 해제 레벨 MAX, 레귤레이터 오픈, All Clear! 무한한 힘이여, 시공을 뛰어넘어 미지의 세계를 열어라! GO! 델타 액셀! COME ON! TG 할 버드 캐논!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG글레이브블래스터(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/95973569.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='기계족 / 싱크로 / 효과\r\n싱크로 몬스터의 튜너 ＋ 튜너 이외의 싱크로 몬스터 2장 이상',value='이 카드는 싱크로 소환으로밖에 특수 소환할 수 없다.\r\n①: 자신 / 상대 턴에, 엑스트라 덱에서 특수 소환된 필드의 몬스터 1장을 대상으로 하고 발동할 수 있다\r\n(이 효과는 1턴 중에, 이 카드의 싱크로 소재로 한 튜너 이외의 싱크로 몬스터의 수까지 사용할 수 있다). 그 몬스터를 제외한다.\r\n②: 1턴에 1번, 몬스터가 앞면으로 제외되었을 경우, 그 중의 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 소환 조건을 무시하고 자신 필드에 특수 소환한다.',inline=True)
    embed.set_footer(text="리미터 해제 레벨 MAX! 레귤레이터 오픈! 내비게이션 ALL CLEAR! 차원을 깨트리는 무한한 힘, 빛을 넘어 미래를 개척해라! GO! 델타 액셀! COME ON! TG 글레이브 블래스터!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 글레이브블래스터(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/95973569.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0xEEEFF1)
    embed.add_field(name='기계족 / 싱크로 / 효과\r\n싱크로 몬스터의 튜너 ＋ 튜너 이외의 싱크로 몬스터 2장 이상', value='이 카드는 싱크로 소환으로밖에 특수 소환할 수 없다.\r\n①: 자신 / 상대 턴에, 엑스트라 덱에서 특수 소환된 필드의 몬스터 1장을 대상으로 하고 발동할 수 있다\r\n(이 효과는 1턴 중에, 이 카드의 싱크로 소재로 한 튜너 이외의 싱크로 몬스터의 수까지 사용할 수 있다). 그 몬스터를 제외한다.\r\n②: 1턴에 1번, 몬스터가 앞면으로 제외되었을 경우, 그 중의 1장을 대상으로 하고 발동할 수 있다.\r\n그 몬스터를 소환 조건을 무시하고 자신 필드에 특수 소환한다.', inline=True)
    embed.set_footer(text="리미터 해제 레벨 MAX! 레귤레이터 오픈! 내비게이션 ALL CLEAR! 차원을 깨트리는 무한한 힘, 빛을 넘어 미래를 개척해라! GO! 델타 액셀! COME ON! TG 글레이브 블래스터!")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG트라이든트런처(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/50750868.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n"TG(테크지너스)" 튜너를 포함하는 효과 몬스터 2장 이상', value='이 카드명의 ①의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 링크 소환에 성공했을 경우에 발동할 수 있다. 자신의 패 / 덱 / 묘지에서 "TG(테크지너스)" 몬스터를 각각 1장씩 고르고, 이 카드의 링크 앞이 되는 자신 필드에 수비 표시로 특수 소환한다.\r\n이 효과의 발동 후, 턴 종료시까지 자신은 "TG(테크지너스)" 몬스터밖에 특수 소환할 수 없다.\r\n②: 상대는 이 카드의 링크 앞의 "TG(테크지너스)" 싱크로 몬스터를 효과의 대상으로 할 수 없다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 트라이든트런처(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/50750868.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='기계족 / 링크 / 효과\r\n"TG(테크지너스)" 튜너를 포함하는 효과 몬스터 2장 이상', value='이 카드명의 ①의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 이 카드가 링크 소환에 성공했을 경우에 발동할 수 있다. 자신의 패 / 덱 / 묘지에서 "TG(테크지너스)" 몬스터를 각각 1장씩 고르고, 이 카드의 링크 앞이 되는 자신 필드에 수비 표시로 특수 소환한다.\r\n이 효과의 발동 후, 턴 종료시까지 자신은 "TG(테크지너스)" 몬스터밖에 특수 소환할 수 없다.\r\n②: 상대는 이 카드의 링크 앞의 "TG(테크지너스)" 싱크로 몬스터를 효과의 대상으로 할 수 없다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG브레이크리미터(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/28189908.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반', value='이 카드명의 ①②의 효과는 1턴에 1번, 어느 쪽이든 1개밖에 사용할 수 없다.\r\n①: 패를 1장 버리고 발동할 수 있다. 덱에서 "TG(테크지너스)" 몬스터 2장을 패에 넣는다(같은 이름의 카드는 1장까지).\r\n②: 묘지의 이 카드를 제외하고, 자신 묘지의 "TG(테크지너스)" 몬스터 1장을 대상으로 하여 발동할 수 있다. 그 몬스터를 덱으로 되돌린다.\r\n자신 필드에 기계족인 "TG(테크지너스)" 몬스터가 존재할 경우, 덱으로 되돌리지 않고 패에 넣을 수도 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 브레이크리미터(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/28189908.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 일반',value='이 카드명의 ①②의 효과는 1턴에 1번, 어느 쪽이든 1개밖에 사용할 수 없다.\r\n①: 패를 1장 버리고 발동할 수 있다. 덱에서 "TG(테크지너스)" 몬스터 2장을 패에 넣는다(같은 이름의 카드는 1장까지).\r\n②: 묘지의 이 카드를 제외하고, 자신 묘지의 "TG(테크지너스)" 몬스터 1장을 대상으로 하여 발동할 수 있다. 그 몬스터를 덱으로 되돌린다.\r\n자신 필드에 기계족인 "TG(테크지너스)" 몬스터가 존재할 경우, 덱으로 되돌리지 않고 패에 넣을 수도 있다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG올클리어(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/54573517.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 지속', value='이 카드명의 ③의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 필드의 "TG(테크지너스)" 몬스터는 기계족이 된다.\r\n②: 자신은 통상 소환 외에도 1번만, 자신 메인 페이즈에 "TG(테크지너스)" 몬스터 1장을 일반 소환할 수 있다.\r\n③: 자신 메인 페이즈에 발동할 수 있다. 자신의 패 / 필드의 "TG(테크지너스)" 몬스터 1장을 파괴하고,\r\n그 몬스터와는 카드명이 다른 "TG(테크지너스)" 몬스터 1장을 자신의 덱 / 묘지에서 패에 넣는다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 올클리어(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/54573517.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 지속',value='이 카드명의 ③의 효과는 1턴에 1번밖에 사용할 수 없다.\r\n①: 필드의 "TG(테크지너스)" 몬스터는 기계족이 된다.\r\n②: 자신은 통상 소환 외에도 1번만, 자신 메인 페이즈에 "TG(테크지너스)" 몬스터 1장을 일반 소환할 수 있다.\r\n③: 자신 메인 페이즈에 발동할 수 있다. 자신의 패 / 필드의 "TG(테크지너스)" 몬스터 1장을 파괴하고,\r\n그 몬스터와는 카드명이 다른 "TG(테크지너스)" 몬스터 1장을 자신의 덱 / 묘지에서 패에 넣는다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG클로즈(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/2339825.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 카운터', value='이 카드명의 ①②의 효과는 1턴에 1번, 어느 쪽이든 1개밖에 사용할 수 없다.\r\n①: 자신 필드에 기계족인 "TG(테크지너스)" 몬스터가 존재하고, 몬스터의 효과 / 마법 / 함정 카드가 발동했을 때에 발동할 수 있다.\r\n그 발동을 무효로 하고 파괴한다.\r\n②: 이 카드가 묘지에 존재하는 상태에서, 싱크로 몬스터가 제외되었을 경우에 발동할 수 있다.\r\n이 카드를 자신 필드에 세트한다. 이 효과로 세트한 이 카드는 필드에서 벗어났을 경우에 제외된다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 클로즈(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/2339825.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 카운터',value='이 카드명의 ①②의 효과는 1턴에 1번, 어느 쪽이든 1개밖에 사용할 수 없다.\r\n①: 자신 필드에 기계족인 "TG(테크지너스)" 몬스터가 존재하고, 몬스터의 효과 / 마법 / 함정 카드가 발동했을 때에 발동할 수 있다.\r\n그 발동을 무효로 하고 파괴한다.\r\n②: 이 카드가 묘지에 존재하는 상태에서, 싱크로 몬스터가 제외되었을 경우에 발동할 수 있다.\r\n이 카드를 자신 필드에 세트한다. 이 효과로 세트한 이 카드는 필드에서 벗어났을 경우에 제외된다.',inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def TGX1HL(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/card/tgx1-hl-974', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 속공', value='자신 필드 위에 앞면 표시로 존재하는 "TG(테크지너스)"라는 이름이 붙은 몬스터 1장을 선택하고 발동한다.\r\n선택한 몬스터의 공격력 / 수비력을 절반으로 하고, 필드 위에 존재하는 마법 / 함정 카드 1장을 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def TGX300(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/58258899.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x1ABC9C)
    embed.add_field(name='마법 카드 / 지속', value='자신 필드 위에 앞면 표시로 존재하는 "TG(테크지너스)"라는 이름이 붙은 몬스터 1장당, 자신 필드 위에 앞면 표시로 존재하는 몬스터의 공격력은 300 포인트 올린다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def TG1EM1(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/76641981.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='상대 필드 위에 존재하는 몬스터 1장과, 자신 필드 위에 앞면 표시로 존재하는 "TG(테크지너스)"라는 이름이 붙은 몬스터 1장을 선택하고 발동한다.\r\n선택한 몬스터의 컨트롤을 맞바꾼다.', inline=True)
    embed.set_footer(text="미래의 운송 장치, 이번 도착지는 명계와 이차원임에 틀림없다.")
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def TGSX1(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/card/tg-sx1-3421', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='자신 필드 위에 존재하는 "TG(테크지너스)"라는 이름이 붙은 몬스터가 전투에 의해서 상대 몬스터를 파괴하고 묘지로 보냈을 때 발동할 수 있다.\r\n자신의 묘지에 존재하는 "TG(테크지너스)"라는 이름이 붙은 싱크로 몬스터 1장을 선택하고 특수 소환한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def TGX3DX2(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/3868277.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='이 카드명의 카드는 1턴에 1장밖에 발동할 수 없다.\r\n①: 패 / 덱에서 "미캉코" 몬스터 1장을 특수 소환한다. 그 후, 그 몬스터가 장착 가능한 장착 마법 카드 1장을 자신의 패 / 묘지에서 고르고 그 몬스터에 장착할 수 있다.\r\n이 효과로 특수 소환한 몬스터는, 필드에서 벗어났을 경우에 제외된다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 배틀스턴소닉(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/93138457.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='①: 상대 몬스터의 공격 선언시에 발동할 수 있다. 그 공격을 무효로 한다. 그 후, 패 / 덱에서 "TG(테크지너스)" 몬스터 또는 레벨 4 이하의 튜너 1장을 특수 소환할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 배틀스턴(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://images.ygoprodeck.com/images/cards/93138457.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x9B59B6)
    embed.add_field(name='함정 카드 / 일반', value='①: 상대 몬스터의 공격 선언시에 발동할 수 있다. 그 공격을 무효로 한다. 그 후, 패 / 덱에서 "TG(테크지너스)" 몬스터 또는 레벨 4 이하의 튜너 1장을 특수 소환할 수 있다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()


#엑소시스터

#샐러맨그레이트











#불꽃성기사
@bot.command()
async def 샤를대제(ctx):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send('https://ygoprodeck.com/cdn-cgi/image/format=auto,width=313/https://images.ygoprodeck.com/images/cards/97864322.jpg', delete_after=60 * 5)
    embed = discord.Embed(colour=0x206694)
    embed.add_field(name='전사족 / 링크 / 효과', value='장착 카드를 장착하고 있는 레벨 9의 "불꽃성기사제－샤를" 1장\r\n①: 이 카드가 링크 소환되었을 경우, 자신 묘지의 "불꽃성기사제－샤를" 1장을 대상으로 하고 발동할 수 있다.\r\n이 카드는 그 카드와 같은 이름의 카드로 취급하고, 같은 효과를 얻는다.\r\n그 후, 대상 몬스터를 공격력을 500 올리는 장착 카드로 취급하여 이 카드에 장착할 수 있다.\r\nㅤ\r\n②: 1턴에 1번, 마법 / 함정 카드의 효과가 발동했을 때, 자신의 패 / 필드(앞면 표시)에서 장착 마법 카드 1장을 묘지로 보내고 발동할 수 있다.\r\n그 효과를 무효로 하여 파괴한다.', inline=True)
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after = 60 * 5)
    await ctx.message.delete()






#기타
@bot.command()
async def 이모지(ctx):
    embed = discord.Embed(title='이모지 명령어 목록.',
                          colour=0xE67E22)
    embed.add_field(name='아래와 같습니다.', value='경악\r\n니비루\r\n번개\r\n지명자\r\n백룡행동\r\n패말림\r\n엘드리치인식\r\n카드창조\r\n셔플\r\n부장\r\n안녕', inline=True)
    embed.set_footer(text='과한 이모지 사용은 정신건강에 좋습니다.')
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed, delete_after=60 * 5)
    await ctx.message.delete()


@bot.command()
async def 경악(ctx):
    await ctx.channel.send('https://media.tenor.com/AdaSVzqCxLIAAAAC/yugioh-anime.gif', delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 니비루(ctx):
    await ctx.channel.send('https://media.tenor.com/H03bmjsgEtsAAAAC/nibiru-the-primal-being.gif', delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 카드창조(ctx):
    await ctx.channel.send('https://media.tenor.com/8UYcZMFmaEQAAAAC/yugioh-vrains.gif', delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 셔플(ctx):
    await ctx.channel.send('https://media.tenor.com/rcPDIaWqt6UAAAAC/yugioh.gif', delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 엘드리치인식(ctx):
    await ctx.channel.send('https://media.tenor.com/ywD2VdFX11oAAAAd/yugioh-yu-gi-oh-master-duel.gif', delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 백룡행동(ctx):
    await ctx.channel.send('https://media.tenor.com/ywD2VdFX11oAAAAd/yugioh-yu-gi-oh-master-duel.gif', delete_after=60 * 5)
    await ctx.message.delete()
@bot.command()
async def 무덤의지명자(ctx):
    await ctx.channel.send('https://media.tenor.com/sXL7vNlyhvsAAAAd/master-duel.gif', delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 번개(ctx):
    await ctx.channel.send('https://media.tenor.com/GpJmeRR8SdkAAAAd/master-duel.gif', delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 패말림(ctx):
    await ctx.channel.send('https://media.tenor.com/_VijVsYiXPQAAAAC/yugioh.gif', delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 부장(ctx):
    await ctx.channel.send("https://i.ibb.co/JRy9zRs/20230322120148.png", delete_after = 60 * 5)
    await ctx.message.delete()

@bot.command()
async def 안녕(ctx):
    await ctx.channel.send('https://i.ibb.co/Y7QHQk6/f2.jpg', delete_after=60 * 5)
    await ctx.message.delete()

@bot.command()
async def 함정(ctx):
    await ctx.channel.send('https://img.etnews.com/photonews/1103/114160 * 5_20110331134110_235_0001.jpg', delete_after=60 * 5)
    await ctx.message.delete()



# 디스코드 봇 토큰
bot.run('') #이 자리에 자신이 만든 봇의 토큰을 넣어주세요.