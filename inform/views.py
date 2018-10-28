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
    answer = get_answer(return_str)
    if '주변에 갈만한 곳' in answer:
        answer = '건대 주변에는 VR 체험, 보드 게임방, 고양이 카페들이 있어요!!'
    elif '위치' in answer:
        answer = '하앍'
        answer = 'https://map.naver.com/?mapmode=0&lng=723' \
                 'b2d03d073e2849ec2ea83f18361b1&pinId=1951264' \
                 '1&pinType=site&lat=56c918fb541e28ad8f4efb21ed' \
                 'a1cf3a&dlevel=11&enc=b64'
    elif '고양이' in answer:
        shops = Shop.objects.filter(place='건대', category='테마카페>고양이카페')
        answer = '건대 주변 고양이 카페로는'
        for idx, shop in enumerate(shops):
            answer += '\n{0}.{1}'.format(idx+1, shop.title)
        answer += '\n위와 같이 있네요!!'
    elif '데이트 추천' in answer:
        answer = '데이트로는 단 둘이 보드 게임방 어떠세요?'
    return JsonResponse({
        'message': {
            'text': answer,
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
