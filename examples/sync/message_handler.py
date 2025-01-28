import udiscord

email = "email@gmail.com" #account email
password = "password" #account password

client = udiscord.Client()
client.login(login=email, password=password)

@client.event(udiscord.EventType.MESSAGE_CREATE)
def on_message(event: udiscord.Event):
    print(event.data)

#or
#client.add_handler(udiscord.EventType.MESSAGE_CREATE, on_message)