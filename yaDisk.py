import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""

        HEADERS = {"Authorization": f'OAuth {self.token}'}
        FILE = file_path

        response = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            params={"path": FILE},
            headers=HEADERS
        )
        # print(response.status_code)
        # pprint(response.json())

        download = requests.put(response.json()['href'])

        # print(download.status_code)
        return print('Файл успешно загружен')


if __name__ == '__main__':
    uploader = YaUploader('<Your Yandex Disk token')
    result = uploader.upload('/superhero.py')
