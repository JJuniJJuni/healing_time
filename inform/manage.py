import csv

from inform.models import Shop
from inform.models import Review


def save_shop_data(path):
    shops = [(shop.place, shop.title.replace(" ", "")) for shop in Shop.objects.all()]
    with open(path, mode='r') as csv_file:
        for data in csv.DictReader(csv_file):
            if (data['place'], data["title"].replace(" ", "")) not in shops:
                Shop.objects.create(place=data['place'], title=data['title'],
                                    link=data['link'],
                                    category=data['category'],
                                    description=data['description'],
                                    telephone=data['telephone'],
                                    address=data['address'],
                                    road_address=data['roadAddress'],
                                    address_url='')


def save_review_data(path):
    titles = [(shop.id, shop.title.replace(' ', '')) for shop in Shop.objects.all()]
    with open(path, mode='r') as csv_file:
        for data in csv.DictReader(csv_file):
            try:
                idx = [title[1] for title in titles].index(data['shop'].replace(' ', ''))
            except ValueError:
                returned_shop = None
            else:
                returned_shop = Shop.objects.get(id=titles[idx][0])
            Review.objects.create(place=data['place'], title=data['shop'],
                                  url=data['url'], shop=returned_shop,
                                  review=data['review'])


def modify_shop_data(path):
    with open(path, mode='r') as csv_file:
        for data in csv.DictReader(csv_file):
            Shop.objects.filter(place=data['place'],
                                title=data['title']).update(
                category=data['category'])


def check_review_data(path):
    saved_shops = [(shop.place, shop.title.replace(' ', '')) for shop in Shop.objects.all()]
    with open(path, mode='r') as csv_file:
        for data in csv.DictReader(csv_file):
            if (data['place'], data['shop'].replace(' ', '')) not in saved_shops:
                print('현재 매칭되지 않는 Reivew 데이터는', data['place'], data['shop'])


if __name__ == '__main__':
    print(check_review_data('../shop_data/건대홍대강남_blog_review_181028_ansi'))