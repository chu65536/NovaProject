import requests

link = "https://lemonvitaliy.amocrm.ru/oauth2/access_token"

client_id = "9bccb77b-5802-412a-b3c4-59bd63d137cf"
client_secret = "20CyR19FWdq8FzzLSwTf7aXJHbtlG8V51XmNMNEP5h44JZXrMGOwp0s9j0KoUq6q"
grant_type = "authorization_code"
code = 'def50200d6c52b0cbc087e80e7c3dfa7260f23826d59589212faf82e8b0a79e49c6723fa5d4d00a7eb10e7c8b433ee051e615fec3d25f14446a072a91e910243a8cc94ee8ac2cb16749ff843323569066ecbd71153b15dfc393a6299bca6ccdeddbc09fc12082ba6a54968aee9d67ce760b1c3cf355572af329efc2a2c476befc567ee57c4d3348002c628a7fe6108696cd206c9f8e00e71c48eb6baa0265704eaa6a336f0790e8bd1f8d60b9151d7d9ab505de68a281e8674086c8ad9ac90ac96edd66c5f78efc2eede1ce085c4c2742e3f89367c605dfee54a186a3e358627d1abddcdc4548c7a287341f747bc1855c9e41422634587db510446ffba261a80ae81331ef9c477ddf58acb727d2a39e8bec43fdc6431bf12bbe2fba39034dcb494e5cd7d9b6e1517347694b89eee9d2f29106c5c2912117dcd626fe931e356888c84d1576908971b748ec68ad668af067fb5e7f3c323860f18bffab9780dc738d1c51c8d99ba21c3a0b4163d41dd317b20ab9c74f43f6d9212fb0a3f5d7b5baa5706608380227251bfc1b46a7dceea20adcc245f83c3afa8f3769a32d55e816ee344f426646979059470943a02903b98e4bca2c269fe3b272c84ad65b15070865e80992f0c7a29628d1b78198b'
redirect_uri = "http://8589-93-181-227-201.ngrok.io"

response = requests.post(link, json={'client_id': client_id,
                                     'client_secret': client_secret,
                                     'grant_type': grant_type,
                                     'code': code,
                                     'redirect_uri': redirect_uri})

print(response.text)
