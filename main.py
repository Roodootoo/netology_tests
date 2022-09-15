import requests


class YaUploader:
    host = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token
        self.headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {self.token}'
                   }

    def create_folder(self):
        ''' Создаём папку на Яндек Диске '''
        url = f'{self.host}/v1/disk/resources'
        params = {'path': 'NewFolder', 'owerwrite': True}
        response = requests.put(url, params=params, headers=self.headers).status_code
        print(response)
        return response


if __name__ == '__main__':
    ''' Получаем токен Яндекс Полигон '''
    with open('token_ya.txt', 'r') as file_token_ya:
        token_ya = file_token_ya.read().strip()
        ya_uploader = YaUploader(token_ya).create_folder()

