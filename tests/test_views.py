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


class TestCrazySauceEndpoint(APITestCase):

    @mock.patch('whatisthismess.crazy_sauce.CrazySauce.send_email')
    def test_post_crazy_sauce(self, mock_send_email):
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
