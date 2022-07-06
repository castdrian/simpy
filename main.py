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
	if 'subtitles' in video and parser.isoparse(video['time']).date() >= datetime.now().date() - timedelta(days=31):
			last_month.append(video['subtitles'][0]['name'])

data = Counter(x for x in last_month).most_common()[:15]
print('Top 15 most watched channels in the last month:\n','\n'.join([f'{x} - {y} videos' for x, y in zip([x[0] for x in data], [x[1] for x in data])]), sep='\n')
