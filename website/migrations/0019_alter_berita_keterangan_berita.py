# Generated by Django 4.2.6 on 2024-06-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_remove_berita_slug_alter_berita_gambar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='keterangan_berita',
            field=models.CharField(blank=True, choices=[('Baru', 'Baru'), ('Lama', 'Lama')], default='Baru', max_length=200, null=True),
        ),
    ]
