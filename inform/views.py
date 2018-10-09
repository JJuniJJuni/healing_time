import csv
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from inform.models import Shop


def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['1.get shop name', '2.developers'],
    })


@csrf_exempt
def message(request):
    message = (request.body.decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
    requestMode = return_str.encode('utf-8')
    if requestMode == '1.get shop name':
        return JsonResponse({
            'message': {
                'text': Shop.objects.all()[0].title
            },
            'keyboard': {
                'type': 'text'  # 텍스트로 입력받기 위하여 키보드 타입을 text로 설정
            }
        })


def save_shop_data(path):
    titles = [shop.title.replace(" ", "") for shop in Shop.objects.all()]
    with open(path, mode='r') as csv_file:
        for data in csv.DictReader(csv_file):
            if data["title"].replace(" ", "") not in titles:
                Shop.objects.create(title=data['title'], link=data['link'],
                                    category=data['category'],
                                    description=data['description'],
                                    telephone=data['telephone'],
                                    address=data['address'],
                                    road_address=data['roadAddress'],
                                    mapX=data['mapx'], mapY=data['mapy'])


if __name__ == "__main__":
    save_shop_data("../shop_data/konkuk_shop_info_craw.csv")
