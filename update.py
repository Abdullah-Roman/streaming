import json
import urllib.request

JSON_URL = "https://raw.githubusercontent.com/srhady/tapmad-bd/refs/heads/main/tapmad_bd.json"
M3U_FILE = "live.m3u"

# Define your default channels here. 
# They will always appear at the top of the playlist.
STATIC_CHANNELS = """#EXTM3U
#EXTINF:-1 tvg-logo="https://iili.io/CjUgT6G.th.jpg" group-title="Sports LIVE",T Sports
https://tvsen5.aynaott.com/TnMn5kZz8aLm/tracks-v1a1/mono.ts.m3u8
"""

def generate_m3u():
    # Fetch the JSON data
    req = urllib.request.Request(JSON_URL, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
        
        channels = data if isinstance(data, list) else data.get('channels', [])
    except Exception as e:
        print(f"Error fetching JSON: {e}")
        return

    # Write static channels first, then append the dynamic Tapmad channels
    with open(M3U_FILE, 'w', encoding='utf-8') as f:
        f.write(STATIC_CHANNELS)
        
        for ch in channels:
            name = ch.get('name', ch.get('title', 'Unknown Channel'))
            url = ch.get('url', ch.get('link', ''))
            logo = ch.get('logo', ch.get('tvg-logo', ''))
            
            # FORCE the group title so your Blogger theme parses it into the Sports slider
            group = "Sports LIVE"

            if url:
                f.write(f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n')
                f.write(f'{url}\n')

if __name__ == "__main__":
    generate_m3u()
