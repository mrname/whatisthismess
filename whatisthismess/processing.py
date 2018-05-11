import requests

# Original class
class Processor():

    def process_many_things(self):
        '''
        Process many things... send report
        '''
        res = requests.get('http://google.com/')
        # do some stuff with res

        # do many other strange computational things

        with open('results.txt', 'w') as f:
            f.write(res.data)


# Subclassing
class SMSProcessor(Processor):

    def process_many_things(self):
        res = super().process_many_things()
        # Do SMS stuff with res

# Refactored

class RefactoredProcessor():

    def get_http_data(self):
        res = requests.get('http://google.com/')
        # do other HTTP stuffs
        return res.data

    def process_many_things(self):
        data = self.get_http_data()
        # do other things

# Adding a new method for added functionality
class NewMethodProcessor():

    def send_sms(self):
        # do SMS stuff
        pass

    def process_many_things(self):
        # do stuff
        self.send_sms()
        # do the rest of the stuff
