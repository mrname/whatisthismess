from copy import deepcopy

from unittest import mock

from whatisthismess.crazy_sauce import CrazySauce


class TestCrazySauce():

    def test_init_custom_smtp(self):
        '''
        We should be able to initialize and instance of CrazySauce, providing
        our own SMTP object
        '''
        sauce = CrazySauce(smtp='whatev')
        assert sauce.smtp == 'whatev'

    @mock.patch('smtplib.SMTP')
    def test_init_default_smtp(self, mock_smtp):
        '''
        If not provided, the class should create a default instance of
        smtplib.SMTP
        '''
        smtp_instance = mock.Mock()
        mock_smtp.return_value = smtp_instance
        sauce = CrazySauce()
        assert mock_smtp.called_once_with(host='localhost')
        assert sauce.smtp == smtp_instance

    def test_make_sauce(self):
        '''
        make_sauce should take a list of integers, and return the result
        multiplied by the provided secret sauce. It SHOULD NOT mutate the input
        data.
        '''
        smtp_instance = mock.Mock()
        sauce = CrazySauce(smtp=smtp_instance)

        data = [2, 4]
        # Keep this to make sure the data did not get mutated
        original_data = deepcopy(data)

        sauce_factor = 2
        expected_result = [4, 8]

        res = sauce.make_sauce(data, sauce_factor)

        assert res == expected_result

        # Ensure we did not mutate the input
        assert data == original_data
