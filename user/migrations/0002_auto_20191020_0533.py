# Generated by Django 2.2.4 on 2019-10-20 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.CharField(blank=True, choices=[('D', 'Dog'), ('C', 'Cat'), ('E', 'Etc')], max_length=1, null=True),
        ),
    ]
