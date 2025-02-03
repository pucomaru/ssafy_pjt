import json


def artists_info(get):

    id_list = []
    
    for individual_information in get:
            
            id_list.append(individual_information['id'])
    
    return id_list





def max_popularity(artists_information_list):
    # 여기에 코드를 작성합니다.
    
    max = 0

    popular_artist = None

    numbers = artists_info(artists_information_list) # id 정보들 담김

    for i in numbers:
        artist_folder_json = open(current_dir / 'data' / 'artists'/ f'{i}.json', encoding='utf-8')
        artists_folder_list = json.load(artist_folder_json)
        if max <= artists_folder_list['popularity']:
            max = artists_folder_list['popularity']
            popular_artist =  artists_folder_list['name']
    
    return popular_artist




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)
    
    print(max_popularity(artists_list))
