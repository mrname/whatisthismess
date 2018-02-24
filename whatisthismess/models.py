from django.db import models

# Make your happy little models here
class Quark(models.Model):
    '''
    Represents a thing of choose
    '''
    mystery = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)

    @property
    def magic(self):
        '''
        Makes magic
        '''
        return 'such magic'

    @property
    def magic2(self):
        '''
        Makes more magic
        '''
        return self.mystery[1:]
