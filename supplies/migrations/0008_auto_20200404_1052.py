# Generated by Django 3.0.4 on 2020-04-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0007_supplier_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='code',
            field=models.CharField(default='pbkdf2_sha256$180000$VwHAciz3JkyR$R3DFMZ7LA4ltrDFivOGzTiBratdjnncdeE8RxQ68/pA=', max_length=20),
        ),
    ]