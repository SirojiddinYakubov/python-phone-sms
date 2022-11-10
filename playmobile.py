import os
import random

import requests

from dotenv import load_dotenv

load_dotenv('.env')

SUCCESS = 200
PROCESSING = 102
FAILED = 400
INVALID_NUMBER = 160
MESSAGE_IS_EMPTY = 170
SMS_NOT_FOUND = 404
SMS_SERVICE_NOT_TURNED = 600

PLAYMOBILE_USERNAME = os.getenv('PLAYMOBILE_USERNAME')
PLAYMOBILE_PASSWORD = os.getenv('PLAYMOBILE_PASSWORD')
PLAYMOBILE_ENDPOINT = os.getenv('PLAYMOBILE_ENDPOINT')


class SendSmsWithPlayMobile:
    def __init__(self, message, phone, username=PLAYMOBILE_USERNAME, password=PLAYMOBILE_PASSWORD,
                 endpoint=PLAYMOBILE_ENDPOINT):
        self.message = message
        self.message_id = random.randint(100000000, 999999999)
        self.phone = phone
        self.spend = None
        self.username = username
        self.password = password
        self.endpoint = endpoint

    def send(self):
        step1 = self.custom_validation()
        if step1['status'] == SUCCESS:
            message = self.clean_message(self.message)
            step2 = self.calculation_send_sms(message)
            if step2['status'] == SUCCESS:
                return self.send_message(message)
            else:
                return {'status': FAILED, 'result': step2['result']}
        else:
            return {'status': FAILED, 'result': step1['result']}

    def custom_validation(self):
        if not len(str(self.phone)) == 9:
            return {'status': FAILED, 'result': "Tel raqam kirtishda xatolik!"}
        if self.message == '' or not self.message:
            return {'status': FAILED, 'result': "Xabar matni kiritilmagan!"}

        return {'status': SUCCESS, 'result': None}

    def send_message(self, message):
        URL = self.endpoint + '/send/'
        try:
            headers = {'Content-type': 'application/json'}
            payload = {
                "messages": [
                    {
                        "recipient": "998" + str(self.phone),
                        "message-id": str(self.message_id),
                        "sms": {
                            "originator": "3700",
                            "content": {
                                "text": str(message),
                            }
                        }
                    }
                ]
            }

            r = requests.post(URL, json=payload, headers=headers,
                              auth=(self.username, self.password))

            if not r.status_code == SUCCESS:
                return {'status': FAILED,
                        'result': "Sms xizmati tomonidan xatolik yuz berganligi sababli sms jo'natilmadi!"}

            return {'status': SUCCESS, 'result': "Sms muvaffaqiyatli jo'natildi!"}

        except Exception as e:
            print(e)
            return {'status': FAILED, 'result': "Sms xizmatida tomonidan xatolik yuz berdi!"}

    def clean_message(self, message):
        print(f"Old message: {message}")
        message = message.replace('ц', 'ts').replace('ч', 'ch').replace('ю',
                                                                        'yu').replace(
            'а', 'a').replace('б', 'b').replace('қ', "q").replace('ў', "o'").replace('ғ', "g'").replace('ҳ',
                                                                                                        "h").replace(
            'х',
            "x").replace(
            'в', 'v').replace('г', 'g').replace('д', 'd').replace('е',
                                                                  'e').replace(
            'ё', 'yo').replace('ж', 'j').replace('з', 'z').replace('и', 'i').replace('й', 'y').replace('к',
                                                                                                       'k').replace(
            'л', 'l').replace('м', 'm').replace('н', 'n').replace('о', 'o').replace('п', 'p').replace('р',
                                                                                                      'r').replace(
            'с', 's').replace('т', 't').replace('у', 'u').replace('ш', 'sh').replace('щ', 'sh').replace('ф',
                                                                                                        'f').replace(
            'э', 'e').replace('ы', 'i').replace('я', 'ya').replace('ў', "o'").replace('ь', "'").replace('ъ',
                                                                                                        "'").replace(
            '’', "'").replace('“', '"').replace('”', '"').replace(',', ',').replace('.', '.').replace(':', ':')
        # filter upper
        message = message.replace('Ц', 'Ts').replace('Ч', 'Ch').replace('Ю', 'Yu').replace(
            'А', 'A').replace('Б', 'B').replace('Қ', "Q").replace('Ғ', "G'").replace('Ҳ', "H").replace('Х',
                                                                                                       "X").replace(
            'В', 'V').replace('Г', 'G').replace('Д', 'D').replace('Е',
                                                                  'E').replace(
            'Ё', 'Yo').replace('Ж', 'J').replace('З', 'Z').replace('И', 'I').replace('Й', 'Y').replace('К',
                                                                                                       'K').replace(
            'Л', 'L').replace('М', 'M').replace('Н', 'N').replace('О', 'O').replace('П', 'P').replace('Р',
                                                                                                      'R').replace(
            'С', 'S').replace('Т', 'T').replace('У', 'U').replace('Ш', 'Sh').replace('Щ', 'Sh').replace('Ф',
                                                                                                        'F').replace(
            'Э', 'E').replace('Я', 'Ya')
        print(f"Cleaned message: {message}")
        return message

    def calculation_send_sms(self, message):
        try:
            length = len(message)
            if length:
                if length >= 0 and length <= 160:
                    self.spend = 1
                elif length > 160 and length <= 306:
                    self.spend = 2
                elif length > 306 and length <= 459:
                    self.spend = 3
                elif length > 459 and length <= 612:
                    self.spend = 4
                elif length > 612 and length <= 765:
                    self.spend = 5
                elif length > 765 and length <= 918:
                    self.spend = 6
                elif length > 918 and length <= 1071:
                    self.spend = 7
                elif length > 1071 and length <= 1224:
                    self.spend = 8
                else:
                    self.spend = 30
                print(f"spend: {self.spend}")
                return {'status': SUCCESS, 'result': None}
            else:
                return {'status': FAILED, 'result': "Xabar matni kiritilmagan!"}
        except Exception as e:
            print(e)
            return {'status': FAILED, 'result': "Xatolik yuz berdi!"}


message = "Салом дунё"
phone = 919791999
playmobile_api = SendSmsWithPlayMobile(message=message, phone=phone)
r = playmobile_api.send()

print(r)
