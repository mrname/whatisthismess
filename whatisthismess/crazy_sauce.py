import smtplib


class CrazySauce():

    # The __init__ method below tries to connect to an SMTP server as soon as
    # you instatiate the class
    def __init__(self):
        self.smtp = smtplib.SMTP(host='localhost')

    def make_sauce(self, things, sauce_factor):
        '''
        Given a list of integers, returns the same list multipled by the
        provided sauce_factor. Note that the input data is ALSO MUTATED!

        :param things: list of integers
        :param sauce_factor: integer representing some type of magic sauce
        :returns: list of integer with magic sauce applied
        '''
        for idx, thing in enumerate(things):
            stuff = thing * sauce_factor
            things[idx] = stuff

        self.smtp.sendmail('someone-important@something-important.com', things)

        return things
