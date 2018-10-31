import csv
import math

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
    etc = Shop.objects.get(title='기타')
    with open(path, mode='r') as csv_file:
        for data in csv.DictReader(csv_file):
            try:
                idx = [title[1] for title in titles].index(data['shop'].replace(' ', ''))
            except ValueError:
                returned_shop = etc
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
    count = 0
    with open(path, mode='r') as csv_file:
        for data in csv.DictReader(csv_file):
            count += 1
            try:
                shop = Review.objects.filter(url=data['url'])
                print('현재 데이터는 {} 지역 {} 입니다.'.format(data['place'], data['shop']))
            except KeyError:
                print('없는 데이터는 {} 지역 {} 입니다.'.format(data['place'], data['shop']))
        print('blog_review.csv 파일 갯수는 {}입니다'.format(count))


def give_score():
    origin = 3.6
    for shop in Shop.objects.all():
        review_count = len(Review.objects.filter(shop=shop))
        shop.score = round(origin + (review_count * 0.05), 2)
        shop.save()


def check_score_data():
    origin = 3.6
    for shop in Shop.objects.all():
        review_count = len(Review.objects.filter(shop=shop))
        current_score = round(origin + (review_count * 0.05), 2)
        print(shop.title, shop.score, review_count, current_score)


if __name__ == '__main__':
    print(check_review_data('../shop_data/건대홍대강남_blog_review_181028_ansi'))