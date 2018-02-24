from unittest import mock

from rest_framework.test import APITestCase

class TestQuarkEndpoint(APITestCase):

    @mock.patch('whatisthismess.models.Quark.magic',
                new_callable=mock.PropertyMock)
    def test_magic_property_bubbles_up(self, mock_magic):
        '''
        No matter what, the value of Quark.magic should always bubble
        up to the endpoint.
        '''
        mock_magic.return_value = 'please work'
        res = self.client.post('/quark/', {'name': 'test', 'mystery': 'test'})

        assert res.status_code == 201
        assert res.data['magic'] == 'please work'
