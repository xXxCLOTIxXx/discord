import discord

email = "email@gmail.com" #account email
password = "password" #account password

client = discord.Client()
info = client.login(email=email, password=password)
print(info.json)