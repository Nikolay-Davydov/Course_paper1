import requests


class VkUser:
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_foto_user(self, user_id, album, count):
        url = 'https://api.vk.com/method/photos.get'
        vk_dict = {}
        size_best = ['w', 'z', 'y', 'x', 'r', 'q', 'p', 'o', 'm', 's']
        get_foto_params = {
            'owner_id': user_id,
            'album_id': album,
            'photo_sizes': '1',
            'count': count,
            'rev': '0',
            'extended': '1'
        }
        res = requests.get(url, params={**self.params, **get_foto_params})
        foto_dict = res.json()
        items = foto_dict['response']['items']
        print("Получили словарь фото с вк")
        for foto_vk in items:
            name = str(foto_vk['likes']['count']) + '.jpg'
            if name in vk_dict.keys():
                name = str(foto_vk['date']) + '_' + name
            size_dict = {}
            for foto_size in foto_vk['sizes']:
                size_dict[foto_size['type']] = foto_size['url']
            for symbol in size_best:
                if symbol in size_dict.keys():
                    size = symbol
                    url = size_dict[symbol]
                    vk_dict[name] = {'size': size, 'url': url}
                break
        print("Создали словарь фото для яндекса")
        return vk_dict
