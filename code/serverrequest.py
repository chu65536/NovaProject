import requests

link = 'http://5c9c-109-161-50-226.ngrok.io'  # ngrok link
link = link + '/req'

print('Enter your first name:')
first_name = input()
print('Enter your last name:')
last_name = input()
print('Enter your phone number:')
phone = input()
print('Enter your email:')
email = input()

name = first_name + '_' + last_name
phone = phone.replace('+7', '8')

link = link + '/?name=' + name + '&phone=' + phone + '&email=' + email

# request to server
response = requests.get(link)

print(response.text)
