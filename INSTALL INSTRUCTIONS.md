Please follow to get the best steam experiance on your Ally, this includes TDP control, Fan control. gpu clock control

There has been alot of work done on this by none other than Glorious Eggroll the man of GEProton fame. Alot of other people have contributed and we owe them a beer! full props to all of them for this amazing work!


'''       Download Balena etcher 

           https://www.balena.io/etcher/ to burn the Nobara image to USB.

           or Rufus 

           https://github.com/pbatard/rufus/releases/download/v4.3/rufus-4.3.exe

           Download the Norara steam deck edition here.


'''       https://nobaraproject.org/download-nobara/# down load Nobara for steam deck

You will need a keyboard attached for install stage!

On initial boot the two special asus front keys wont work dont worry they will soon!




After installed do any updates it has requested, There is a update option in applications that will update the whole system.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Next open Konsole and copy and paste the following
'''       curl -sSL https: // raw.githubusercontent.com/
TaitTechMedia /
nobara_ally_helper/master/ install.sh sh
This will clone onto a directory and install the following
latest kernel with latest Ally updates. you can also run this again to get latest updates!
Rogue-enemy that allows the use of all thw keys and gyro.
Deckloader for steam os plug ins
PowerControl to allow TDP adjustment.
and finally, asusctl for custom fan profiles.

Please also do the following and follow the instructions, once its installed open it in your applications and click install Deamon, this will now dynamically adjust cpu performance states and use auto cpu boost when needed.

git clone https://github.com/AdnanHodzic/auto-cpufreq.git
cd auto-cpufreq && sudo ./auto-cpufreq-installer

please note none of this is my work and credit should go to the creators for there long hours and headaches.

Optional but worth it!
linux virtual keyboard are not very good however there is a fix

open doliphin browser, click on top right and then click on show hidden files.
then go to .config folder
create a folder and call it
plasma_mobile-workspace
open it and create another folder called env, again open that....

now create a new text file and delete the defualt name and use
immodule_temp_fix.sh
now open it and type the following

#!/bin/bash
unset GTK_IM_MODULE
unset QT_IM_MODULE

save it and reboot, on the bottom right there ahould be a small keyboard icon, click it , you only need to do this once.
now the keyboard will work as good as windows!


one last thing again optional, there is an issue of slow power drain while sleeping and this fixes it.

open konsole and type the following

sudo nano /etc/udev/rules.d/50-fingerprint.rules

then in the new window type or copy and paste this

ACTION=="add", SUBSYSTEM=="usb", TEST=="power/control", ATTR{idVendor}=="1c7a", ATTR{idProduct}=="0588", ATTR{power/control}="auto"

save and reboot thats it! welcome to your New steam powered rog ally! 








CONGRATULATIONS NOW ENJOY YOUR STEAMALLY!

EXTRA INFO

Recommend display scaling set to 125 percent

Recommended APPS-

XCG for xbox gamepass full screen game streaming

Geforce now electron  for nvidia streaming

I hope this guide has helped you!!!



