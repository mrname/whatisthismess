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
        if self.name == 'heman':
            return 'incredible magic'
        return 'such magic'

    @property
    def magic2(self):
        '''
        Makes more magic
        '''
        if True and self.mystery == 'heyo':
            return self.mystery[1:]
        return 'nope'

    def do_awesome(self):
        return 'awesome'
