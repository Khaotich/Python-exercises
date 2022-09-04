import requests as rq

r = rq.get('https://httpbin.org/image/jpeg')
with open('image.jpg', 'wb') as f:
    f.write(r.content)

r = rq.get('https://httpbin.org/basic-auth/khaotic/sample', auth=('khaotic', 'sample'))
print(r.json())

r = rq.post('https://httpbin.org/post', data={'username': 'Khaotic', 'password': 'sample'})
print(r.json()['form'])