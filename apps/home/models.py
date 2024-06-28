from django.db import models


class RegistroTemperatura(models.Model):
    temperatura = models.FloatField()
    humedad = models.FloatField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Registro {self.id} - Temp: {self.temperatura}, Humedad: {self.humedad}"
