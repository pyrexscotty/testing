from vehicles import *

hiscar= Car('BMW','535i','saloon',4,0)
hercar=Car('Toyota','Land Cruiser','4WD',4,100)
print ('His car: '+hiscar.__str__())
print('Her car: '+hercar.__str__())

for i in range(1,11):
    hiscar.accelerate()
    hercar.decelerate()
    print(i)

print('His car:'+hiscar.__str__())
print('Her car:' +hercar.__str__())
