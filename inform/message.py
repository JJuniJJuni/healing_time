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
    return '{} 주변에는 '.format(place) + categories + '들이 있네요!!'
