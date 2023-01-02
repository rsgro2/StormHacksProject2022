import discord
import random
import time

keyword = ''
hint = ''
guess = 0
control = 1

#FOR QUOTES
quoteOpen = open("quotes.txt",'r',encoding="utf-8")
quotes = []
for quote in quoteOpen:
    quote = quote.strip()
    quotes.append(quote)

animals = {"spider" : "Hint: 6 letter word",
"walrus" : "Hint: 6 letter word",
"monkey" : "Hint: 6 letter word",
"turtle" : "Hint: 6 letter word",
"wombat" : "Hint: 6 letter word",
"parrot" : "Hint: 6 letter word",
"alpaca" : "Hint: 6 letter word",
"salmon" : "Hint: 6 letter word",
"beaver" : "Hint: 6 letter word",
"rabbit" : "Hint: 6 letter word",
"falcon" : "Hint: 6 letter word",
"bobcat" : "Hint: 6 letter word",
"cougar" : "Hint: 6 letter word",
"jaguar" : "Hint: 6 letter word",
"pigeon" : "Hint: 6 letter word",
"toucan" : "Hint: 6 letter word",
"canary" : "Hint: 6 letter word",
}

countries = {"canada" : "Hint: 6 letter word",
"brazil" : "Hint: 6 letter word",
"france" : "Hint: 6 letter word",
"mexico" : "Hint: 6 letter word",
"monaco" : "Hint: 6 letter word",
"poland" : "Hint: 6 letter word",
"russia" : "Hint: 6 letter word",
"turkey" : "Hint: 6 letter word",
"sweden" : "Hint: 6 letter word",
"serbia" : "Hint: 6 letter word",
"israel" : "Hint: 6 letter word",
"greece" : "Hint: 6 letter word",
"angola" : "Hint: 6 letter word",
"kosovo" : "Hint: 6 letter word",
"belize" : "Hint: 6 letter word",
"jordan" : "Hint: 6 letter word",
"latvia" : "Hint: 6 letter word",
"norway" : "Hint: 6 letter word",
"panama" : "Hint: 6 letter word",
"taiwan" : "Hint: 6 letter word",
"uganda" : "Hint: 6 letter word",
"zambia" : "Hint: 6 letter word",
"brunei" : "Hint: 6 letter word",
"guinea" : "Hint: 6 letter word",
"guyana" : "Hint: 6 letter word",
}

client = discord.Client()
client = discord.Client()

@client.event
async def on_ready():  
    channel = client.get_channel(discord channel ID) 
    await channel.send('Hi, I am Break Bot! Enter "i need a break" if you want to play a fun game or enter "inspire me" if you want an inspirational quote: ')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event 
async def on_message(message, a = None):
    if message.content.startswith('inspire me'):
        await message.channel.send(random.choice(quotes))

    if message.author == client.user:
        return

    global keyword
    global hint
    global control

    if message.content.startswith('i need a break'):
        await message.channel.send("Lets play Wardle!")

        await message.channel.send("Choose and enter your theme (animals, countries): ")
        return 

    if message.content.startswith("animals"): 
        items = random.choice(list(animals.items()))
        keyword = items[0]
        hint = items[1]
        userInput = "animals"
        await message.channel.send("{} . Enter your guess: ".format(hint))
        control = 0
        return
        

    elif message.content.startswith("countries"):
        items = random.choice(list(countries.items()))
        keyword = items[0]
        hint = items[1]
        userInput = "countries"
        await message.channel.send("{} . Enter your guess: ".format(hint))
        control = 0
        return
        
    elif control == 0:
        global guess
        await message.channel.send("Enter your guess: ")
        if guess<6:
            guess += 1
            
            displayGuess = ""
            underline = "\u0332"
            
            i=0
            for letter in message.content:
                if letter in keyword:
                    if letter == keyword[i]:
                        displayGuess += letter
                    else:
                        displayGuess += letter
                        displayGuess += underline

                else:
                    displayGuess += "\-"
        
                i+=1
            await message.channel.send("Result is {}".format(displayGuess))
        else:
            await message.channel.send("The answer was {}!".format(keyword))
            control = 1
  
        
client.run('DISCORD BOT TOKEN')
