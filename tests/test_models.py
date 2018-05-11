from rest_framework.test import APITestCase

from .model_factory import QuarkFactory

class TestQuarkModel(APITestCase):
    '''
    Tests for whatisthismess.models.Quark
    '''

    def setUp(self):
        self.quark = QuarkFactory()

    def test_magic_default(self):
        '''
        Tests the default value of the 'magic' property
        '''
        assert self.quark.magic == 'such magic'

    def test_magic_heman(self):
        '''
        If the name of the quark is 'heman', the 'magic' property should
        always be 'incredible magic'
        '''
        self.quark.name = 'heman'
        assert self.quark.magic == 'incredible magic'
