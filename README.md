# Restart VM from button

Simple script on how to restart a VM hosted in Synology using a button connected to a Raspberry PI

**Background**: After change back to winter time in 2021, Home Assistant VM went nuts and the only solution was to restart the Virtual Machine where it's running. Since the rest of the family lacks the technological background to do so, they were stuck till I was available to make the restart. This kept me thinking, and after a nice discussion in the Facebook group of Home Assistant, a few nice suggestions ended up in this script.

This scripts allows by pressing a physical button to restart a Virtual Machine hosted in a Synology environment.

## Synology API ##
Synology provides an API for controlling remotely the virtual machine environement, documented here:

https://global.download.synology.com/download/Document/Software/DeveloperGuide/Package/Virtualization/All/enu/Synology_Virtual_Machine_Manager_API_Guide.pdf?fbclid=IwAR14RBBd0kGSXSK9yJ1MtNvzHwh8KLcXCKdjIFxdAz-5i6-RcCVzWcJd4wQ

## Raspberry PI Config ##

Just followed some quick tutorial on how to react to a button in raspberry PI. It connects the 3.3V (Pin1) with a pull-up resistor (220R) using a normal push-button to pin 10. Check before your raspberry PI pinout to verify it's a normal GPIO pin.

![raspberry-pi-button](https://raspberrypihq.com/wp-content/uploads/2018/02/02_Push-button_bb-min.jpg)




