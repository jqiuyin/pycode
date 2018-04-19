# -*- coding: utf-8 -*-
from Car import Car,Battery,EleCar
my_tesla=EleCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.battery_charging(20)
my_tesla.battery.describe_battery()
my_tesla.fill_gas(5)
my_tesla.read_gas()
