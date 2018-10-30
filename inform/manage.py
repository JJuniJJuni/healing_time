import csv

from inform.models import Shop


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


def check_review_data(path):
    saved_shops = [(shop.place, shop.title) for shop in Shop.objects.all()]
    with open(path, mode='r') as csv_file:
        for data in csv.DictReader(csv_file):
            if (data['place'], data['shop'].replace(' ', '')) in saved_shops:
                print('현재 매칭되는 Reivew 데이터는', data['place'], data['shop'])


if __name__ == '__main__':
    print(check_review_data('../shop_data/건대홍대강남_blog_review_181028_ansi'))