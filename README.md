<body>
	<h1 align="center">
		<img src="https://github.com/xXxCLOTIxXx/discord/blob/main/docs/res/banner.png" alt="UDISCORD">
	</h1>
	<p align="center">
	    <a href="https://github.com/xXxCLOTIxXx/discord/releases"><img src="https://img.shields.io/github/v/release/xXxCLOTIxXx/discord" alt="GitHub release" />
	    <a href="https://pypi.org/project/udiscord/"><img src="https://img.shields.io/pypi/v/udiscord.svg" alt="Pypi version" />
	    <img src="https://img.shields.io/pypi/dm/udiscord" />
	    <a href="https://github.com/xXxCLOTIxXx/discord/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="license" /></a>
	    <a href="https://github.com/xXxCLOTIxXx/discord/blob/main/docs/index.md"><img src="https://img.shields.io/website?down_message=failing&label=docs&up_color=green&up_message=passing&url=https://github.com/xXxCLOTIxXx/discord/blob/main/docs/index.md" alt="docs" /></a>
	</p>
	<div align="center">
		<a href="https://github.com/xXxCLOTIxXx/xXxCLOTIxXx/blob/main/sponsor.md">
			<img src="https://img.shields.io/static/v1?style=for-the-badge&label=Sponsor project&message=%E2%9D%A4&color=ff69b4" alt="Sponsor project"/>
		</a>
		<a href="https://github.com/xXxCLOTIxXx/xXxCLOTIxXx/blob/main/contacts.md">
      		<img src="https://img.shields.io/badge/Contacts-Contacts-F79B1F?style=for-the-badge&amp;logoColor=0077b6&amp;color=0077b6" alt="Contacts"/>
		</a>
	</div>
	<br>
	<p align="center"><b>UDISCORD</b> — A library for creating user bots on Discord based on unofficial API, obtained by analyzing web traffic and mobile app traffic.</p>
	<p align="center">
		UDISCORD provides access to various features for managing a Discord account, such as bans, kicks, sending messages, receiving events, and much more. The library is designed for ease of use and allows automating many processes on Discord.
	</p>
	<p align="center">
		⚠️ Important! Abuse of this library for malicious purposes or violation of Discord's rules may lead to account suspension or banning.
	</p>
	<h2 align="center">Code Examples</h2>
	<h3>🔹 Login with Email and Password</h3>

```python
from udiscord import Client, Message

# Create a client instance
client = Client()

# Log in with email and password (this also initiates the socket connection)
info = client.login(email="email", password="password")
print(info.token)  # Prints the token after successful login

# Log out and disconnect from the socket
client.logout()
```
<h3>🔹 Command and Event Handling</h3>

```python
@client.command(["!commands", "/commands"])
def get_commands(message: Message):
    # The bot will reply saying it doesn't have commands
    client.send_message(message.channelId, "Sorry, I don't have commands :_(")
```

<div align="center">
	<a href="https://github.com/xXxCLOTIxXx/discord/blob/main/docs/index.md">
		<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=14&duration=1&pause=31&color=3DACF7&random=false&width=195&lines=Read+the+documentation" alt="Read the documentation"/>
	</a>
</div>
</body>
