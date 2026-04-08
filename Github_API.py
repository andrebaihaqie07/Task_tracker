import urllib.request
import urllib.error
import json


class Fetch:

    def __init__(self):
        self.username = input('whats username?: ')
        self.url = f'https://api.github.com/users/{self.username}/events'
        self.text = None

    def respons(self):
        with urllib.request.urlopen(self.url) as response:
            status_code = response.status
            self.text = response.read().decode()
            print("Status code", status_code)
            print("Response Text",  self.text[:500])

    def check_data(self):
        data = json.loads(self.text)
        if isinstance(data, list):
            print("Jumlah data:", len(data))
            for event in data[:5]:
                print(event.get('type'), event.get('repo', {}).get('name'))
        else:
            print("Bukan list, kemungkinan error", data)


send = Fetch()

try:
    send.respons()
    send.check_data()
except urllib.error.HTTPError as e:
    print("HTTP Error:", e.code, e.reason)
except urllib.error.URLError as e:
    print("URL Error:", e.reason)
except Exception as e:
    print("Error:", e)
