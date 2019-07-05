# Generated by Django 2.2.3 on 2019-07-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_fruit_grain_meat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seafood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='fruit',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='grain',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='meat',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='vegetable',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]