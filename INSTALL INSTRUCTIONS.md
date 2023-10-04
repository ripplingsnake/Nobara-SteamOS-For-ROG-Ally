Please follow to get the best steam experiance on your Ally, this includes TDP control, Fan control. LEDS are not controlled yet but is being worked on 

There has been alot of work done on this by none other than Glorious Eggroll the man of GEProton fame. Alot of other people have contributed and we owe them a beer!

Download https://www.balena.io/etcher/ to burn the Nobara image to USB.

https://nobaraproject.org/download-nobara/# down load Nobara for steam deck

You can chose to dual boot during the install. If given the option choose the no swap file option.

###################################################################################################




After installed do any updates it has requested, There is and update option in applications that will update the whole system.

###############################################################




To get your controller working Open Nobara package manager (Bottom left gold icon) and search for HnadyGCCS select it and apply. If you dont find it there open Konsole and Type or copy and paste the following- 


Sudo dnf install handygccs 


it will ask you if you want to install clcik yes. Now your controls are working. After a reboot

#################################################################




Fan controls-
Again open Nobara Package Manager search for asusctl, there will be two options- Ausctl and rog gui, select both and install. ROG will now be availible in your applications.
Now reboot the Ally to allow the changes to be made.
DO NOT use max tdp watts when unplugged as you will get major stutters as the battrey wont keep up with power demand!

  SET YOUR FAN CURVES TO COOL YOUR SYSTEM IF YOU PLAN ON USING MAX TDP

#######################################################################




Next we will control TDP-
Downlaod the file located here       https://1drv.ms/u/s!AryeQSxPChg1itJ6EhuvGMrpPc7Gsw?e=iD6hT9    then use the following command-




###############################################

sudo cp -f /home/marc/Downloads/steamos-priv-write /usr/bin/steamos-polkit-helpers

If this command fails then do this open your download folder to where the file is then open another window in Dolphin and click on

your root folde, at the bottom of the window left hand side then click the 3 lines(hamburger menu) navigate to-

  USR
  
  BIN
  
  STEAMOS-POLKIT-HELPERS 

  right click in this folder and open as administrator then drag the downloaded file into the folder and click yes to overwrite.
  
  
##################################################




Notes on TDP Important, the steam UI is controlled by Valve and it will show 1-15watts however this is scaled for the ally from 5-40watts, so be aware of this 15watts is full 40watts of power. 1 is 5watts! DO NOT set to max tdp if your are not plugged in! the Battrey can not handle the power draw and you will get stutters in game! 
10watts on slider is max reccomend for Battery Play.!


################################################




Copy the following command to downlaod Deckyloader and cryoutilities





DeckyLoader-

curl -L https://github.com/SteamDeckHomebrew/decky-loader/raw/main/dist/install_release.sh | sh

Cryoutilites

curl https://raw.githubusercontent.com/CryoByte33/steam-deck-utilities/main/install.sh | bash -s --




##############################################################################################

Now we will disable zram and set a 16GB swap file copy and paste these commands one at a time-



sudo touch /etc/systemd/zram-generator.conf

sudo dnf remove zram-generator-defaults

reboot

sudo dd if=/dev/zero of=/swapfile bs=1G count=16

sudo truncate -s 0 /swapfile

sudo chattr +C /swapfile

sudo dd if=/dev/zero of=/swapfile bs=1G count=16

sudo chmod 600 /swapfile

sudo mkswap /swapfile

sudo swapon /swapfile

now enter

sudo nano /etc/fstab

if there is a line that contains anything with swap in it delete the whole line then,

Add this to the end of the lines thats there,


#################################



/swapfile swap swap defaults 0 0


#################################




press cntl + O push enter to write the line in then Cntl + x so save and exit


Reboot


Now open cyroutils thats on your desktop enter your password and click apply recommened settings.



CONGRATULATIONS NOW ENJOY YOUR STEAMALLY!

Recommend display scaling set to 125 percent

Recommended APPS-

XCG for xbox gamepass full screen game streaming

Geforce now electron  for nvidia streaming





