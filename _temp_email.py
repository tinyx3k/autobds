import requests

api = "https://10minutemail.net/address.api.php"

def createTempMail():
    session = requests.session()
    data = session.get(api).json()
    print(data)

    email = data['mail_get_mail']
    return email, session


def getListMail(session):
    data = session.get(api).json()
    print(data)
    listMail = data['mail_list']
    return listMail


# email, session = createTempMail()
# lm = getListMail(session)