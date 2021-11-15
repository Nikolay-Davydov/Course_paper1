import requests


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path}
        response = requests.post(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, filename)
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

    def upload_url_to_disk(self, file_params):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        try:
            response = requests.post(url=upload_url, params=file_params, headers=headers)
            response.raise_for_status()
            if response.status_code == 202:
                print("Success")
        except:
            print("При попытке загрузки фотографии на Yandex диск произошла ошибка, проверьте токен Yandex.")

    def create_folder(self, folder_name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources?path="+ folder_name
        headers = self.get_headers()
        try:
            response = requests.put(url=upload_url, headers=headers)
            response.raise_for_status()
            if response.status_code == 201:
                print("Создание папки на Yandex диске")
        except:
            print("При попытке создания папки на Yandex диск произошла ошибка, проверьте токен Yandex.")

    def is_not_exist_folder(self, folder_name):
        print("Проверка возможности создания папки")
        try:
            upload_url = "https://cloud-api.yandex.net/v1/disk/resources?path=" + folder_name
            headers = self.get_headers()
            response = requests.get(url=upload_url, headers=headers)
            check_result = response.json()
            if ('error' in check_result and check_result['error'] == 'DiskNotFoundError'):
                return True
            else:
                return False
        except:
            print("При попытке создания папки на Yandex диск произошла ошибка, проверьте токен Yandex.")
