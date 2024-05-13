from dotenv import load_dotenv
import discord
import os

from app.sike_ai.open_ai import sike_response

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

#This class applies to the bot logging into the server
class MyClient(discord.Client):
    async def on_ready(self):
        print("Successfully logged in as:",self.user)

    #This class is resposible for the messages
    async def on_message(self, message):
        print(message.content) #This is to print the message that has been received in the command line
        if message.author == self.user: #In case if the user talks with the other members in the server,we dont want the bot to reply to that message so we print nothing
            return
        command, user_message = None , None

        for text in ['/sike','/bot']:
            if message.content.startswith(text):
                command= message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command , user_message)

        if command == '/sike' or command == '/bot':
            bot_response = sike_response(prompt = user_message)
            await message.channel.send(f"Answer: {bot_response}")

intents = discord.Intents.default()
intents.message_content =  True

client = MyClient(intents=intents)