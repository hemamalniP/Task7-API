import requests

url='https://localhost:5000/user_name='
param={'name':'sri'}
ans=requests.post(url,data=param)
print(ans)
