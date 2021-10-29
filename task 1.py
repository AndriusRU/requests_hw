from pprint import pprint
import requests

token = "2619421814940190"
def search_id(name_hero):
    url = f"https://superheroapi.com/api/{token}/search/{name_hero}"
    response = requests.get(url, timeout=5)
    return response.json().get('results')[0].get('id')


def hero_character(id_hero):
    url = f"https://superheroapi.com/api/{token}/{id_hero}/powerstats"
    response = requests.get(url, timeout=10)
    return response.json().get('intelligence')

def best_intelligence(list_heros):
    new_dict = {}
    for item in list_heros:
        new_dict[item] = int(hero_character(search_id(item)))
    max_value = max(new_dict.values())
    out_dict = {}
    for key, value in new_dict.items():
        if value == max_value:
            out_dict[key] = value
    return out_dict


if __name__ == '__main__':
    list_heros = ['Hulk', 'Captain America', 'Thanos']
    print(*best_intelligence(list_heros).keys())