from django.db import models
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify

class Kontak(models.Model):
    nama = models.CharField(max_length=200, blank=False, null=True)
    gambar = ResizedImageField(size=[200, 200], quality=80, crop=['middle', 'center'] , upload_to='gambar/profil', blank=False, null=True, verbose_name="Gambar (1920 x 1200 pixel)")
    no_whatsapp = models.PositiveBigIntegerField(blank=True, null=True)
    nama_ig = models.CharField(max_length=200, blank=False, null=True)
    nama_fb = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=200,blank=False, null=True)
    jabatan = models.CharField(max_length=200, blank=False, null=True)
    class Meta:
        verbose_name_plural ="Kontak"


class Profil(models.Model):
    gambar = ResizedImageField(size=[200, 200], quality=80, crop=['middle', 'center'] , upload_to='gambar/profil', blank=False, null=True, verbose_name="Gambar (1920 x 1200 pixel)")
    deskripsi = models.CharField(max_length=20000, blank=False, null=True)
    class Meta:
        verbose_name_plural ="Profil"

class Slide(models.Model):
    teks_awal = models.CharField(max_length=200, blank=True, null=True)
    teks_dua = models.CharField(max_length=200, blank=True, null=True) 
    teks_tiga = models.CharField(max_length=200, blank=True, null=True)
    gambar_slide = models.ImageField(upload_to='gambar/slide', blank=False, null=True)
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural ="Slide"

class Berita(models.Model):
    judul_berita = models.CharField(max_length=200, blank=True, null=True)
    gambar = ResizedImageField(size=[800, 600], quality=80, crop=['middle', 'center'] ,upload_to='gambar/banner', blank=True, null=True)
    keterangan = models.TextField(max_length=5000, blank=True, null=True)
    tanggal_upload= models.DateField(null=True)
    class Ket(models.TextChoices):
        Baru = 'Baru', 'Baru'
        Lama = 'Lama', 'Lama'
        
    keterangan_berita = models.CharField(
        max_length=50,
        choices=Ket.choices,
        default=Ket.Baru,
    )
    class Meta:
        verbose_name_plural ="Berita"
    
class Statis(models.Model):
    alamat_kami = models.TextField(max_length=200, blank=False, null=True)
    telpon = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=200, blank=False, null=True)
    class Meta:
        verbose_name_plural ="Statis"
    
class Laporan(models.Model):
    nama_santri = models.CharField(max_length=50, blank=False, null=True)
    niup = models.PositiveBigIntegerField(blank=True, null=True)
    gambar = ResizedImageField(size=[200, 200], quality=80, crop=['middle', 'center'] , upload_to='gambar/banner', blank=False, null=True)
    wali_santri = models.CharField(max_length=50, blank=False, null=True)
    tmp_lahir = models.CharField(max_length=50, blank=False, null=True)
    tgl_lahir = models.DateField(null=True)
    alamat = models.CharField(max_length=100, blank=False, null=True)
    lembaga = models.CharField(max_length=50, blank=False, null=True)
    class Waliasuh(models.TextChoices):
        Ust1 = 'Ust Kholiurrohman', 'Ust Kholiurrohman'
        Ust2 = 'Ust Amrozy', 'Ust Amrozy'
        Ust3 = 'Ust Yusril', 'Ust Yusril'
        Ust4 = 'Ust Ubaidillah', 'Ust Ubaidillah'
        Ust5 = 'Ust Hilmy', 'Ust Hilmy'
        Ust6 = 'Ust Zubair', 'Ust Zubair'
        
    wali_asuh = models.CharField(
        max_length=50,
        choices=Waliasuh.choices,
        default=Waliasuh.Ust1,
    )
    class Kamar(models.TextChoices):
        D07 = 'D07', 'D07'
        D08 = 'D08', 'D08'
        D09 = 'D09', 'D09'
        D10 = 'D10', 'D10'
        D11 = 'D11', 'D11'
        D12 = 'D12', 'D12'

    kamar = models.CharField(
        max_length=50,
        choices=Kamar.choices,
        default=Kamar.D07,
    )
    nilai_fiqih = models.IntegerField(blank=False, null=True)
    nilai_tauhid = models.IntegerField(blank=False, null=True)
    nilai_alquran = models.IntegerField(blank=False, null=True)
    tanggal_publish= models.DateField(null=True)
    pelanggaran = models.CharField(max_length=100, blank=False, null=True)
    
    class Meta:
        verbose_name_plural ="Laporan"

    
    
    