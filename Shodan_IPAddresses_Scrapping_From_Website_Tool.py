#Python3
import requests
from bs4 import BeautifulSoup
import re
import time
from random import randint
from termcolor import colored
from colorama import init
import pyfiglet
from pyfiglet import fonts

init()
# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
Y = '\033[93m'
BOLD = '\033[1m'
END = '\033[0m'

print (colored(pyfiglet.figlet_format("Shodan IP Addresses Scrapping Tool", font="standard"), "red"))
print (G+BOLD+"By Rishabh Sharma [Follow: https://lazyhacker22.blogspot.com/]\n"+END)

regex = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
data = []

#service name
service = "rtsp"

#add your shodan cookie here
Cookie1 = 'polito="your cookie values"'

#change x value, so that request send that many times
x = 30

i = 10
while (i < x):
        
        f = open("IPaddresses.txt","a")
        headers = {
                "Host": "www.shodan.io",
                "Cookie": Cookie1,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "origin": "https://www.okcupid.com",
                "Referer": "https://www.shodan.io/search?query="+service,
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Te": "trailers",
            }
        
        url = "https://www.shodan.io/search?query="+service+"&page="+str(i)
        #url = "https://www.shodan.io/search?query="+service+"+country%3A%22US%22&page="+str(i)
        print (url)
        page = requests.get(url, headers=headers, verify=True)
        soup = BeautifulSoup(page.content, 'html.parser')
        page_body = soup.body
        text = str(page_body)
        matches = re.finditer(regex, text, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
                ips = ("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
                if ips not in data:
                        data.append(ips)
                        filtererip =  (ips)
                        print (G+"[+]"+END+filtererip)
                        f.write(filtererip)
                        f.write("\n")
                #else:
                        #print ("[-]"+ips+" exist in database....")

        i = i+1
        f.close()
        randomtime = (randint(5,30))
        print ("Sleep for "+str(randomtime)+" sec...")
        time.sleep(randomtime)
