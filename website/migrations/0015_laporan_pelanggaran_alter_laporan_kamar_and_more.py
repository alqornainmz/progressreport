# Generated by Django 4.2.6 on 2024-06-13 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_remove_laporan_nama_laporan_alamat_laporan_gambar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='laporan',
            name='pelanggaran',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='laporan',
            name='kamar',
            field=models.CharField(choices=[('D07', 'D07'), ('D08', 'D08'), ('D09', 'D09'), ('D10', 'D10'), ('D11', 'D11'), ('D12', 'D12')], default='D07', max_length=50),
        ),
        migrations.AlterField(
            model_name='laporan',
            name='wali_asuh',
            field=models.CharField(choices=[('Ust Kholiurrohman', 'Ust Kholiurrohman'), ('Ust Amrozy', 'Ust Amrozy'), ('Ust Yusril', 'Ust Yusril'), ('Ust Ubaidillah', 'Ust Ubaidillah'), ('Ust Hilmy', 'Ust Hilmy'), ('Ust Zubair', 'Ust Zubair')], default='Ust Kholiurrohman', max_length=50),
        ),
    ]
