
class Car(object):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0
        self.remain_gas=0
    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name
   
    def upgrade_odometer(self,milesage):
        if self.odometer<milesage:
            self.odometer=milesage
        else:
            print ('无法修改，请重新输入')
    def read_odometer(self):
        print(str(self.odometer))
    def fill_gas(self,gasoline):
        if gasoline>0:
            self.remain_gas+=gasoline
        else:
            print ("无法修改，请重新输入")
    def read_gas(self):
        print('还有'+str(self.remain_gas)+'的油')
        
class Battery(object):
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print('车的电池有'+str(self.battery_size)+'kwh 电量')
    def battery_charging(self,battery_level):
        self.battery_size+=battery_level
        
class EleCar(Car):
    def __init__(self,make,model,year):
        super(EleCar,self).__init__(make,model,year)
        self.battery=Battery()
    
    def fill_gas(self,gasoline):
        print('不需要要加油')
    def read_gas(self):
        print('没有油')
        
my_tesla=EleCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.battery_charging(20)
my_tesla.battery.describe_battery()
my_tesla.fill_gas(5)
my_tesla.read_gas()