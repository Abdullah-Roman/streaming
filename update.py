import json
import urllib.request
import os

JSON_URL = "https://raw.githubusercontent.com/srhady/tapmad-bd/refs/heads/main/tapmad_bd.json"
M3U_FILE = "live.m3u"

def generate_m3u():
    # Fetch the JSON data
    req = urllib.request.Request(JSON_URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    
    # Handle different JSON structures (list vs object containing a list)
    channels = data if isinstance(data, list) else data.get('channels', [])

    # Write data to live.m3u
    with open(M3U_FILE, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        
        for ch in channels:
            # Extract fields, falling back to defaults if they don't exist
            name = ch.get('name', ch.get('title', 'Unknown Channel'))
            url = ch.get('url', ch.get('link', ''))
            logo = ch.get('logo', ch.get('tvg-logo', ''))
            group = ch.get('group', ch.get('category', 'Tapmad BD'))

            if url:
                f.write(f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n')
                f.write(f'{url}\n')

if __name__ == "__main__":
    generate_m3u()
