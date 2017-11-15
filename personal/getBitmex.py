import requests
import simplejson as json

headers = {
    'Accept' : 'application/json'
}
r = requests.get('https://www.bitmex.com/api/v1', headers=headers)
