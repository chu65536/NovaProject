import requests


def amocrm_request(name, phone, email):
    link = "https://lemonvitaliy.amocrm.ru/api/v4/contacts"

    f = open('../../data/accesstoken.txt', 'r')
    access_token = f.read()
    f.close()

    name = name.replace('_', ' ')
    phone_link = link + "?query=" + phone
    email_link = link + "?query=" + email
    authorization = 'Bearer ' + access_token

    # Trying to find person with that phone/email
    phone_response = requests.get(phone_link, headers={'Authorization': authorization})
    email_response = requests.get(email_link, headers={'Authorization': authorization})

    # headers for editing data and login
    req_headers = {'Content-Type': 'application/json',
                   'Authorization': authorization}

    user_id = -1
    if email_response.text != "":
        user_id = email_response.json()['_embedded']['contacts'][0]['id']
    if phone_response.text != "":
        user_id = phone_response.json()['_embedded']['contacts'][0]['id']

    # if the user already exists - editing
    if user_id != -1:
        print('User already exists')
        print('Updating...')

        up_json = [{
                    'id': user_id,
                    'name': name,
                    'custom_fields_values':
                    [
                        {
                            "field_id": 617295,
                            "field_name": "Телефон",
                            "field_code": "PHONE",
                            "field_type": "multitext",
                            "values":
                            [
                                {
                                    "value": phone,
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
                            "values":
                            [
                                {
                                    "value": email,
                                    "enum_id": 315393,
                                    "enum_code": "WORK"
                                }
                            ]
                        }
                    ]
                 }]

        update_response = requests.patch(link, headers=req_headers, json=up_json)
        if update_response.status_code == 200:
            print('User successfully updated.')
        else:
            print('Something went wrong...')

    # if the user does not exists - creating
    else:
        print('Creating user...')

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
                                    "value": phone,
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

        create_response = requests.post(link, headers=req_headers, json=cr_json)

        phone_response = requests.get(phone_link, headers={'Authorization': authorization})
        user_id = phone_response.json()['_embedded']['contacts'][0]['id']

        if create_response.status_code == 200:
            print('User successfully created.')
        else:
            print('Something went wrong...')

    # creating lead
    lead_json = [{
                    "name": "Название сделки",
                    "price": 12345,
                    "_embedded":
                    {
                        "contacts":
                        [
                            {
                                "id": user_id
                            }
                        ]
                    }
                }]

    lead_link = "https://lemonvitaliy.amocrm.ru/api/v4/leads"
    lead_response = requests.post(lead_link, headers=req_headers, json=lead_json)

    if lead_response.status_code == 200:
        print('Lead successfully created.')
    else:
        print('An error occurred')

