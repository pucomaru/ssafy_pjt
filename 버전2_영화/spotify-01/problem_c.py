import json
from pprint import pprint


def artist_info(artists, genres):
    total_list=[]

    for i in range(len(artists)):

        artist_information={}
        
        artist_information['genres_names']=[]

        for artists_ids_num_list in artists[i]['genres_ids']:
            for genres_list in genres:
                if genres_list['id'] == artists_ids_num_list: 
                    artist_information['genres_names'].append(genres_list['name'])

        artist_information['id']=artists[i]['id']
        artist_information['images']=artists[i]['images']
        artist_information['name']=artists[i]['name']
        artist_information['type']=artists[i]['type']

        total_list.append(artist_information)

    return total_list





# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    genres_json = open(current_dir / 'data' / 'genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
