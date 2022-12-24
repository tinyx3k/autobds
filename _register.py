import requests
import time

apiTempMail = "https://10minutemail.net/address.api.php"

def createTempMail():
    session = requests.session()
    data = session.get(apiTempMail).json()
    # print(data)

    email = data['mail_get_mail']
    return email, session


def getListMail(session):
    data = session.get(apiTempMail).json()
    # print(data)
    listMail = data['mail_list']
    return listMail

def reg1(url='', data={}):
    email, ses = createTempMail()
    listMail = getListMail(ses)
    payload = {
        "Username": data['username'],
        "Password": data['password'],
        "ComfirmPassword": data['password'],
        "Email": email,
        "Fullname": data['fullname'],
        "CitiId": data['cityId'],
        "DistrictId": data['districtId'],
        "WardId": data['wardId'],
        "Address": "",
        "Phone":data['phone']
    }
    requests.get(url, data=payload)


def reg2(url, data):
    email, ses = createTempMail()
    payload = {
        'txtRegisterEmail': email,
        'txtRegisterFullName': data['fullname'],
        'txtRegisterNickName': data['username'],
        'txtRegisterPassword': data['password'],
        'txtRegisterConfirmPassword': data['password'],
        'txtRegisterAddress': 'Ha noi',
        'txtRegisterAddressCity': 2,
        'txtRegisterAddressDistrict': 21,
        'txtRegisterPhone': '',
        'txtRegisterMobile': data['phone'],
        'slTypeOfMembers': 1,
        'txtSecode': '73469'
    }
    print(payload)
    c = requests.post(url, data=payload)
    print(c.text)
    time.sleep(20)
    listMail = getListMail(ses)
    print(listMail)


reg2('http://123nhadat.vn/reg.html?act=reg&code=sm', {
    'fullname': 'Nguyen Van A',
    'username': 'asdfkljksdaij',
    'password': 'zxczxc@zxczxc',
    'phone': '0987387234'
})
