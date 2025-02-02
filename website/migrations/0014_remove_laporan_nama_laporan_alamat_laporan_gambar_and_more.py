# Generated by Django 4.2.6 on 2024-06-13 17:38

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_laporan_tanggal_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laporan',
            name='nama',
        ),
        migrations.AddField(
            model_name='laporan',
            name='alamat',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='laporan',
            name='gambar',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[200, 200], upload_to='gambar/banner'),
        ),
        migrations.AddField(
            model_name='laporan',
            name='kamar',
            field=models.CharField(choices=[('07', 'D07'), ('08', 'D08'), ('09', 'D09'), ('10', 'D10'), ('11', 'D11'), ('12', 'D12')], default='07', max_length=10),
        ),
        migrations.AddField(
            model_name='laporan',
            name='lembaga',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='laporan',
            name='nama_santri',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='laporan',
            name='tgl_lahir',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='laporan',
            name='tmp_lahir',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='laporan',
            name='wali_asuh',
            field=models.CharField(choices=[('ust1', 'Ust Kholiurrohman'), ('ust2', 'Ust Amrozy'), ('ust3', 'Ust Yusril'), ('ust4', 'Ust Ubaidillah'), ('ust5', 'Ust Hilmy'), ('ust6', 'Ust Zubair')], default='ust1', max_length=10),
        ),
        migrations.AddField(
            model_name='laporan',
            name='wali_santri',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Santri',
        ),
    ]
