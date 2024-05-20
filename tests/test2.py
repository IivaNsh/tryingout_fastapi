import requests



print("sending request")

files = {
    'file': open('test_file.json', 'rb'),
}

response = requests.post('http://127.0.0.1:8000/save_file', files=files)

print(response.status_code)
print(response.content)