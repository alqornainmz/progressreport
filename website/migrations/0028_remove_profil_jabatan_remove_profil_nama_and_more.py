# Generated by Django 4.2.6 on 2024-06-20 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_remove_profil_email_remove_profil_nama_fb_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='jabatan',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='nama',
        ),
        migrations.AddField(
            model_name='profil',
            name='deskripsi',
            field=models.CharField(max_length=20000, null=True),
        ),
    ]