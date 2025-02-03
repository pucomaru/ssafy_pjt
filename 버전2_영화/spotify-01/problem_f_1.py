"""
    팔로워가 5,000,000 이상, 10,000,000 미만인 아티스트의 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint
from pathlib import Path

current_dir = Path(__file__).resolve().parent


def artists_info(get):

    id_list = []
    
    for individual_information in get:
            
            id_list.append(individual_information['id'])
    
    return id_list



def get_popular(artists_information_list):
    # 여기에 코드를 작성합니다.
    artists = []

    numbers = artists_info(artists_information_list)
    for i in numbers:
            artists_information={}

            artist_folder_json = open(current_dir / 'data' / 'artists'/ f'{i}.json', encoding='utf-8')
            artists_folder_list = json.load(artist_folder_json)

            if 5000000 <= artists_folder_list['followers']['total'] < 10000000 : 
                artists_information['followers'] = artists_folder_list['followers']['total']
                artists_information['name'] = artists_folder_list['name']
                artists.append(artists_information)
    
    return artists


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)


    pprint(get_popular(artists_list))

