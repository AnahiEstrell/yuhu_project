from django.db import models
from core.models import CommonMoves


class Task(CommonMoves):
    """Task in the systems"""

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    descripcion = models.CharField(max_length=255)

    class Meta:
        """Nombre de la tabla en la base de datos."""
        db_table = 'task'
