# Generated manually to fix schema

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fresharrivals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fresharrivals',
            old_name='freshtitle',
            new_name='freshTitle',
        ),
        migrations.RenameField(
            model_name='fresharrivals',
            old_name='freshprice',
            new_name='freshPrice',
        ),
        migrations.RenameField(
            model_name='fresharrivals',
            old_name='freshoffer',
            new_name='freshOffer',
        ),
        migrations.AddField(
            model_name='fresharrivals',
            name='freshbestprice',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
