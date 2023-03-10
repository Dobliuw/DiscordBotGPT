import discord 
import subprocess, openai, os
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 

client = commands.Bot(command_prefix='!', intents=intents)
#client = discord.Client(intents=intents)

load_dotenv()

api_key = os.getenv("API_KEY")
client_key = os.getenv("CLIENT_KEY")
openai.api_key = api_key


def chatGPT(command): 
    messages = [{"role": "system", "content": "Sos un bot de ayuda para discord"}]
    messages.append({"role": "user", "content": command})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    output = response.choices[0].message.content
    return output


@client.event 
async def on_ready():
    print(f"Me loguie como {client.user} compa")

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if client.user in message.mentions:
        author_mention = message.author.mention
        await message.channel.send(f"Que onda {author_mention}, todo bien??")
        
    await client.process_commands(message)


@client.command()
async def dobliuw(ctx):
    await ctx.send("""
    :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: DOBLIUW´S INFO :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: :flag_ar: 
    :gem: --> Linkedin: https://www.linkedin.com/in/dev-owen/  
    :gem: --> Github: https://github.com/OwenConW              
    :gem: --> Discord: </Dobliuw>#9986                         
    :gem: --> Instagram: https://www.instagram.com/owenconw 
    """)


@client.command()
async def ask(ctx, *texto):
    await ctx.send("\n\n\t`Bancame que estoy escribiendo...`\n")
    command = " ".join(texto)
    output = chatGPT(command)
    #author_name = discord.utils.escape_mentions(ctx.author.display_name)
    #author_mention = f"@{author_name}"
    author_mention = ctx.author.mention
    await ctx.channel.send("\n%s tu respuesta a \"%s\":  %s" % (author_mention, command, output))    


client.run(client_key)
