from collections import Counter
from datetime import timedelta
from dateutil.parser import isoparse
from json import loads
from sys import exit

try:
	with open('watch-history.json', 'r', encoding='utf-8') as f:
		data = loads(f.read())
except FileNotFoundError:
	exit('File watch-history.json not found.')
	
last_month = []
for video in data:
	if 'subtitles' in video and isoparse(video['time']).date() >= isoparse(data[0]['time']).date() - timedelta(days=31):
			last_month.append(video['subtitles'][0]['name'])

data = Counter(last_month).most_common()[:15]
print('Top 15 most watched channels in the past month:\n', '\n'.join([f'{x} - {y} videos' for x, y in zip([x[0] for x in data], [x[1] for x in data])]), sep='\n')
