from unittest import mock

from whatisthismess.processing import Processor

class TestProcessor():

    # Example of mocking our way through pasghetti code
    @mock.patch('requests.get')
    @mock.patch('other.thing')
    @mock.patch('another_thing')
    def test_run_processing(mock_thing, mock_other_thing, mock_request):
        # A whole bunch of mock bootstrapping
        pass

    @mock.patch('requests.get')
    def test_get_http_data(mock_request):
        # Test just getting the HTTP data and returning
        pass

    @mock.patch('whatisthismess.processing.Processor.get_http_data')
    def test_run_processing(mock_get_http_data):
        # We can see how run_processing uses the mock
        pass
