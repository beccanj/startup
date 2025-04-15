# Generated by Django 5.1.6 on 2025-04-15 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='article_images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Crops', 'Crops'), ('Livestock', 'Livestock'), ('Soil', 'Soil'), ('Pests', 'Pests'), ('SmartAgri', 'SmartAgri')], max_length=50, null=True),
        ),
    ]
