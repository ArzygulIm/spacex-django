from django.db import models

class FlightSchedule(models.Model):
    mission_name = models.CharField(max_length=100)
    launch_date = models.DateTimeField()
    rocket = models.ForeignKey(
        'technology.Rocket',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    satellite = models.ForeignKey(
        'technology.Satellite',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ('planned', 'Запланирован'),
        ('launched', 'Запущен'),
        ('completed', 'Завершен'),
        ('cancelled', 'Отменен')
    ])

    def __str__(self):
        return f"{self.mission_name} - {self.launch_date.strftime('%Y-%m-%d %H:%M:%S')}"