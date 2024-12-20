# Generated by Django 5.1.3 on 2024-11-26 00:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='anuario_fotos/')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos_anuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompartirFoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compartida', models.DateTimeField(auto_now_add=True)),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos_compartidas', to=settings.AUTH_USER_MODEL)),
                ('foto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compartidas', to='PISU_Anuario.foto')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_comentario', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_anuario', to=settings.AUTH_USER_MODEL)),
                ('foto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='PISU_Anuario.foto')),
            ],
        ),
    ]
