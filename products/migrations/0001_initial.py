# Generated by Django 5.0.3 on 2024-04-04 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
        ('subcat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('offer', models.DecimalField(decimal_places=2, max_digits=7)),
                ('brand', models.CharField(max_length=255)),
                ('ownerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.user')),
                ('subcat', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subcat.subcat')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
