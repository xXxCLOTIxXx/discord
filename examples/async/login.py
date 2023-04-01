import discord
import asyncio

email = "email@gmail.com" #account email
password = "password" #account password


async def main():
		client = discord.AsyncClient()
		f = await client.login(email=email, password=password)
		print(f.json)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())