import requests, json
API_KEY = '9f5f00e6-d25b-482f-96b27-860e9eaeea7'


class STL_file_processor():
    def upload(self, file):
        url = 'https://api.3yourmind.com/v1/uploads'
        files = {'file': file} #open('/var/www/python/intvw_prep/3yourMind/stand.stl','rb')}
        values = {'origin': 'vimal_sample_app'}

        response = requests.post(url,
                          files=files,
                          data=values,
                          headers={'Authorization': 'ApiKey %s' % API_KEY}) 

        if response.status_code == 200:
            content = json.loads(response.content)
            if content.get('success'):
                return content.get('uuid')
        else:
            raise Exception('Couldn\'t post file')

    def get_info(self, uuid):
        url = 'https://api.3yourmind.com/v1/uploads/%s' % uuid
        response = requests.get(url, headers={'Authorization': 'ApiKey %s' % API_KEY})

        if response.status_code == 200:
            content = json.loads(response.content)
            return content
        else:
            raise Exception('Couldn\'t fetch info')

