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
        response = requests.post(url=upload_url, params=file_params, headers=headers)
        response.raise_for_status()
        if response.status_code == 202:
            print("Success")
