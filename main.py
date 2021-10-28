import os
import nextcord

bot = nextcord.Client()

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return

    if msg.content:
        from parser import parse_num
        from converter import convert
        value = parse_num(msg.content)
        if value == None:
            return;
        else:
            await msg.channel.send(f'**{msg.author},** {convert(msg.content, value)}')

@bot.event
async def on_ready():
    print(f'{bot.user} is live!')

bot.run(os.environ['TOKEN'])

