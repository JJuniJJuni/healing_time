import csv
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from inform.dialog_flow import get_answer
from inform.models import Shop


def keyboard(request):
    return JsonResponse({
        'type': 'text',
        'content': '안녕하세요 힐링타임 추천 서비스 입니다. 무엇을 도와드릴까요?'
    })


@csrf_exempt
def message(request):
    message = (request.body.decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
    return JsonResponse({
        'message': {
            'text': get_answer(return_str),
        },
        'keyboard': {
            'type': 'text',
        }
    })


def save_shop_data(path):
    shops = [(shop.place, shop.title.replace(" ", "")) for shop in Shop.objects.all()]
    with open(path, mode='r') as csv_file:
        for data in csv.DictReader(csv_file):
            if (data['place'] , data["title"].replace(" ", "")) not in shops:
                Shop.objects.create(place=data['place'], title=data['title'],
                                    link=data['link'],
                                    category=data['category'],
                                    description=data['description'],
                                    telephone=data['telephone'],
                                    address=data['address'],
                                    road_address=data['roadAddress'],
                                    mapX=data['mapx'], mapY=data['mapy'])


def modify_shop_data(path):
    with open(path, mode='r') as csv_file:
        for data in csv.DictReader(csv_file):
            Shop.objects.filter(place=data['place'],
                                title=data['title']).update(
                category=data['category'])


def check_data(path):
    names = []
    titles = {}
    overwritten = []
    with open(path, mode='r') as csv_file:
        for data in csv.DictReader(csv_file):
            place, title = data['place'], data['title']
            if (place, title) not in names:
                names.append((place, title))
                titles[(place, title)] = 1
            else:
                overwritten.append(object)
                titles[(place, title)] += 1
    for over in overwritten:
        print(over)


if __name__ == "__main__":
    save_shop_data("../shop_data/shop_info_craw_ansi.csv")
