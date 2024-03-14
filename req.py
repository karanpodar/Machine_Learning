import requests

req = requests.get('http://localhost:8080/candidates?text=I am the begt spell cherken')

print(req.text)
print('EOF')