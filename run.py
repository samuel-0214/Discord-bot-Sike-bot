#Since we are using more that one __init__.py files so we are compelled to run this run.py file on the app level directory
#So to do that we need to import all the packages 

from app.discord_bot.discord_api import client,discord_token

if __name__ == '__main__':
    client.run(discord_token)