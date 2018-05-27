# Android-Controlled-Wireless-Outlet
Use Android:Tasker app to toggle Wireless 433Mhz Outlets on/off via RPI

First: Get a RPi setup with Raspian.
Second: Obtain "codesend" via https://github.com/timleland/rfoutlet  (tutorial from which this is based from here: https://timleland.com/wireless-power-outlets/ -- Steps 5, 7, and 8 are mandatory for this project).
Third: get python installed (make sure it is)  -- I used version 2.7.9.
Fourth: Install Tornado WebSockets "pip install tornado"   <-- www.tornadoweb.org/en/stable
Fifth: Using Tim Lelands tutorial (step 6) on obtaining 433MHz transmission codes, alter/update ServerListen.py file to fit needs. Additionally, edit the script to change which port you want to the Pi to listen on (currently listens on 7777), and the command names (if desired).
Sixth: Add the script to automatically launch on system start up  (I used /etc/rc.local)  "python ~pi/Desktop/ServerListen.py &"
 /-- Alright. The Pi is all setup --
 
 Tasker app
 First: Create a task and add 'Net Action --> HTTP Get'
 Second: Configure the task action; "Server:Port"  (this is your RPi address, Port the python server is listening on, and the command to be executed by, said python webserver).
  ex. "192.168.1.50:7777/off/"  <--  Here, "/off/" comes from the ServerListen.py file running on the RPi.
 
 Ta-Dahh! We have working Android:Tasker controlled 433MHz wireless outlets. 
