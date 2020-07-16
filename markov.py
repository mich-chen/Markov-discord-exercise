"""A Markov chain generator that can tweet random messages."""

import sys
from random import choice
import os
import discord


def open_and_read_file(filenames):
    """Take list of files. Open them, read them, and return one long string."""

    body = ''
    for filename in filenames:
        text_file = open(filename)
        body = body + text_file.read()
        text_file.close()

    return body


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains."""

    chains = {}

    words = text_string.split()
    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    return chains


def make_text(chains):
    """Take dictionary of Markov chains; return random text."""

    keys = list(chains.keys())
    key = choice(keys)

    words = [key[0], key[1]]
    while key in chains:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text).

        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

        word = choice(chains[key])
        words.append(word)
        key = (key[1], word)

    return ' '.join(words)


# Get the filenames from the user through a command line prompt, ex:
# python markov.py green-eggs.txt shakespeare.txt
filenames = sys.argv[1:]

# Open the files and turn them into one long string
text = open_and_read_file(filenames)

# Get a Markov chain
chains = make_chains(text)

random_text = make_text(chains)

"""********************************************************************"""

client = discord.Client()
# creates instance of class Client
# this client is connect to discord


@client.event
# register an event
# do things in 'callback'
# callback is function that is called when something happens

#on_ready function called when bot finished logging in and set things up
async def on_ready():

    print(f'Successfully connected! Logged in as {client.user}')

@client.event
# on_message called when bot received message
async def on_message(message):

    if message.author == client.user:
        # checks if author of message received is same as client.user
        # check if the message is from ourself
        return

    if message.content.startswith('hello'):
        # if message starts with '$hello'
        
        await message.channel.send('wassuppppp', random_text)
        # reply to channel it was used in

client.run(os.environ['DISCORD_TOKEN'])
# run bot with login token

# run bot in terminal with $python example_bot.py



# print(random_text)
