# Generated by Django 5.0.7 on 2024-11-10 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('technology', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_name', models.CharField(max_length=100)),
                ('launch_date', models.DateTimeField()),
                ('destination', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('planned', 'Запланирован'), ('launched', 'Запущен'), ('completed', 'Завершен'), ('cancelled', 'Отменен')], max_length=50)),
                ('rocket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='technology.rocket')),
                ('satellite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='technology.satellite')),
            ],
        ),
    ]
