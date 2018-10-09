import csv

from django.http import JsonResponse


def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['1.healing time', '2.developers'],
    })


def read_csv(path):
    with open(path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print(csv_reader)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print("Column names are {', '.join(row)}")
                line_count += 1
            print(line_count, row)
            line_count += 1


if __name__ == "__main__":
    read_csv("../shop_data/konkuk_shop_info_craw.csv")
