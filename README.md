These steps are the essential steps to get a beagle bone talking with a node using the bring up script node_comm_test.py. This script is intended to validate the wiring of the cape by sending and receiving a RS485 message to and from a connected node.


1) We first need to prepare a new sdcard. We do this by burning an image onto the sd card. Use the application named Etcher.io to create a new sd card. Currently using this image: https://debian.beagleboard.org/images/bone-debian-9.2-iot-armhf-2017-10-10-4gb.img.xz

Etcher can be found here: https://etcher.io/


2) Insert the new burned SD Card into a new Beagle Bone Black Wireless and connect the BBBW to your computer via USB cable

3) If the image was burned correctly, you will see a drive names BEAGLEBONE appear on your desktop. 

4) SSH VIA a terminal and type the following, the '7' in the IP address may be a 6 depending on your machine. Please check beagle bone documentation for that:

ssh debian@192.168.7.2 
debian@beaglebone:~$ sudo su

default password is: temppwd

5) Set up internet access so we can update and download code and necessary libraries and patches (skip if you have already done so) Match the wifi name with that of your network:

Setup Wifi Connection:
To Set Wifi
sudo connmanctl

connmanctl> enable wifi

connmanctl> scan wif
i
connmanctl> services
.....
Highway 1 wifi_.....
.....
connmanctl> agent on

connmanctl> connect wifi_....

Passphrase? <Enter password>

connmanctl> quit

To check IP address

sudo ifconfig -a

6) Enable UART 1 with these commands:

sudo apt-get update ; sudo apt-get install git-core 

git clone https://github.com/beagleboard/bb.org-overlays 
cd ./bb.org-overlays 

./dtc-overlay.sh 
./install.sh 




7) Edit /boot/uEnv.txt and add these lines:

##Example v4.1.x
#cape_disable=bone_capemgr.disable_partno=
cape_enable=bone_capemgr.enable_partno=BB-UART1, BB-UART2

###Overide capes with eeprom
uboot_overlay_addr0=/lib/firmware/BB-UART1-00A0.dtbo

8) reboot using:

sudo reboot

9) download the bringup test script:

git clone https://github.com/bjtman/hub_bring_up

10) install pytho serial python library:

sudo pip install pyserial

