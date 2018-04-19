import json
numbers=[1,2,3,4,5,6,7,8,9]
f_obj=open('numbers.json','w')
json.dump(numbers,f_obj)
f_obj.close()
