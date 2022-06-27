# task1
from urllib.parse import urlparse

def domain_name(url):
	if url[0] == "w":
		url = "http://" + url								# Добавляем "http://" для корректного парсинга
	parsed = urlparse(url)
	parsed = parsed.netloc.split('.')
	while len(parsed[-1]) < 4:
		del parsed[-1]
	return parsed[-1]

# asserts
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("http://www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
