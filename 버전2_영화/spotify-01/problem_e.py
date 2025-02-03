import json
from pprint import pprint


def artists_info(get):

    id_list = []
    
    for individual_information in get:
            
            id_list.append(individual_information['id'])
    
    return id_list




def dec_artists(artists_information_list):
    # 여기에 코드를 작성합니다.

    numbers = artists_info(artists_information_list) # id 정보들 담김

    popular_artists=[]


    for i in numbers:
        artists_information={}

        artist_folder_json = open(current_dir / 'data' / 'artists'/ f'{i}.json', encoding='utf-8')
        artists_folder_list = json.load(artist_folder_json)

        if artists_folder_list['followers']['total'] > 10000000 : 
            artists_information['name'] = artists_folder_list['name']
            artists_information['uri-id'] =artists_folder_list['uri'].split(":")[-1]
            popular_artists.append(artists_information)
            
    return popular_artists


    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    pprint(dec_artists(artists_list))
