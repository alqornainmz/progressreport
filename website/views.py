from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Laporan, Berita, Profil, Kontak, Slide
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from io import BytesIO
from datetime import datetime
from zoneinfo import ZoneInfo
# from django.templatetags.static import static
# from django.conf import settings
# import os
from reportlab.lib import colors
from reportlab.platypus import Table, SimpleDocTemplate, TableStyle
# from django.db.models import Q
# from django.views import View
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
# from weasyprint import HTML


# @login_required(login_url='loginpage')
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = username).first()
        if user_obj is None :
            messages.success(request, 'Username Tidak Ditemukan')
            return redirect('loginpage')
        cocokan = authenticate(request, username=username, password=password)
        if cocokan is None :
            messages.success(request, 'Password Salah')
            return redirect('loginpage')
        if cocokan is not None :
            login(request, cocokan)
            return redirect ('beranda')
    context = {
        "judul": "Halaman Login",
    }
    return render(request, 'loginpage.html', context)

@login_required(login_url='loginpage')
def logoutpage(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url='loginpage')
def beranda(request):
    slide = Slide.objects.all()
    context = {
        "slide" : slide,
        "judul": "Halaman Beranda",
    }
    return render(request, 'beranda.html', context)

@login_required(login_url='loginpage')
def profil(request):
    profil = Profil.objects.all()
    hubungi = Kontak.objects.all()
    context = {
        "profil" : profil,
        "hubungi" : hubungi,
        "judul": "Halaman Profil",
    }
    return render(request, 'profil.html', context)

@login_required(login_url='loginpage')
def laporan(request):
    if request.POST:
        kata_kunci = request.POST['cari']
        laporan = Laporan.objects.filter(Q(niup__contains=kata_kunci) | Q(nama_santri__contains=kata_kunci))
        context = {
            "laporan" : laporan,
            "judul": "Halaman Laporan",
            "kata_kunci": kata_kunci,
        }
    else:
        laporan = Laporan.objects.all()
        context = {
            "laporan" : laporan,
            "judul": "Halaman Laporan",
            "kata_kunci": '',
        }
    return render(request, 'laporan.html', context)

# class cari(View):
#     def get(self, request):
#         query = self.request.GET.get('q')
        
#         query_list = Laporan.objects.filter(
#             Q(nama_santri=query),
#             Q(niup=query)
#         )
        
#         context = {
#             'query_list': query_list,
#         }
        
#         return render(request, 'cari.html', context)
    

@login_required(login_url='loginpage')
def berita(request):
    berita = Berita.objects.all()
    context = {
        "berita": berita,
        "judul": "Halaman Berita",
        
    }
    return render(request, 'berita.html', context)

@login_required(login_url='loginpage')
def hubungi(request):
    hubungi = Kontak.objects.all()
    context = {
        "hubungi" : hubungi,
        "judul": "Halaman hubungi",
    }
    return render(request, 'hubungi.html', context)


