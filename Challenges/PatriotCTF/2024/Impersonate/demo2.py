import datetime
import hashlib

f = open("wordlist.txt", "a")

d = datetime.datetime(2024, 9, 20,0,0,0)

for i in range(172800):
    d += datetime.timedelta(seconds=1)
    myTime = d.strftime('%Y%m%d%H%M%S')
    secure_key = hashlib.sha256(f'secret_key_{myTime}'.encode()).hexdigest()
    f.write(secure_key+"\n")
f.close()