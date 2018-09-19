import requests
import kinpoint
import time

USERNAME = 'jonathanrbarney'
with open ("password.txt", "r") as myfile:
    PASSWORD=myfile.readlines()

s = kinpoint.auth(USERNAME, PASSWORD)
#r = s.start_crawl(3000,'m,f','b,c,i,e,s')
r = s.get_crawl_status().json()
check = r['isDoneProcessing']
while not check:
    r = s.get_crawl_status().json()
    check = r['isDoneProcessing']
    print(f"{str(check)} {str(r['personsCrawled'])} {str(r['personCount'])}")
    time.sleep(2*60)
s.reserve_all()
print('All Done!')

