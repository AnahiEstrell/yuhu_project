from django.db import models
from core.models import CommonMoves
from datetime import date, timedelta


def default_fecha_vencimiento():
    return date.today() + timedelta(days=1)


class Task(CommonMoves):
    """Task in the systems"""

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    descripcion = models.CharField(max_length=255)
    fecha_vencimiento = models.DateField(default=default_fecha_vencimiento)

    class Meta:
        """Nombre de la tabla en la base de datos."""
        db_table = 'task'
