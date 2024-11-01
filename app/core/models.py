from django.db import models


class CommonMoves(models.Model):
    """ Model to add register of moves in another models. """
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    eliminado = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        abstract = True

    def __str__(self):
        if hasattr(self, 'nombre'):
            return self.nombre
        else:
            return str(self.id)
