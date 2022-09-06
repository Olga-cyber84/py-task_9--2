import requests
# "Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем."


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = file_path.split("/")[-1]
        print(file_name)
        """Метод загружает файл на яндекс диск"""
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        print(file_name)
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload?path=" + \
            file_name + "&overwrite=true"
        print(url)
        response = requests.get(url, headers=headers)
        url_for_loading = response.json()["href"]
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json'}

        with open(file_path, 'rb') as f:
            response = requests.put(
                url_for_loading, headers=headers, files={"file": f})


if __name__ == '__main__':
    path_to_file = ""
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
