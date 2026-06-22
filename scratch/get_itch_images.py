import urllib.request
import re

urls = [
    'https://weirdothen.itch.io/erashift',
    'https://birdbox774.itch.io/logic-rift'
]

for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    match = re.search(r'"og:image"\s+content="([^"]+)"', html)
    if match:
        print(f"URL: {url} -> Image: {match.group(1)}")
    else:
        print(f"URL: {url} -> No image found")
