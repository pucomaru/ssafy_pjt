import json
from pprint import pprint


def artist_info(artist, genres):
    artist_information={}
    # artist_information['genres_names']=artist_dict['genres_ids']
    artist_information['genres_names']=[]
    for i in range(len(genres)):
        if genres[i]['id'] == artist['genres_ids'][0] :
            artist_information['genres_names'].append(genres[i]['name'])
        if genres[i]['id'] == artist['genres_ids'][1] : 
            artist_information['genres_names'].append(genres[i]['name'])

    artist_information['id']=artist['id']
    artist_information['images']=artist['images']
    artist_information['name']=artist['name']
    artist_information['type']=artist['type']
    return artist_information
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open(current_dir / 'data' / 'genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
