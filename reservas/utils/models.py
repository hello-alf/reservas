"""Django models.utilities"""

from django.db import models


class BookingAudit(models.Model):
    """Comparte Ride base model, molde de atributos

    BookingAudit Model acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the objects was created
        + modified (DateTime): Store the last datetime the objects was modified
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.')
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was modified.')

    class Meta:
        """Meta option.
            we define the abstract attribute for the database not consider this class and model physically
        """
        abstract = True

        #Para adicionar funcionalidad extra al objeto, no para mapearla en BD proxy = true
        #proxy = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
