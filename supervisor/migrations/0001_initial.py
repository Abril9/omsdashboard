# Generated by Django 3.2.8 on 2023-02-17 16:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('numero', models.IntegerField()),
                ('nombre', models.CharField(max_length=150)),
                ('materia_prima_nombre', models.CharField(max_length=150)),
                ('cantidad_area', models.IntegerField()),
                ('cantidad_deposito', models.IntegerField()),
                ('tiempo_estimado_produccion', models.DateTimeField()),
                ('tiempo_estimado_attressaggio', models.DateTimeField()),
                ('tiempo_real_produccion', models.DateTimeField()),
                ('tiempo_real_attressaggio', models.DateTimeField()),
                ('diseño', models.FileField(upload_to='pdfs_disenios')),
            ],
            options={
                'verbose_name': 'Artículo',
                'verbose_name_plural': 'Artículos',
            },
        ),
        migrations.CreateModel(
            name='Operario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre_completo', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrdenDeProduccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fecha_caducidad', models.DateField()),
                ('fecha_inicio_produccion', models.DateField()),
                ('fecha_finalizado', models.DateField()),
                ('cantidad_articulo', models.IntegerField()),
                ('maquina_asignada', models.IntegerField()),
                ('orden_cola_produccion', models.IntegerField()),
                ('articulo_a_producir', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supervisor.articulo')),
            ],
            options={
                'verbose_name': 'OPR',
                'verbose_name_plural': "OPR's",
            },
        ),
        migrations.CreateModel(
            name='Scatola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nro_scatola', models.IntegerField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('cantidad', models.IntegerField()),
                ('operario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supervisor.operario')),
                ('opr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supervisor.ordendeproduccion')),
            ],
            options={
                'verbose_name': 'Scatola',
                'verbose_name_plural': 'Scatolas',
            },
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(max_length=100)),
                ('activo_desde', models.DateTimeField()),
                ('tiempo_actual_con_articulo', models.DateTimeField()),
                ('cantidad_producidos', models.IntegerField()),
                ('operario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supervisor.operario')),
            ],
            options={
                'verbose_name': 'Máquina',
                'verbose_name_plural': 'Máquinas',
            },
        ),
        migrations.AddField(
            model_name='articulo',
            name='operario_mas_rapido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supervisor.operario'),
        ),
    ]