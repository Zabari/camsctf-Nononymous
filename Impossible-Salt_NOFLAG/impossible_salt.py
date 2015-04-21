#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib, random
import requests as re

def salt_filename(filename):
	return hashlib.sha512((generate_salt() + filename).encode()).hexdigest()[:50]

def generate_salt():
	SALT = 'saltystuff'
	for i in range(0, 10000):
		SALT=SALT+ str(random.randint(0, 9))
	return hashlib.sha512(SALT.encode()).hexdigest()
url="http://cdn.camsctf.com/"
for x in range(100):
	thang=salt_filename("flag.txt")
	r=re.get(url+thang)
	if "{" in r.text:
		print r.text
