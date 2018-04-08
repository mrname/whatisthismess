import smtplib


class CrazySauce():

    def __init__(self):
        self.smtp = smtplib.SMTP(host='localhost')

    def make_sauce(self, things, sauce_factor):
        '''
        Makes sauce, returns said sauce
        '''
        for idx, thing in enumerate(things):
            stuff = thing * sauce_factor
            things[idx] = stuff

        self.smtp.sendmail('admin@test.com', stuff)

        return things
