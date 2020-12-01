# Mock Text Discord Bot


import discord

TOKEN = '{BOT TOKEN HERE}'

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!mock'):
        channel = message.channel
        newmsg = message.content
        listmsg = newmsg.split()
        listmsg.remove("!mock")        
        def lst2str(s):  
            str1 = " "  
            return (str1.join(listmsg)) 
        msgcontent = lst2str(listmsg) 

        def mock(st):
            final = []
            for index, c in enumerate(st):
                if index % 2 == 0 & c.isalpha():
                    final.append(c.lower())
                else:
                    final.append(c.upper())
            return ''.join(final)

        await channel.send(file=discord.File('sbob.png'))
        await channel.send("***" + mock(msgcontent) + "***")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
