# Generated by Django 3.0.2 on 2020-01-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontos_turisticos', '0008_pontoturistico_aprovado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]
