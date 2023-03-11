import os

os.system('echo 505 | sudo tee /sys/class/gpio/export > /dev/null  2> /dev/null')
os.system('echo 506 | sudo tee /sys/class/gpio/export > /dev/null  2> /dev/null')

os.system('echo in | sudo tee /sys/class/gpio/gpio505/direction > /dev/null  2> /dev/null')
os.system('echo out | sudo tee /sys/class/gpio/gpio506/direction > /dev/null  2> /dev/null')

gpio506 = os.popen('cat /sys/class/gpio/gpio506/value').read()
gpio505 = os.popen('cat /sys/class/gpio/gpio505/value').read()

print('gpio506: ' + gpio506)
print('gpio505: ' + gpio505)

os.system('echo 0 | sudo tee /sys/class/gpio/gpio506/value > /dev/null  2> /dev/null')

gpio506 = os.popen('cat /sys/class/gpio/gpio506/value').read()
gpio505 = os.popen('cat /sys/class/gpio/gpio505/value').read()

print('gpio506: ' + gpio506)
print('gpio505: ' + gpio505)
print(str(int(gpio505)+int(gpio506)))


os.system('echo 1 | sudo tee /sys/class/gpio/gpio506/value  > /dev/null  2> /dev/null')

gpio506 = os.popen('cat /sys/class/gpio/gpio506/value').read()
gpio505 = os.popen('cat /sys/class/gpio/gpio505/value').read()

print('gpio506: ' + gpio506)
print('gpio505: ' + gpio505)
print(str(int(gpio505)+int(gpio506)))

os.system('echo 505 | sudo tee /sys/class/gpio/unexport > /dev/null  2> /dev/null')
os.system('echo 506 | sudo tee /sys/class/gpio/unexport > /dev/null  2> /dev/null')