from requests import Request, Session
headers={"Content-Type":"application/coffee-pot-command", "cookie":"PHPSESSID=2537527762"}
s = Session()
url="http://coffee.camsctf.com/"
#print s.get(url).text
req = Request('BREW',  url,
    headers=headers,
    data="23"
)
prepped = s.prepare_request(req)
res=s.send(prepped)
print res.text
req=Request('WHEN',  url,
    headers=headers)
prepped = s.prepare_request(req)
res=s.send(prepped)
print res.text
req = Request('GET',  url,
    headers=headers
)
prepped = s.prepare_request(req)
res=s.send(prepped)
print res.text

headers={"Content-Type":"+c70Xz/73+4riCRCllkBKm5MClqoTv7CUOJYtrS5LL8=", "cookie":"PHPSESSID=2537527762","Content-Type":"application/coffee-pot-command"}

req = Request('GET',  url,
    headers=headers,
	data="23"
)
prepped = s.prepare_request(req)
res=s.send(prepped)
print res.text

