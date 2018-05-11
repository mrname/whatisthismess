import pytest

from unittest import mock

from whatisthismess.processing import Processor


class TestProcessor():

    # Example of mocking our way through pasghetti code
    @pytest.mark.skip('Not implemented, only stub provided')
    @mock.patch('requests.get')
    # Looks like we could be patching things forever here....
    # The mocks below are commented because they do not exist and are for
    # example purposes only
    #@mock.patch('other.thing')
    #@mock.patch('another_thing')
    def test_run_processing_many_mocks(
        mock_thing, mock_other_thing, mock_request
    ):
        # A whole bunch of mock bootstrapping
        pass

    @pytest.mark.skip('Not implemented, only stub provided')
    @mock.patch('requests.get')
    def test_get_http_data(mock_request):
        # Test just getting the HTTP data and returning
        # If the method needs to do anything else (like convert JSON), you can
        # now test it by itself
        pass

    @pytest.mark.skip('Not implemented, only stub provided')
    # The mocks below are commented because they do not exist and are for
    # example purposes only
    #@mock.patch('whatisthismess.processing.Processor.get_http_data')
    def test_run_processing(mock_get_http_data):
        # We can see how run_processing uses the mock of the method we have
        # already tested
        pass
