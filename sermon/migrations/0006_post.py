# Generated by Django 2.1.4 on 2019-06-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sermon', '0005_remove_event_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=3000)),
                ('photo', models.FileField(upload_to='')),
                ('author', models.CharField(max_length=30)),
                ('date', models.DateField()),
            ],
        ),
    ]