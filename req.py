import requests

link = "https://lemonvitaliy.amocrm.ru/oauth2/access_token"

client_id = "9bccb77b-5802-412a-b3c4-59bd63d137cf"
client_secret = "20CyR19FWdq8FzzLSwTf7aXJHbtlG8V51XmNMNEP5h44JZXrMGOwp0s9j0KoUq6q"
grant_type = "authorization_code"
code = "def502004984f46c2a2b5d08c64022a152498064daf9d804fce1743f574ddb57cd9817666c7ea174c11c68f1b3c230ed5f054d27f8aee36ac3046ddbb5cab40ae655cbc692889519538574a64e62ef4f2c08a89cd75a3e8d124f6fb2965298e8c17aa226b0628ba78567987cf4030ed0bdc562c68990c5b48405418094a564e0664fba1a908508b26114b20d50f6bd54abe49b2e393294c39b701105a6b0f04fe065e3eb5487002057696161404d12b99e9a7611eb8e97217426611cbac4d0777455c69ec15e2c4c211dcf68d1e3489362538ca13840cee31a08ff84930927326a7df2b6e7cdf2a13b45deb224cb0142646d8d9cb6af487a9d1a44629dd4ff52a07a4d5bad948ea89af8e5bc95d736f5dbb0d125d038c44885bb4892f0b9bd3c16c606182d8d74a24ecbc30ed91b2bf9b9e8493a989b7a43f1dda9d5e2fcede11443a8ab6878df20b6b9a6483385c3832fc40736f6adffc706e94a218a66e3c3c9c81d7cb2d599ef8e03d5bcf3838e1987867b788b6d3f84856531027232e18e72e987a62955796d16e01a486b609dcc8a1f7d0c41467efd2c96455427e2a4b46465f0a0937c9646591967fb500eef894265893dc8e2e538dd9d74a706f04a29b0d872423ce480f368990b6b87"
redirect_uri = "http://97fd-93-181-227-201.ngrok.io"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjQ4NWEzNGNmNjRhMjA5ZGNhZmZjNjA4ZmMyNjYzNTMzNjBiYTE5NGEwZmQ1ZWI4MWM3OGU4ZmFlZGY2NzEwZDZmZGYyMWIxNTAzMWE0OTIzIn0.eyJhdWQiOiI5YmNjYjc3Yi01ODAyLTQxMmEtYjNjNC01OWJkNjNkMTM3Y2YiLCJqdGkiOiI0ODVhMzRjZjY0YTIwOWRjYWZmYzYwOGZjMjY2MzUzMzYwYmExOTRhMGZkNWViODFjNzhlOGZhZWRmNjcxMGQ2ZmRmMjFiMTUwMzFhNDkyMyIsImlhdCI6MTYzNzA3MjI4MywibmJmIjoxNjM3MDcyMjgzLCJleHAiOjE2MzcxNTg2ODMsInN1YiI6Ijc2NDE5MTYiLCJhY2NvdW50X2lkIjoyOTgyNDkzMywic2NvcGVzIjpbInB1c2hfbm90aWZpY2F0aW9ucyIsImNybSIsIm5vdGlmaWNhdGlvbnMiXX0.EySd-EYsIP9zXmgOPMgyFBEZDotxZW9qVEpC1xAhh875GPgqUyWYFFW9KVI_KN898ztFA5hzNE40P2yiCQhVfwpnPw6g6DX5wziuYB90xPFkBZvvJhscQfOCnMZQ9Vk0f98DWFch0gQ8UtHAEHSNWIgbjRDpEbbtZRD3rhpdpNIux_OpV6snGR7nZdZI-KqMInmR-x0uHLMtgrzESpbNrCT-pmyVGFJ6fJEslK983P874COiQAnj5B9BRL9ArxOkLQfI4g9O1U1PspPwWA2M8b__dE8lcV4KmtezHXckteojsNC_xkZCWp6-xcgWNGl9L-abPFwEj9yZPcnQPx8JlA"

print('Enter your first name: ')
first_name = input()
print('Enter your last name: ')
last_name = input()
print('Enter your phone number: ')
phone_number = input()
print('Enter your email: ')
email = input()

name = first_name + ' ' + last_name

response = requests.post(link, json={'client_id': client_id,
                                     'client_secret': client_secret,
                                     'grant_type': grant_type,
                                     'code': code,
                                     'redirect_uri': redirect_uri}).text

api_link = "https://lemonvitaliy.amocrm.ru/api/v4/contacts" + "?query=" + phone_number
api_header = "Bearer " + access_token
api_response = requests.get(api_link, headers={'Authorization': api_header}).text

print('ACCESS REQUEST')
print(response)

print('API REQUEST')
print(api_response)

if api_response != "":
    print('User already exists')
    print('Updating...')
else:
    print('Creating user...')

    cr_headers = {'Content-Type': 'application/json',
              'Authorization': api_header}

    cr_json = [{
                'name': name,
                'custom_fields_values': [
                    {
                        "field_id": 617295,
                        "field_name": "Телефон",
                        "field_code": "PHONE",
                        "field_type": "multitext",
                        "values": [
                            {
                                "value": phone_number,
                                "enum_id": 315381,
                                "enum_code": "WORK"
                            }
                        ]
                    },
    {
                        "field_id": 617297,
                        "field_name": "Email",
                        "field_code": "EMAIL",
                        "field_type": "multitext",
                        "values": [
                            {
                                "value": email,
                                "enum_id": 315393,
                                "enum_code": "WORK"
                            }
                        ]
                    }
                ]
             }]


    create_request = requests.post(api_link, headers=cr_headers, json=cr_json).text

    print('CREATE REQUEST')
    print(create_request)



