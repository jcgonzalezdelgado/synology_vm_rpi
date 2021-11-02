import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import requests
import json
import time

SynologyIP = "PUT-IP-FROM-SYNOLOGY" #NOT FROM HOME ASSISTANT!!!!
SynologyPort = "PUT-PORT-FROM-SYNOLOGY"
SynologyUser = "PUT-USER-FROM-SYNOLOGY"
SynologyPass = "PUT-PASSWORD-FROM-SYNOLOGY"
SynologyVMName = "PUT-NAME-OF-VM"

RaspberryPI_GPIO = 10 #CHANGE IT ACCORDINGLY

login_url = 'http://' + SynologyIP + ':' + SynologyPort + '/webapi/auth.cgi'
command_url = 'http://' + SynologyIP + ':' + SynologyPort + '/webapi/entry.cgi'

myobj_login ={'api': 'SYNO.API.Auth', 'method': 'login', 'version': '3', 'account': SynologyUser, 'passwd': SynologyPass, 'format': 'sid', 'session': 'dsm_info'}

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(RaspberryPI_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
while True: # Run forever
        if GPIO.input(RaspberryPI_GPIO) == GPIO.HIGH: #Waiting for someone to push the button
                string_response = requests.post(login_url, data = myobj_login) #LOGIN Request
                json_response = json.loads(string_response.text)
                if (json_response["success"]):
                        sid = json_response["data"]["sid"]
                        print(sid)
                        myobj_turnoff ={'api': 'SYNO.Virtualization.API.Guest.Action', 'method': 'poweroff', 'version': '1', '_sid': sid, 'guest_name': SynologyVMName}
                        myobj_turnon ={'api': 'SYNO.Virtualization.API.Guest.Action', 'method': 'poweron', 'version': '1', '_sid': sid, 'guest_name': SynologyVMName}

                        string_response = requests.post(command_url, data = myobj_turnoff) #TURN OFF REQUEST
                        json_response = json.loads(string_response.text)
                        if (json_response["success"]):
                                print("VM " + SynologyVMName + " turned off correctly. Waiting 10s to turn it on again")
                                time.sleep(10)
                                string_response = requests.post(command_url, data = myobj_turnon) #TURN ON REQUEST
                                json_response = json.loads(string_response.text)
                                if (json_response["success"]):
                                        print("VM " + SynologyVMName + " turned on again")
                                else:
                                        print("Error turning on machine")
                        else:
                                print("Error turning off machine")
                else:
                        print("Error connecting")