import os
import nextcord

activity = nextcord.Activity(name='your every word', type = nextcord.ActivityType.listening)
bot = nextcord.Client(activity=activity)

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
            output = convert(msg.content, value)
            if output == None:
                return
            else:
                await msg.channel.send(f'**{msg.author},** {output}')

@bot.event
async def on_ready():
    print(f'{bot.user} is live!')
    

bot.run(os.environ['TOKEN'])

