# Generated by Django 4.2.6 on 2024-05-26 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_alamat_laporan_alamat_kami_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='laporan',
            options={},
        ),
        migrations.RenameField(
            model_name='laporan',
            old_name='telpon',
            new_name='nilai',
        ),
        migrations.RemoveField(
            model_name='laporan',
            name='alamat_kami',
        ),
        migrations.RemoveField(
            model_name='laporan',
            name='email',
        ),
    ]
