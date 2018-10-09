import csv

from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    road_address = models.CharField(max_length=100)
    mapX = models.CharField(max_length=20)
    mapY = models.CharField(max_length=20)


def csv_to_model(path):
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
    csv_to_model("../shop_data/konkuk_shop_info_craw.csv")