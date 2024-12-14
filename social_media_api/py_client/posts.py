import requests
from getpass import getpass
username = input("username: ")
password = getpass()
auth_endpoint = 'http://127.0.0.1:8000/log/'

auth_response = requests.post(auth_endpoint,json={'username':username,'password':password})
print(auth_response.json())

if auth_response.status_code == 200:

    token = auth_response.json()['token']
    headers = {
        "Authorization":f'Token {token}'
    }

    endpoint = 'http://127.0.0.1:8000/api/posts/'
    get_response = requests.get(endpoint,headers=headers)
    print(get_response.json())