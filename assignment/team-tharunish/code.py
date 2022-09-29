import random
def tempdetect(temp_value):
if temp_value>75:
 print("High Temperature")
else:
 print("Normal Temperature")
while(1):
temp_value=random.randint(40,100)
humidity_value=random.randint(0,100)
print(temp_value)
print(humidity_value)
tempdetect(temp_value)
print("\n")
