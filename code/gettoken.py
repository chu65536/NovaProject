import requests

link = "https://lemonvitaliy.amocrm.ru/oauth2/access_token"

client_id = "9bccb77b-5802-412a-b3c4-59bd63d137cf"
client_secret = "20CyR19FWdq8FzzLSwTf7aXJHbtlG8V51XmNMNEP5h44JZXrMGOwp0s9j0KoUq6q"
grant_type = "authorization_code"
code = ''  # insert code here
redirect_uri = "http://8589-93-181-227-201.ngrok.io"

response = requests.post(link, json={'client_id': client_id,
                                     'client_secret': client_secret,
                                     'grant_type': grant_type,
                                     'code': code,
                                     'redirect_uri': redirect_uri})

