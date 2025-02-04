from setuptools import setup, find_packages

with open("README.md", "r") as file:
	long_description = file.read()

link = 'https://github.com/xXxCLOTIxXx/discord/archive/refs/heads/main.zip'
ver = '1.3.5'

setup(
	name = "udiscord",
	version = ver,
	url = "https://github.com/xXxCLOTIxXx/discord",
	download_url = link,
	license = "MIT",
	author = "Xsarz",
	author_email = "xsarzy@gmail.com",
	description = "Library for creating discord bots and scripts.",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	keywords = [
		"discord.py",
		"discord",
		"discord-py",
		"discord-bot",
		"api",
		"python",
		"python3",
		"python3.x",
		"xsarz",
		"official",
		"sync",
		"async"
	],
	install_requires = [
		"requests",
		"ujson",
		"logging",
		"websocket-client",
		"colorama",
		"aiohttp"
	],
	packages = find_packages()
)
