# Generated by Django 4.2.6 on 2024-07-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0033_alter_kontak_gambar_alter_kontak_no_whatsapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='laporan',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
