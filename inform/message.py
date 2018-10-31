import re

from inform.models import Shop


def print_categories(question):
    place, categories = question.split()[0], []
    for shop in Shop.objects.filter(place=place):
        try:
            category = re.findall('(?<=>)\w+', shop.category)[-1]
        except IndexError:
            category = shop.category
        if category not in categories:
            categories.append(category)
    categories = ','.join(categories)
    return '{} 주변에는 '.format(place) + categories + '들이 있어요!!'


def print_shops(question):
    data = question.split()
    place, category = data[0], data[2]
    message = '{} 주변 {} 매장들은 다음과 같이 있어요!!'.format(place, category)
    shops = [shop for shop in Shop.objects.filter(place=place) if shop.category.endswith(category)]
    for idx, shop in enumerate(shops):
        message += '\n{}.{}'.format(idx+1, shop.title)
    print(message)
    return message
