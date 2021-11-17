import requests

link = "https://lemonvitaliy.amocrm.ru/api/v4/leads"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjQ4NWEzNGNmNjRhMjA5ZGNhZmZjNjA4ZmMyNjYzNTMzNjBiYTE5NGEwZmQ1ZWI4MWM3OGU4ZmFlZGY2NzEwZDZmZGYyMWIxNTAzMWE0OTIzIn0.eyJhdWQiOiI5YmNjYjc3Yi01ODAyLTQxMmEtYjNjNC01OWJkNjNkMTM3Y2YiLCJqdGkiOiI0ODVhMzRjZjY0YTIwOWRjYWZmYzYwOGZjMjY2MzUzMzYwYmExOTRhMGZkNWViODFjNzhlOGZhZWRmNjcxMGQ2ZmRmMjFiMTUwMzFhNDkyMyIsImlhdCI6MTYzNzA3MjI4MywibmJmIjoxNjM3MDcyMjgzLCJleHAiOjE2MzcxNTg2ODMsInN1YiI6Ijc2NDE5MTYiLCJhY2NvdW50X2lkIjoyOTgyNDkzMywic2NvcGVzIjpbInB1c2hfbm90aWZpY2F0aW9ucyIsImNybSIsIm5vdGlmaWNhdGlvbnMiXX0.EySd-EYsIP9zXmgOPMgyFBEZDotxZW9qVEpC1xAhh875GPgqUyWYFFW9KVI_KN898ztFA5hzNE40P2yiCQhVfwpnPw6g6DX5wziuYB90xPFkBZvvJhscQfOCnMZQ9Vk0f98DWFch0gQ8UtHAEHSNWIgbjRDpEbbtZRD3rhpdpNIux_OpV6snGR7nZdZI-KqMInmR-x0uHLMtgrzESpbNrCT-pmyVGFJ6fJEslK983P874COiQAnj5B9BRL9ArxOkLQfI4g9O1U1PspPwWA2M8b__dE8lcV4KmtezHXckteojsNC_xkZCWp6-xcgWNGl9L-abPFwEj9yZPcnQPx8JlA"

authorization = 'Bearer ' + access_token

req_headers = {'Content-Type': 'application/json',
               'Authorization': authorization}

lead_json = [{
                "name": "Название сделки",
                "price": 12345,
                "_embedded": {
                    "contacts":[
                        {
                            "id": 5109037
                        }
                    ]
                }
}]


response = requests.post(link, headers=req_headers, json=lead_json)
print(response.text)