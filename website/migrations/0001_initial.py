# Generated by Django 4.2.6 on 2024-05-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_berita', models.CharField(blank=True, max_length=200, null=True)),
                ('gambar', models.ImageField(null=True, upload_to='gambar/banner')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('keterangan', models.TextField(blank=True, max_length=200, null=True)),
                ('tanggal_upload', models.DateTimeField(auto_now_add=True, null=True)),
                ('keterangan_berita', models.CharField(choices=[('Baru', 'Baru'), ('Lama', 'Lama')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kontak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('no_whatsapp', models.PositiveBigIntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('isi', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Laoran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_santri', models.TextField(max_length=200, null=True)),
                ('wali_santri', models.TextField(max_length=200, null=True)),
                ('ttl', models.TextField(max_length=200, null=True)),
                ('alamat', models.TextField(max_length=200, null=True)),
                ('lembaga', models.TextField(max_length=200, null=True)),
                ('nilai_fiqih', models.CharField(max_length=200, null=True)),
                ('nilai_tauhid', models.CharField(max_length=200, null=True)),
                ('nilai_alquran', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('keterangan', models.TextField(blank=True, max_length=200, null=True)),
                ('gambar', models.ImageField(null=True, upload_to='gambar/profil', verbose_name='Gambar (1920 x 1200 pixel)')),
                ('tanggal_upload', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teks_awal', models.CharField(blank=True, max_length=200, null=True)),
                ('teks_dua', models.CharField(blank=True, max_length=200, null=True)),
                ('teks_tiga', models.CharField(blank=True, max_length=200, null=True)),
                ('gambar_slide', models.ImageField(null=True, upload_to='gambar/slide')),
                ('aktif', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alamat_kami', models.TextField(max_length=200, null=True)),
                ('telpon', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
            ],
        ),
    ]
