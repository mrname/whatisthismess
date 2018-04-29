from copy import deepcopy
from unittest import mock

from rest_framework.test import APITestCase

from whatisthismess.crazy_sauce import CrazySauce

from .model_factory import QuarkFactory

class TestQuarkEndpoint(APITestCase):

    def test_magic_property_default(self):
        '''
        Default quarks should have a magic property of 'such magic'
        '''
        quark = QuarkFactory()
        res = self.client.get('/quark/{0}/'.format(quark.pk))

        assert res.status_code == 200
        assert res.data['magic'] == 'such magic'

    def test_magic_property_heman(self):
        '''
        Heman's quarks should have a magic property of 'incredible magic'
        '''
        quark = QuarkFactory(name='heman')
        res = self.client.get('/quark/{0}/'.format(quark.pk))

        assert res.status_code == 200
        assert res.data['magic'] == 'incredible magic'

class TestCrazySauceEndpoint(APITestCase):

    def mock_sauce_init(self):
        self.smtp = mock.Mock()

    @mock.patch.object(CrazySauce, '__init__', new=mock_sauce_init)
    def test_post_crazy_sauce(self):
        '''
        A POST to crazy sauce should go through the provided array of integers,
        apply the current crazy sauce factor (it's 2 right now?) and return
        both the old sauce and the new sauce
        '''
        # Let's be simple for now and assume crazy sauce will always be two
        data = [2,4]
        expected_sauce = [4,8]

        res = self.client.post('/crazy_sauce/', data, format='json')

        assert res.status_code == 200
        assert res.data['old_sauce'] == data
        assert res.data['new_sauce'] == expected_sauce
