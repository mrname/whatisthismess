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
