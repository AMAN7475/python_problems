'''The Problem: Smart Home Ecosystem
You are building the backend logic for a Smart Home application. The system needs to manage different types of smart devices connected to a central hub.

=============================================================================
Phase 1: The Parent Class (SmartDevice)
Create a base class named SmartDevice.
Attributes:
name (string) — e.g., "Living Room Light"
brand (string) — e.g., "Philips"
__is_on (boolean, private) — Should default to False.

Methods:
turn_on() — Sets __is_on to True and prints "[device name] is now ON."
turn_off() — Sets __is_on to False and prints "[device name] is now OFF."
get_status() — A getter method that returns a string indicating if the device is "ON" or "OFF".

=============================================================================
Phase 2: Inheritance & Custom Behavior
Create two child classes that inherit from SmartDevice:

SmartLight
Additional Attribute: brightness (integer, from 0 to 100, defaults to 50).
Additional Method: set_brightness(level) — Updates the brightness level. 
(If the device is currently OFF, turning up the brightness should automatically turn the device ON.)

SmartThermostat
Additional Attribute: temperature (integer, defaults to 22°C).
Additional Method: set_temperature(temp) — Updates the temperature, but only if the thermostat is currently ON. 
(If it's OFF, print a warning: "Cannot set temperature. Thermostat is powered off.")

=============================================================================
Phase 3: Putting it to the Test (Expected Output)
Write a script to test your classes:

Create a SmartLight instance named "Kitchen Bulb".
Turn it on, change its brightness to 80, and print its status.

Create a SmartThermostat instance named "Main AC".
Try to set the temperature to 24°C while it's off (it should fail).
Turn it on, set the temperature to 24°C, and print its status.

Need a hint on how to start?
To make sure the child classes properly set up the name and brand from the parent class, remember to use the super().__init__() function inside the child classes' constructors.'''



# ====================================================================
# Solution
# ====================================================================
# Phase 1: Parent Class (SmartDevice)

class SmartDevice:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        self.__is_on = False                       #device is OFF by default

    def turn_on(self):                             #Method to turn the device ON
        self.__is_on = True
        print("{} is now ON.".format(self.name))
    
    def turn_off(self):                            #Method to turn the device OFF
        self.__is_on = False
        print("{} is now OFF.".format(self.name))

    def get_status(self):                          #Method to check the status
        if self.__is_on:
            return "ON"
        else:
            return "OFF"

# =====================================================================
# Phase 2: Inheritance & Custom Behavior

# Child class - Smart Light
class SmartLight(SmartDevice):

    def __init__(self, name, brand):             #Calling the parent class constructor
        super().__init__(name, brand)
        self.brightness = 50                     #Additional attribute for SmartLight

    
    def set_brightness(self, level):             #Method to change brightness

        # Update the brightness
        self.brightness = level

        if self.get_status() == "OFF":           #If the light is OFF, automatically turn it ON
            self.turn_on()
        print("Brightness is set to {}% .".format(self.brightness))


# Child class - Smart Thermostat
class SmartThermostat(SmartDevice):

    def __init__(self, name, brand):           #Calling the parent class constructor
        super().__init__(name, brand)
        self.temperature = 22                  #Temperature attribute for thermostat


    def set_temperature(self, temp):           #Method to change temperature
        if self.get_status() == "ON":
            self.temperature = temp
            print("Temperature is set to {}°C. ".format(self.temperature))
        else:
            print("Cannot set temperature. Thermostat is powered off.")

# ============================================================================
# Phase 3: Testing


print("----------Smart Light----------")

light = SmartLight("Kitchen Bulb", "Philips")     #Create a SmartLight object
light.turn_on()                                   #Turn the light ON 
light.set_brightness(80)                          #Change brightness

print("Light Status:", light.get_status())        #Print current status


print("\n------ Smart Thermostat ------")


thermostat = SmartThermostat("Main AC", "Samsung")      #Create a SmartThermostat object
thermostat.set_temperature(24)                          #Try to change temperature while OFF
thermostat.turn_on()                                    #Turn thermostat ON
thermostat.set_temperature(24)                          #Change temperature

print("Thermostat Status:", thermostat.get_status())    #Print current status