from collections import Counter
from datetime import datetime, timedelta
from dateutil import parser
from json import loads

try:
	with open('watch-history.json', 'r', encoding='utf-8') as f:
		data = loads(f.read())
except FileNotFoundError:
	print('File watch-history.json not found.')
	exit()

last_month = []

for video in data:
	time = parser.isoparse(video['time'])

	if 'subtitles' in video:
		if time.date() >= datetime.now().date() - timedelta(days=31):
			last_month.append({ 'name': video['subtitles'][0]['name'], 'url': video['subtitles'][0]['url'] })

data = Counter(x['name'] for x in last_month).most_common()[:15]

channels = [x[0] for x in data]
counts = [x[1] for x in data]

print('Top 15 most watched channels in the last month:\n\n')
print('\n'.join([f'{x} - {y} videos' for x, y in zip(channels, counts)]))
