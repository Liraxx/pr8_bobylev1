import random
password = list('abcdefghijklmnopqrstuvwxyz')
password = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
password = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
random.shuffle(password)
password = ''.join([random.choice(password) for x in range(11)])
print (password)
