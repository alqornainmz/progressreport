# Generated by Django 4.2.6 on 2024-06-12 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_remove_santri_tanggal_laporan_tanggal_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='laporan',
            name='nama',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='santris', to='website.santri'),
        ),
    ]