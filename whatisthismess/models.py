from django.db import models

# Make your happy little models here
class Quark(models.Model):
    '''
    Represents a thing of choose
    '''
    mystery = models.CharField(max_length=255, blank=True, null=True)

    @property
    def create_magic(self):
        return 'such magic'
