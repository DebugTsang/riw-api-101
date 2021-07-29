import requests
 
sum = 0
r = requests.get('http://192.168.0.136:5000/magic') # A
m = r.json()
print (m[0]["result"])
sum += m[0]["result"]

r = requests.get('http://192.168.0.142:5000/magic') # B
m = r.json()
print (m[0]["result"])
sum += m[0]["result"]

r = requests.get('http://192.168.0.141:5000/magic') # C
m = r.json()
print (m[0]["result"])
sum += m[0]["result"]

r = requests.get('http://192.168.0.134:5000/magic') # D
m = r.json()
print (m[0]["result"])
sum += m[0]["result"]

r = requests.get('http://192.168.0.140:5000/magic') # E
m = r.json()
print (m[0]["result"])
sum += m[0]["result"]
print("SUM")
print(sum)