"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
from pprint import pprint
from pathlib import Path



current_dir = Path(__file__).resolve().parent

artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
artists_list = json.load(artist_json)

genres_json = open(current_dir / 'data' / 'genres.json', encoding='utf-8')
genres_list = json.load(genres_json)


def artists_info(get):

    id_list = []
    
    for individual_information in get:
            
            id_list.append(individual_information['id'])
    
    return id_list


def genres_info():
    acoustic_id = None 
    for i in genres_list:
          if i['name'] == 'acoustic':
               acoustic_id = i['id']
    return acoustic_id          



def acoustic_artists():

    artists = []

    acoustic_id = genres_info()


    numbers = artists_info(artists_list)


    for i in numbers:

            artist_folder_json = open(current_dir / 'data' / 'artists'/ f'{i}.json', encoding='utf-8')
            artists_folder_list = json.load(artist_folder_json)

            for nums in artists_folder_list['genres_ids']:
                 if nums == acoustic_id:
                      artists.append(artists_folder_list['name'])

    return artists
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(acoustic_artists())
