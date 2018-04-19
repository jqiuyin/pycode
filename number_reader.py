import json
number_reader=open('numbers.json')
numbers=json.load(number_reader)
print (numbers)
number_reader.close()