from django.urls import path
from .import views
from .views import generate_pdf, print_pdf

urlpatterns = [
    path('beranda', views.beranda, name='beranda'),
    path('', views.loginpage, name='loginpage'),
    path('logoutpage', views.logoutpage, name='logoutpage'),
    path('profil', views.profil, name='profil'),
    path('laporan', views.laporan, name='laporan'),
    path('berita', views.berita, name='berita'),
    path('hubungi-kami', views.hubungi, name='hubungi'),
    path('<slug:slug>', views.berita, name='berita'),
    path('generate_pdf/<int:laporan_id>/<int:nomor_surat>/', generate_pdf, name='generate_pdf'),
    path('print_pdf/<int:laporan_id>/<int:nomor_surat>/', print_pdf, name='print_pdf'),
    # path('laporan/<int:laporan_id>/print/<int:nomor_surat>/', generate_pdf, name='print_laporan'),
    
]
