# Generated by Django 4.2.6 on 2024-06-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_laporan_nama_alter_laporan_tanggal_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laporan',
            name='tanggal_publish',
            field=models.DateField(null=True),
        ),
    ]