import requests

bing_url = 'https://www.bing.com/indexnow'
data = {
    'host': 'roisyl.github.io',
    'key': '505ad98d5bed469083b92703077f9750',
    'keyLocation': 'https://roisyl.github.io/505ad98d5bed469083b92703077f9750.txt',
    'urlList': [
        'https://roisyl.github.io/BUAA-SE/BUAA-OS-Lab-General/',
    ]
}

res = requests.post(bing_url, data=data)
print(res.status_code)