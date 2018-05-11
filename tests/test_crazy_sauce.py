from unittest import mock

from whatisthismess.crazy_sauce import CrazySauce


class MockedCrazySauce(CrazySauce):
    def __init__(self):
        self.smtp = mock.Mock()


class TestCrazySauce():

    def test_make_sauce(self):
        '''
        make_sauce should take a list of integers, and return the result
        multiplied by the provided secret sauce.
        '''
        sauce = MockedCrazySauce()

        data = [2, 4]

        sauce_factor = 2
        expected_result = [4, 8]

        res = sauce.make_sauce(data, sauce_factor)

        assert res == expected_result
