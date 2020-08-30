import requests
from html5print import HTMLBeautifier

suchbegriff = input('What word to you want to be looked up on Youtube live? ').lower()
url = 'http://www.youtube.com/results?search_query=' + suchbegriff + '&sp=EgJAAQ%253D%253D'

scrape = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'})
data = HTMLBeautifier.beautify(scrape.text, 4).splitlines()

videoId = []
for ids in data:
    if '"addedVideoId": "' in ids:
        videoId.append(ids + '\n')

print()
print(''.join(videoId).replace(' ', '').replace('"addedVideoId":"', '').replace('"', '').replace(',', ''))
