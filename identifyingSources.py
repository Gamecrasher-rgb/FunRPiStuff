import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '3235485028',
  'message': 'Test',
  'key': '6758d5f3183daa56d79695bf52c0ade7ecade142VGy0XajDboQXRhqKnrXPS1rC1',
})
print(resp.json())