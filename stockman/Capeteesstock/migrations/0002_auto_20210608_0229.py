# Generated by Django 3.2.4 on 2021-06-08 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capeteesstock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newitem',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newitem',
            name='color',
            field=models.CharField(choices=[('blue', 'Blue'), ('green', 'Green'), ('black', 'Black'), ('yellow', 'Yellow'), ('grey', 'Grey'), ('white', 'White'), ('royal blue', 'Royal Blue'), ('orange', 'Orange'), ('pink', 'Pink'), ('navy', 'Navy'), ('purple', 'Purple'), ('red', 'Red'), ('lime', 'Lime'), ('grey melange', 'Grey Melange'), ('stone', 'Stone'), ('sky blue', 'Sky Blue'), ('maroon', 'Maroon'), ('emerald green', 'Emerald Green'), ('teal', 'Teal'), ('grey', 'Grey'), ('dark green', 'Dark Green'), ('army green', 'Army Green'), ('grass green', 'Grass Black'), ('turqouise', 'Turqouise'), ('Cerise', 'Cerise')], max_length=20),
        ),
        migrations.AlterField(
            model_name='newitem',
            name='description',
            field=models.CharField(choices=[('Tshirt145G', 'Tshirt145G'), ('Tshirt165G', 'Tshirt165G'), ('Tshirt180G', 'Tshirt180G'), ('LS.Tshirt145G', 'LS.Tshirt145G'), ('LS.Tshirt165G', 'LS.Tshirt165G'), ('LS.Tshirt180', 'LS.Tshirt180G'), ('Golfer145G', 'Golfer145G'), ('Golfer165G', 'Golfer165G'), ('Golfer180G', 'Golfer180G'), ('LS.Golfer145G', 'LS.Golfer145G'), ('LS.Golfer165G', 'LS.Golfer165G'), ('LS.Golfer180G', 'LS.Golfer180G'), ('Hoody', 'Hoody'), ('Cap', 'Cap'), ('Beanie', 'Beanie')], max_length=20),
        ),
        migrations.AlterField(
            model_name='newitem',
            name='size',
            field=models.CharField(choices=[('xs', 'Xsmall'), ('s', 'Small'), ('m', 'Medium'), ('l', 'Large'), ('xl', 'Xlarge'), ('xxl', 'XXLarge')], max_length=20),
        ),
    ]
