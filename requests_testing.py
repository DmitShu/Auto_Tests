import requests

latitude = '55'
longitude = '37'
res = requests.get( "http://api.open-notify.org/iss-pass.json?lat="+latitude+"&lon="+longitude)
print(res.text)