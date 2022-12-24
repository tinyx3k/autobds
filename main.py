import random
import requests
import json

class Random:
    def __init__(self):
        self.number = '123456789'
        self.text = 'zxcvbnmasfghjklqwertyuiop'

    def randomPhone(self):
        result = '09'
        for i in range(8):
            result += random.choice(self.number)
        return result


class Email:
    def __init__(self):
        pass


class TempMail:
    def __init__(self, session):
        self.session = session

    def randomMail(self):
        pass

    def getOtp(self, name, regex):
        pass


class Service:
    def __init__(self, api, regex, payload, header={}):
        self.payload = payload
        self.api = api
        self.session = requests.session()
        self.session.headers = header
        self.regex = regex


    def register(self):
        # initial data

        # Register
        res = self.session.post(self.api, data=self.payload)

        if res.json()['success']:
           return True

        else:
            print('error when register')
            return False

    def verify(self):
        pass    

    def uploadPost(self):
        pass

class Upload:
    def __init__(self):
        pass


if __name__ == "__main__":
    with open('./config.json', 'r') as f:
        userData = json.load(f)

    rand = Random()

    alinhadat = {
        'api': 'https://api.alinhadat.vn/account/signup',
        'payload': {
            'step': '1',
            'fullname': userData['fullname'],
            'email': userData['email'],
            'phone': rand.randomPhone(),
            'password': userData['password'],
            'code': ''
        },
        'regex': 'r"\D(\d{6})\D", s'
    }

    sv = Service(alinhadat['api'], alinhadat['regex'], alinhadat['payload'])
    sv.register()
