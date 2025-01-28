import udiscord

email = "email@gmail.com" #account email
password = "password" #account password

client = discord.Client()
info = client.login(login=email, password=password)
print(info.json)
