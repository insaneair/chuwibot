import discord
from discord.ext import commands
import random
import requests

# 봇의 접두사 설정
prefix = "!"

# Intents 설정
intents = discord.Intents.default()
client = discord.Client(intents=intents)
intents.typing = False
intents.presences = False
intents.message_content = True
intents.members = True

# 봇 객체 생성
bot = commands.Bot(command_prefix='!', intents=intents)

# 봇이 준비되었을 때 실행되는 이벤트 핸들러
@bot.event
async def on_ready():
    print(f"봇이 로그인하였습니다. (이름: {bot.user.name}, ID: {bot.user.id})")
    # 활동 정보 설정
    activity = discord.Game(name="맛있는 추이고기 먹방")
    await bot.change_presence(activity=activity)


# 공지 명령어 처리
@bot.command()
@commands.has_permissions(administrator=True)
async def 공지(ctx, *, message):
    # 공지를 보낼 채널 ID
    channel_id = 1106143767288885259

    # 공지를 보낼 채널 객체 가져오기
    channel = bot.get_channel(channel_id)

    # 공지를 보내는 로직
    embed = discord.Embed(title="공지사항", description=message, color=discord.Color.blue())
    embed.set_footer(text=f"작성자: {ctx.author.display_name}")
    await channel.send(embed=embed)

    # 명령어 메시지 삭제
    await ctx.message.delete()

# 주사위 명령어 처리
@bot.command()
async def 주사위(ctx):
    # 주사위 숫자 랜덤 생성 (1부터 6까지)
    dice = random.randint(1, 6)
    await ctx.send(f"주사위를 굴려 {dice}이(가) 나왔습니다!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '!추이는':
        embed = discord.Embed(description='범죄자다', color=discord.Color.green())
        await message.channel.send(embed=embed)

    if message.content == '!공기는':
        embed = discord.Embed(description='문화다', color=discord.Color.green())
        await message.channel.send(embed=embed)
    if message.content == '!민초는':
        embed = discord.Embed(description='문화다', color=discord.Color.green())
        await message.channel.send(embed=embed)
    if message.content == '!승우는':
        embed = discord.Embed(description='추이다', color=discord.Color.green())
        await message.channel.send(embed=embed)
    if message.content == '!서버정보':
        embed = discord.Embed(description='위 서버는 유니브 서버가 붕괴된 이후 서버원들 끼리 모여 만든 대피소이다 이서버를 만든이는 승우이고 현재 운영자는 승우와 공기이다 이 서버의 서버교는 추이교로 추이라는 유일신을 숭배하는 종교이다 현재 서버원은 관리자포함 7명이고 봇은 8개이다', color=discord.Color.green())
        await message.channel.send(embed=embed)
    if message.content == "!추이": #추이사진전송
        await message.channel.send("https://i.imgur.com/fqFabOj.jpg")



    await bot.process_commands(message)
    

# 명령어 목록 보기
@bot.command()
async def 도움(ctx):
    # 사용 가능한 명령어 리스트
    command_list = bot.commands
    command_names = [command.name for command in command_list]

    # 명령어 목록을 Embed 형태로 출력
    embed = discord.Embed(title="명령어 목록", description="사용 가능한 명령어들입니다.", color=discord.Color.green())
    embed.add_field(name="공지", value="!공지 [내용] - 공지를 작성합니다. (작성 후 메시지가 자동으로 삭제됩니다.)", inline=False)
    embed.add_field(name="주사위", value="!주사위 - 1부터 6까지의 숫자 중 하나를 랜덤으로 출력합니다.", inline=False)
    embed.add_field(name="도움", value="!도움 - 사용 가능한 명령어 목록을 보여줍니다.", inline=False)
    embed.add_field(name="추이는", value="!추이는 - 추이가 바보라는것을 알려줍니다", inline=False)
    embed.add_field(name="공기는", value="!공기는 - 공기가 문화라는것을 알려줍니다", inline=False)
    embed.add_field(name="민초는", value="!민초는 - 민초가 문화라는것을 알려줍니다", inline=False)
    embed.add_field(name="승우는", value="!승우는 - 승우가 추이라는것을 알려줍니다", inline=False)
    embed.add_field(name="추이", value="!추이 - 추이의 셀카를 보여줍니다", inline=False)
    embed.add_field(name="서버정보", value="!서버정보 - 서버에 대한 정보를 알려줍니다", inline=False)


    await ctx.send(embed=embed)

# 봇 토큰으로 봇 로그인
bot.run("MTEwOTExNjczNjIzNTYzNDgwOA.Gzpd8b.piKg5lLWCJJ8uedibvdMAkjR9P-YsCjQZtTTpo")