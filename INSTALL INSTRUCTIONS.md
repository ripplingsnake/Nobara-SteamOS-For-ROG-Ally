Please follow to get the best steam experiance on your Ally, this includes TDP control, Fan control. also gpu clock control.



'''       Download Balena etcher 

  
           
           https://www.balena.io/etcher/ to burn the Nobara image to USB.



Alternitavly use Rufus



           https://github.com/pbatard/rufus/releases/download/v4.3/rufus-4.3.exe



Download the Norara steam deck edition -


'''       https://nobaraproject.org/download-nobara/# down load Nobara for steam deck








After install do any updates.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Next open Konsole and copy and paste the following
'''       

curl -sSL https://raw.githubusercontent.com/TaitTechMedia/nobara_ally_helper/master/install.sh


This will install all the latest updates for the ROG Ally.
 You can also run this again to get latest updates in future.


If you find sleep is not working while in Gamemode?

Open konsole and type


'''      sudo systemctl enable steam-powerbuttond.service   '''

Reboot.

Copy and paste these commands into konsole





#KDE Virtual Keyboard Fix


mkdir -p ~/.config/plasma_mobile-workspace/env/ && echo -e '#!/bin/bash\nunset GTK_IM_MODULE\nunset QT_IM_MODULE' > ~/.config/plasma_mobile-workspace/env/immodule_temp_fix.sh && sh ~/.config/plasma_mobile-workspace/env/immodule_temp_fix.sh

#Fingerprint sensor power drain issue fix



sudo bash -c 'echo "ACTION==\"add\", SUBSYSTEM==\"usb\", TEST==\"power/control\", ATTR{idVendor}==\"1c7a\", ATTR{idProduct}==\"0588\", ATTR{power/control}=\"auto\"" > /etc/udev/rules.d/50-fingerprint.rules'

so automatically create those two files and for the bash script it will run in.




Please note none of this is my work and credit should go to the creators for there long hours and headaches.








CONGRATULATIONS NOW ENJOY YOUR STEAMALLY!

EXTRA INFO

Recommend display scaling set to 125 percent

Recommended APPS-

XCG for xbox gamepass full screen game streaming

Geforce now electron  for nvidia streaming

I hope this guide has helped you!!!



