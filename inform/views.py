import csv

from inform.models import Shop
from django.http import JsonResponse


def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['1.healing time', '2.developers'],
    })


def save_shop_data(path):
    titles = [shop.title.replace(" ", "") for shop in Shop.objects.all()]
    with open(path, mode='r') as csv_file:
        for data in csv.DictReader(csv_file):
            if data["title"].replace(" ", "") not in titles:
                Shop.objects.create(title=data['title'], link=data['link'], category=data['category'],
                                  description=data['description'], telephone=data['telephone'],
                                  address=data['address'], road_address=data['roadAddress'],
                                  mapX=data['mapx'], mapY=data['mapy'])


if __name__ == "__main__":
    save_shop_data("../shop_data/konkuk_shop_info_craw.csv")
