# Generated by Django 3.0.5 on 2020-08-02 10:12

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to=utils.get_upload_path_image),
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(default='-', max_length=128, null=True),
        ),
    ]
