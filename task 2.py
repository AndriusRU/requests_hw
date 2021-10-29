from pprint import pprint
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f"OAuth {self.token}"
        }

    def upload(self, file_path: str, yandex_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        self.upload_file_to_disk(disk_file_path=yandex_path, filename=file_path)
        # Функция может ничего не возвращать

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    filename = 'test.txt'
    path_to_file = 'test.txt'
    yadisk_path = 'test'
    token = ''
    uploader = YaUploader(token)
    # uploader._get_upload_link(path_to_file)
    # uploader.upload_file_to_disk(f"{yadisk_path}/{filename}", path_to_file)
    result = uploader.upload(path_to_file, f"{yadisk_path}/{filename}")
