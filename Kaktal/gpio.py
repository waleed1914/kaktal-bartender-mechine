import time
import os

# Define the GPIO pins for the LEDs
led_pins = [97, 98, 96, 68, 83, 87, 80, 82, 79, 97, 64, 65, 27, 86]

# Export the GPIO pins if they are not already exported
for pin in led_pins:
    if not os.path.exists('/sys/class/gpio/gpio{}/direction'.format(pin)):
        with open('/sys/class/gpio/export', 'w') as f:
            f.write(str(pin))

# Set the direction of the GPIO pins to "out"
for pin in led_pins:
    with open('/sys/class/gpio/gpio{}/direction'.format(pin), 'w') as f:
        f.write('out')

# Turn on and off each LED in a loop
while True:
    for i, pin in enumerate(led_pins):
        with open('/sys/class/gpio/gpio{}/value'.format(pin), 'w') as f:
            f.write('1')
        print('LED {} is on'.format(i+1))
        time.sleep(0.5)
    for i, pin in enumerate(led_pins):
        with open('/sys/class/gpio/gpio{}/value'.format(pin), 'w') as f:
            f.write('0')
        print('LED {} is off'.format(i+1))
        time.sleep(0.5)