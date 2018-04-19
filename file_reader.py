reader=open(r'C:\Users\季秋赟\Desktop\pi_million_digits.txt')



"""
#writer=open('pi_digits.txt','w')
for line in reader:
	writer.write(line)
"""
pi_string=reader.read()
birthday='0210'
print(pi_string[:50])
print(pi_string[-50:])
print(len(pi_string))
if birthday in pi_string:
	print ('yes')
else:
	print ('no')
	
reader.close()
#writer.close()