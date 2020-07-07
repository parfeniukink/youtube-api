import requests

url = 'http://127.0.0.1:8000/api/videos/'
headers = {'Content-Type': 'application/json'}
body = """{
"tags": "coding, how to start coding"
}"""
# body = """{}"""

req = requests.get(url, headers=headers, data=body)

print(req.status_code)
print(req.text)