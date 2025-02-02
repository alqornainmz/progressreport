# Generated by Django 4.2.6 on 2024-05-26 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_laoran_laporan_alter_berita_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laporan',
            old_name='alamat',
            new_name='alamat_kami',
        ),
        migrations.RenameField(
            model_name='laporan',
            old_name='nilai_alquran',
            new_name='telpon',
        ),
        migrations.RemoveField(
            model_name='laporan',
            name='lembaga',
        ),
        migrations.RemoveField(
            model_name='laporan',
            name='nama_santri',
        ),
        migrations.RemoveField(
            model_name='laporan',
            name='nilai_fiqih',
        ),
        migrations.RemoveField(
            model_name='laporan',
            name='nilai_tauhid',
        ),
        migrations.RemoveField(
            model_name='laporan',
            name='ttl',
        ),
        migrations.RemoveField(
            model_name='laporan',
            name='wali_santri',
        ),
        migrations.AddField(
            model_name='laporan',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
