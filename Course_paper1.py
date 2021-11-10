import json
import VKont
import Yandex

VK_VERSION = '5.131'


def file_json_dict(rezult_dict):
    with open('vk_dict.json', 'w') as outfile:
        json.dump(rezult_dict, outfile)
    print("Запись файла завершена")


ya_token = input('1. Введите токен для Яндекс диска: ')
vk_token = input('2. Введите токен Вконтакте: ')
try:
    vk_id = int(input('3. Введите id аккаунта Вкотакте: '))
    ya = Yandex.YandexDisk(token=ya_token)
    vk = VKont.VkUser(token=vk_token, version=VK_VERSION)
    rez_dict = vk.get_foto_user(vk_id, 'profile', 5)
    json_dict = []
    for key, value in rez_dict.items():
        print("загружаем фото на яндекс диск")
        params = {
            'path': 'work/'+key,
            'url': value['url']
        }
        print("добавляем информацию о файле в список для файла-результата")
        json_dict.append(
          {
              'name': key,
              'size': value['size']
          }
        )
        ya.upload_url_to_disk(params)
    print("запись в  файл-результата")
    file_json_dict(json_dict)
except ValueError:
  print("Вы не ввели id аккаунта Вкотакте")