def terbilang(n):
    satuan = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan", "Sepuluh", "Sebelas"]
    
    if n < 12:
        return satuan[n]
    elif n < 20:
        return terbilang(n - 10) + " Belas"
    elif n < 100:
        return terbilang(n // 10) + " Puluh " + terbilang(n % 10)
    elif n < 200:
        return "Seratus " + terbilang(n - 100)
    elif n < 1000:
        return terbilang(n // 100) + " Ratus " + terbilang(n % 100)
    elif n < 2000:
        return "Seribu " + terbilang(n - 1000)
    elif n < 1000000:
        return terbilang(n // 1000) + " Ribu " + terbilang(n % 1000)
    elif n < 1000000000:
        return terbilang(n // 1000000) + " Juta " + terbilang(n % 1000000)
    elif n < 1000000000000:
        return terbilang(n // 1000000000) + " Miliar " + terbilang(n % 1000000000)
    elif n < 1000000000000000:
        return terbilang(n // 1000000000000) + " Triliun " + terbilang(n % 1000000000000)
    return "Angka terlalu besar"


def terbilang_with_decimal(number):
    number_str = str(number)
    if '.' in number_str:
        integer_part, decimal_part = number_str.split('.')
        integer_part = int(integer_part)
        decimal_part_str = decimal_part  # keep as string for iteration

        integer_text = terbilang(integer_part)
        decimal_text = ' '.join([terbilang(int(digit)) for digit in decimal_part_str])

        return f"{integer_text} Koma {decimal_text}"
    else:
        return terbilang(int(number))

def get_nilai_huruf(nilai):
    if 90 <= nilai <= 100:
        return "A"
    elif 80 <= nilai <= 89:
        return "B"
    elif 60 <= nilai <= 79:
        return "C"
    else:
        return "D"

def get_current_datetime_asia_jakarta():
    timezone = ZoneInfo('Asia/Jakarta')
    current_time = datetime.now(timezone)
    
    bulan = {
        1: "Januari",
        2: "Februari",
        3: "Maret",
        4: "April",
        5: "Mei",
        6: "Juni",
        7: "Juli",
        8: "Agustus",
        9: "September",
        10: "Oktober",
        11: "November",
        12: "Desember"
    }
    
    day = current_time.day
    month = bulan[current_time.month]
    year = current_time.year
    
    return f"{day} {month} {year}"

def get_bln_thn():
    timezone = ZoneInfo('Asia/Jakarta')
    current_time = datetime.now(timezone)
    return current_time.strftime('%m.%Y')

def generate_pdf(request, laporan_id, nomor_surat):
    # Fetch data from the database
    laporan = Laporan.objects.filter(niup=laporan_id).first()
    
    if not laporan:
        return HttpResponse("Laporan tidak ditemukan.", content_type='text/plain')

    # Create a buffer for the PDF
    buffer = BytesIO()

    # Create the PDF object, using the A4 page size
    p = canvas.Canvas(buffer, pagesize=A4)

    # Set up the header
    p.setFont("Helvetica", 14)
    p.drawCentredString(300, 800, "PONDOK PESANTREN NURUL JADID")
    p.setFont("Helvetica-Bold", 14)
    p.drawCentredString(300, 785, "BIRO KEPESANTRENAN")
    p.setFont("Helvetica", 14)
    p.drawCentredString(300, 770, "DAERAH SYEKH NAWAWI AL-BANTANI")
    p.setFont("Helvetica", 9)
    p.roundRect(65, 748, 470, 11, 5, stroke=1, fill=0)
    p.drawCentredString(300, 750, "PO BOX 1 Paiton Probolinggo 67291 Jawa Timur Telp. (0335) 771731 E-Mail : syekhnawawialbantani@gmail.com")

    # image_absolute_path = settings.STATICFILES_DIRS[0] / 'img/nj.png'
    # image_path = static('img/nj.png')
    # image_width = 80
    # image_height = 80
    # image_x = 60  # Posisi X gambar
    # image_y = 730  # Posisi Y gambar

    # image_path = os.path.join(settings.BASE_DIR, 'static', 'img', 'nj.png')
    
    # try:
    #     p.drawImage(image_path, 60, 730, width=80, height=80)
    # except Exception as e:
    #     print(f"Error: {e}")
    
    
    
    # Konversi path gambar ke path absolut
    

    
    # Draw a line under the title
    p.line(50, 740, 550, 740)

    # Set up the title
    p.setFont("Helvetica-Bold", 12)
    p.drawCentredString(300, 700, "Laporan Penilaian Hasil Belajar")
    p.line(208, 696, 391, 696)
    p.setFont("Helvetica", 12)
    p.drawCentredString(300, 685, f"NJ-F/02.01.D/A.III/00{nomor_surat}/{get_bln_thn()}")
    
    
    # Draw data details
    y_position = 650
    p.setFont("Helvetica", 12)
    p.drawString(50, y_position, f"Nama Santri: {laporan.nama_santri}")
    y_position -= 20
    p.drawString(50, y_position, f"NIUP: {laporan.niup}")
    y_position -= 20
    p.drawString(50, y_position, f"Lembaga: {laporan.lembaga}")
    
    p.drawString(350, 650, f"Nama Wali: {laporan.wali_santri}")
    p.drawString(350, 630, f"Alamat: {laporan.alamat}")
    p.drawString(350, 610, f"Kamar: {laporan.kamar}")


    # Prepare data for the table    
    data = [["No", "Mata Pelajaran", "KKM", "Angka", "Huruf", "Terbilang"]]
    data.append(["1", "Tauhid", "65", laporan.nilai_tauhid,  get_nilai_huruf(laporan.nilai_tauhid), terbilang(laporan.nilai_tauhid)])
    data.append(["2", "Fiqih", "65", laporan.nilai_fiqih, get_nilai_huruf(laporan.nilai_fiqih), terbilang(laporan.nilai_fiqih)])
    data.append(["3", "Al-Qur'an", "65", laporan.nilai_alquran, get_nilai_huruf(laporan.nilai_alquran), terbilang(laporan.nilai_alquran)])
    data.append(["Jumlah", "", "", laporan.nilai_alquran + laporan.nilai_fiqih + laporan.nilai_tauhid, "", terbilang(laporan.nilai_alquran + laporan.nilai_fiqih + laporan.nilai_tauhid)])
    data.append(["Rata - Rata", "", "", round((laporan.nilai_alquran + laporan.nilai_fiqih + laporan.nilai_tauhid ) / 3, 2), "", terbilang_with_decimal(round((laporan.nilai_alquran + laporan.nilai_fiqih + laporan.nilai_tauhid ) / 3, 2))])

    # Create the table
    table = Table(data, colWidths=[30, 100, 50, 50, 50, 220])
    
    # Apply style to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('SPAN', (3, 4), (4, 4)),
        ('SPAN', (0, 4), (2, 4)),
        ('SPAN', (0, 5), (2, 5)),
        ('SPAN', (3, 5), (4, 5)),
    ])
    table.setStyle(style)

    # Find the width and height of the table
    table.wrapOn(p, 500, 200)
    
    # Draw the table at the specified position
    table.drawOn(p, 50, y_position - 130)

    # Draw data details
    y_position = 400
    p.setFont("Helvetica", 12)
    p.drawString(50, y_position, f"Wali Santri")
    y_position -= 100
    p.drawString(50, y_position, f"(............................................)")
    
    p.drawString(420, 430, f"Diberikan di Paiton")
    p.drawString(420, 415, f"Tanggal, "+ get_current_datetime_asia_jakarta())
    p.drawString(420, 400, f"Kepala Daerah")
    p.setFont("Helvetica-Bold", 12)
    p.drawString(420, 300, f"ZUBAIR AQ.")


    # Closing the PDF object cleanly
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and return the response
    pdf = buffer.getvalue()
    buffer.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="laporan_santri_{laporan_id}.pdf"'
    # response['Content-Disposition'] = f'inline; filename="laporan_santri_{laporan_id}.pdf"'
    response.write(pdf)
    
    return response

def print_pdf(request, laporan_id, nomor_surat):
    # Fetch data from the database
    laporan = Laporan.objects.filter(niup=laporan_id).first()
    
    if not laporan:
        return HttpResponse("Laporan tidak ditemukan.", content_type='text/plain')

    # Create a buffer for the PDF
    buffer = BytesIO()

    # Create the PDF object, using the A4 page size
    p = canvas.Canvas(buffer, pagesize=A4)

    # Set up the header
    p.setFont("Helvetica", 14)
    p.drawCentredString(300, 800, "PONDOK PESANTREN NURUL JADID")
    p.setFont("Helvetica-Bold", 14)
    p.drawCentredString(300, 785, "BIRO KEPESANTRENAN")
    p.setFont("Helvetica", 14)
    p.drawCentredString(300, 770, "DAERAH SYEKH NAWAWI AL-BANTANI")
    p.setFont("Helvetica", 9)
    p.roundRect(65, 748, 470, 11, 5, stroke=1, fill=0)
    p.drawCentredString(300, 750, "PO BOX 1 Paiton Probolinggo 67291 Jawa Timur Telp. (0335) 771731 E-Mail : syekhnawawialbantani@gmail.com")

    # image_absolute_path = settings.STATICFILES_DIRS[0] / 'img/nj.png'
    # image_path = static('img/nj.png')
    # image_width = 80
    # image_height = 80
    # image_x = 60  # Posisi X gambar
    # image_y = 730  # Posisi Y gambar

    # image_path = os.path.join(settings.BASE_DIR, 'static', 'img', 'nj.png')
    
    # try:
    #     p.drawImage(image_path, 60, 730, width=80, height=80)
    # except Exception as e:
    #     print(f"Error: {e}")
    
    
    
    # Konversi path gambar ke path absolut
    

    
    # Draw a line under the title
    p.line(50, 740, 550, 740)

    # Set up the title
    p.setFont("Helvetica-Bold", 12)
    p.drawCentredString(300, 700, "Laporan Penilaian Hasil Belajar")
    p.line(208, 696, 391, 696)
    p.setFont("Helvetica", 12)
    p.drawCentredString(300, 685, f"NJ-F/02.01.D/A.III/00{nomor_surat}/{get_bln_thn()}")
    
    
    # Draw data details
    y_position = 650
    p.setFont("Helvetica", 12)
    p.drawString(50, y_position, f"Nama Santri: {laporan.nama_santri}")
    y_position -= 20
    p.drawString(50, y_position, f"NIUP: {laporan.niup}")
    y_position -= 20
    p.drawString(50, y_position, f"Lembaga: {laporan.lembaga}")
    
    p.drawString(350, 650, f"Nama Wali: {laporan.wali_santri}")
    p.drawString(350, 630, f"Alamat: {laporan.alamat}")
    p.drawString(350, 610, f"Kamar: {laporan.kamar}")


    # Prepare data for the table    
    data = [["No", "Mata Pelajaran", "KKM", "Angka", "Huruf", "Terbilang"]]
    data.append(["1", "Tauhid", "65", laporan.nilai_tauhid,  get_nilai_huruf(laporan.nilai_tauhid), terbilang(laporan.nilai_tauhid)])
    data.append(["2", "Fiqih", "65", laporan.nilai_fiqih, get_nilai_huruf(laporan.nilai_fiqih), terbilang(laporan.nilai_fiqih)])
    data.append(["3", "Al-Qur'an", "65", laporan.nilai_alquran, get_nilai_huruf(laporan.nilai_alquran), terbilang(laporan.nilai_alquran)])
    data.append(["Jumlah", "", "", laporan.nilai_alquran + laporan.nilai_fiqih + laporan.nilai_tauhid, "", terbilang(laporan.nilai_alquran + laporan.nilai_fiqih + laporan.nilai_tauhid)])
    data.append(["Rata - Rata", "", "", round((laporan.nilai_alquran + laporan.nilai_fiqih + laporan.nilai_tauhid ) / 3, 2), "", terbilang_with_decimal(round((laporan.nilai_alquran + laporan.nilai_fiqih + laporan.nilai_tauhid ) / 3, 2))])

    # Create the table
    table = Table(data, colWidths=[30, 100, 50, 50, 50, 220])
    
    # Apply style to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('SPAN', (3, 4), (4, 4)),
        ('SPAN', (0, 4), (2, 4)),
        ('SPAN', (0, 5), (2, 5)),
        ('SPAN', (3, 5), (4, 5)),
    ])
    table.setStyle(style)

    # Find the width and height of the table
    table.wrapOn(p, 500, 200)
    
    # Draw the table at the specified position
    table.drawOn(p, 50, y_position - 130)

    # Draw data details
    y_position = 400
    p.setFont("Helvetica", 12)
    p.drawString(50, y_position, f"Wali Santri")
    y_position -= 100
    p.drawString(50, y_position, f"(............................................)")
    
    p.drawString(420, 430, f"Diberikan di Paiton")
    p.drawString(420, 415, f"Tanggal, "+ get_current_datetime_asia_jakarta())
    p.drawString(420, 400, f"Kepala Daerah")
    p.setFont("Helvetica-Bold", 12)
    p.drawString(420, 300, f"ZUBAIR AQ.")


    # Closing the PDF object cleanly
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and return the response
    pdf = buffer.getvalue()
    buffer.close()
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = f'attachment; filename="laporan_santri_{laporan_id}.pdf"'
    response['Content-Disposition'] = f'inline; filename="laporan_santri_{laporan_id}.pdf"'
    response.write(pdf)
    
    return response