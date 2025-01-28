import udiscord

email = "email@gmail.com" #account email
password = "password" #account password

client = udiscord.Client()
info = client.login(login=email, password=password)
print(info.json)
