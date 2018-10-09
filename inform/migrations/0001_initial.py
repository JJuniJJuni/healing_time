from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('road_address', models.CharField(max_length=100)),
                ('mapX', models.CharField(max_length=20)),
                ('mapY', models.CharField(max_length=20)),
            ],
        ),
    ]
