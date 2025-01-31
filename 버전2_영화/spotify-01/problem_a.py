import json
from pprint import pprint


def artist_info(artist):
    artist_information={}
    artist_information['genres_ids']=artist_dict['genres_ids']
    artist_information['id']=artist_dict['id']
    artist_information['images']=artist_dict['images']
    artist_information['name']=artist_dict['name']
    artist_information['type']=artist_dict['type']
    return artist_information




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    pprint(artist_info(artist_dict))
