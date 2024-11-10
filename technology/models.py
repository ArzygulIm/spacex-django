from django.db import models

class Rocket(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название ракеты")
    description = models.TextField(verbose_name="Описание")
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Высота (м)")
    diameter = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Диаметр (м)")
    mass = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Масса (кг)")
    stages = models.IntegerField(verbose_name="Количество ступеней")
    first_flight = models.DateField(verbose_name="Дата первого полета")
    country = models.CharField(max_length=100, verbose_name="Страна")
    image = models.ImageField(upload_to="rockets/images/", blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.name


class Satellite(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название спутника")
    description = models.TextField(verbose_name="Описание")
    mission_type = models.CharField(max_length=100, verbose_name="Тип миссии")
    launch_date = models.DateField(verbose_name="Дата запуска")
    orbit_type = models.CharField(max_length=100, verbose_name="Тип орбиты")
    rocket = models.ForeignKey(Rocket, on_delete=models.CASCADE, related_name="satellites", verbose_name="Запущена на ракете")
    image = models.ImageField(upload_to="satellites/images/", blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.name
