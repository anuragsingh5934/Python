# using key() method for get key value:

login_cred = {
    'sumitsinghrajpoot@gmail.com': '123@sumit',
    'aniruddhapy0098@hotmail.com': '9566756538',
    'kundan.org.nic@gmail.com': 'rajpoot1997',
    'singh.anurag5934@gmail.com': '123321@123'
}

for email in login_cred.keys():
    print(email)

# or

for email in login_cred:
    print(email)