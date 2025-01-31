import json
from pathlib import Path



def max_popularity(artists):
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artists_detail = open(current_dir / 'data' / '116.json' , encoding='utf-8' )

    print(artists_detail)    

    

    return

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    print(max_popularity(artists_list))
