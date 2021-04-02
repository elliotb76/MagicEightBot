# created with https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
import discord
import os, sys
import json
import random
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

client = discord.Client()

magic8Responses1 = [
    "It is certain.", "It is decidedly so.", "Without a doubt.",
    "Yes – definitely.", "You may rely on it.", "As I see it, yes.",
    "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
    "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
    "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.",
    "My reply is no.", "My sources say no.", "Outlook not so good.",
    "Very doubtful."
]

uWuWords = [
    "uwu", "owo", "daddy", "moist", "daddi"
]

uWuResponses = [
    "What's this?", "(° ͜ʖ °)", "( ͡° ͜ʖ ͡°)", "( ͡° ͜ʖ ͡°)╭∩╮", "( ͡~ ͜ʖ ͡°)", "( ͡◉ ͜ʖ ͡◉)", "[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]", "( ͡ಠ ʖ̯ ͡ಠ)", "╭∩╮( ͡° ل͟ ͡° )╭∩╮", "( ͡° ͜ʖ ͡°)︻̷┻̿═━一-", "(ง ͡° ͜ʖ ͡°)=/̵͇̿̿/'̿'̿̿̿ ̿ ̿̿'", "( ͡◕ ͜ʖ ͡◕)", "(◉͜ʖ◉)", "(つ ♥ ͜ʖ ♥)つ", "( ͝סּ ͜ʖ͡סּ)"
]

monkeWords = [
    "monke", "ape"
]

monkeResponses = [
    "Did someone say... monke?", "M O N K E", "Apes together strong", "Uh ohh...", "where banana"
]

whomstResponses = [
    "'ly", "'yaint", "'nt", "'ed", "'ies", "'s", "'y", "'es", "'nt", "'ed", "'ies", "'s", "'y", "'es", "'nt", "'t", "'re", "'ing", "'able", "'ric", "'ive", "'al", "'nt", "'ne", "'m", "'ll", "'ble", "'al"
]

# if a question contains one of these words, we should probably respond
includeWords = [
    "is", "am", "are", "was", "were", "do", "does", "did", "will", "can", "could", "should", "would", "has", "have",
    "than", "good", "bad"
]

# if a question starts with one of these words, ignore it
# possible to ask 'do you know who?' which would be a y/n.
excludeStartWords = [
    "what", "why", "when", "how", "where", "who", "whose"
]

excludeWords = [
    "or"
]

magic8Responses = list()
responsesFilePath = os.getcwd() + os.sep + "responses.json"

with open(responsesFilePath) as file:
    responses = json.load(file)
    for item in responses:
        magic8Responses.append(item)
# print(magic8Responses)


@client.event
async def on_ready():
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ' -- We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    msg = message.content.lower()
    msgStripped = msg.replace(' ', '')

    if msgStripped.find("monke") != -1:
        await message.channel.send(random.choice(monkeResponses))

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if "whomst" in msg:
        whomstResponseMessage = 'whomst'
        whomstResponsesTemp = whomstResponses[:]
        # print("list length: " + str(len(whomstResponses)))
        numEndings = random.randint(2, len(whomstResponses)-1)
        # print("Expected number of endings: " + str(numEndings))
        for x in range(numEndings):
            randEndingIndex = random.randint(0, len(whomstResponsesTemp)-1)
            # print("Index of ending to add: " + str(randEndingIndex))
            whomstResponseMessage += whomstResponsesTemp[randEndingIndex]
            whomstResponsesTemp.remove(whomstResponsesTemp[randEndingIndex])
        await message.channel.send(whomstResponseMessage)  # WHOMST
        # print(whomstResponseMessage)

    if msg.endswith('?'):
        msg = msg.replace('?', '')
        msg_ = msg.split()
        if "outlook" in msg: await message.channel.send("Fuck Outlook")  # fuck outlook
        # respond in a smart way to y/n questions? question has 'is' or 'does' 'can' 'will' 'are' 'do' 'you I'

        for word in excludeStartWords:
            if msg.startswith(word): return
            if any(word in msg_ for word in excludeWords): return

        # if msg contains one of the include words, reply
        if any(word in msg_ for word in includeWords):
            await message.channel.send(random.choice(responses))
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ' -- Replying to question')
            # add TTS in the future?

    msg_ = msg.split()
    if any(word in msg_ for word in uWuWords):
        # await message.channel.send("What's this?")
        uWuRand = random.randint(0, 1)
        if uWuRand == 0:
            await message.channel.send("What's this?")
        else:
            await message.channel.send(random.choice(uWuResponses))

load_dotenv(find_dotenv())
client.run(os.getenv('TOKEN'))
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ' -- Client exiting')

