import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '3235485028',
  'message': 'Hello world',
  'key': 'textbelt',
})
print(resp.json())