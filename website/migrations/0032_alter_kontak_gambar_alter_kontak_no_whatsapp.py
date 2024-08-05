# Generated by Django 4.2.6 on 2024-06-23 18:04

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_laporan_niup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontak',
            name='gambar',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[600, 600], upload_to='gambar/profil', verbose_name='Gambar (1920 x 1200 pixel)'),
        ),
        migrations.AlterField(
            model_name='kontak',
            name='no_whatsapp',
            field=models.CharField(max_length=200, null=True),
        ),
    ]