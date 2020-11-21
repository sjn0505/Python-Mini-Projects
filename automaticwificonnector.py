import os
import sys


saved_profiles = os.popen('netsh wlan show profiles').read()    #to see all saved networks
#print(saved_profiles)
available_profiles=os.popen('netsh wlan show networks').read()  #to show available networks
#print(available_profiles)

preferred_ssid=input('Enter the preferred Wifi for your connection: ')
#print(preferred_ssid)

response = os.popen('netsh wlan disconnect').read()             #to disconnect from current network
#print(response)

if preferred_ssid not in saved_profiles:                        #checking whether its there in saved profiles/network
    print("Profile for "+preferred_ssid+" is not saved by the system")
    print("Sorry but you can't establish the connection")
    sys.exit()
else:
    print("Profile for "+preferred_ssid+" is saved in system")

while True:                                                                #to check if its currently available
    avail= os.popen('netsh wlan show networks').read()
    #sleep(3)
    if preferred_ssid in avail:
        print('Found')
        break

print('------connecting--------')
resp= os.popen('netsh wlan connect name='+'"'+preferred_ssid+'"').read()   #to connect to the network.
print(resp)

