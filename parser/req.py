import requests

def get_html(url):
	try:
		result = requests.get(url)
		result.raise_for_status()
		return result.text
	except requests.exceptions.RequestExceptions:
		print('Не вышло')
		return False
