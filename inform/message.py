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
    shops = [shop for shop in Shop.objects.filter(place=place, category__endswith=category)]
    shops = sorted(shops, key=lambda shop: shop.score, reverse=True)
    for shop in shops:
        message += "\n-{} (평점: {}/5)".format(shop.title, shop.score)
    message += '\n궁금하신 매장 이름을 입력해주세요!!'
    # print(message)
    return message


def print_shop_info(question):
    tokens = question.split()
    place, title = tokens[0], ' '.join(tokens[1:-1])
    shop = Shop.objects.get(place=place, title=title)
    message = "{place} 지역 '{title}'의 전화번호와 주소는 다음과 같아요!!" \
              "\n[전화번호]\n{telephone}" \
              "\n[지도]\n{map_url}" \
              "\n가격, 이용 시간 등의 정보는 다음 url을 참조하세요!!" \
              "\n{info_url}" \
              "\n후기 정보가 궁금하시면 '후기'라고 입력해주세요!!".format(place=shop.place,
                                                      title=shop.title,
                                                      telephone=shop.telephone,
                                                      map_url=shop.address_url,
                                                      info_url=shop.info_url)
    print(message)
    return message
