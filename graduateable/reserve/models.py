from django.db import models

class Reservation(models.Model):
    time = models.CharField(max_length=5)  # 시간 (예: "09:00")
    status = models.CharField(max_length=10, choices=[('가능한', '가능한'), ('거부된', '거부된')])  # 상태
    name = models.CharField(max_length=100)  # 이름

    def __str__(self):
        return f"{self.time} - {self.status}"
