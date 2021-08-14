# Check if the bot is up to date
import requests

def checkUpdate(version):
	url = requests.get(url="https://raw.githubusercontent.com/AsumaPT/draconBot/main/info.json")
	data = url.json()

	uptodate = True if data["version"] == version else False
	return uptodate

