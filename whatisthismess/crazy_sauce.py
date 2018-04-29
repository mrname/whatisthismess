import smtplib


class CrazySauce():

    def __init__(self, smtp=None):
        self.smtp = smtp if smtp else smtplib.SMTP(host='localhost')

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

        self.send_email(things)

        return things

    def send_email(self, stuff, email_to='admin@test.com'):
        '''
        Just sends an email to a given address using the instance's mailer

        :param stuff: contents of email
        :type stuff: list of integers
        :param email_to: address to email to.
        :type email_to: string
        '''
        return self.smtp.sendmail(email_to, stuff)
