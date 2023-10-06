Please follow to get the best steam experiance on your Ally, this includes TDP control, Fan control. LEDS are not controlled yet but is being worked on 

There has been alot of work done on this by none other than Glorious Eggroll the man of GEProton fame. Alot of other people have contributed and we owe them a beer!


'''       Download https://www.balena.io/etcher/ to burn the Nobara image to USB.

'''       https://nobaraproject.org/download-nobara/# down load Nobara for steam deck

You can chose to dual boot during the install. If given the option choose the no swap file option.




After installed do any updates it has requested, There is a update option in applications that will update the whole system.




To get your controller working Open Nobara package manager (Bottom left gold icon) and search for HandyGCCS select it and apply. If you dont find it there, open Konsole and Type or copy and paste the following- 


'''   sudo dnf install HandyGCCS


It will ask you if you want to install click yes. Now your controls are working, after a reboot



Fan controls-
Again open Nobara Package Manager search for asusctl, there will be two options-

'''      Asusctl 

'''      rog-gui

Select both and install. ROG will now be availible in your applications.
Now reboot the Ally to allow the changes to be made.



!!!!!!!!!!!!!Notes on TDP Important!!!!!!!!!!!!!!


The steam UI is controlled by Valve and it will show 1-15 watts however this is scaled for the ally from 7-30 watts, so be aware of this.
15 watts is full 30 watts of power. 1 watt is 7watts!






Copy the following command to downlaod Deckyloader and cryoutilities



DeckyLoader-

'''         curl -L https://github.com/SteamDeckHomebrew/decky-loader/raw/main/dist/install_release.sh | sh

Cryoutilites

'''         curl https://raw.githubusercontent.com/CryoByte33/steam-deck-utilities/main/install.sh | bash -s --




Now we will disable zram and set a 16GB swap file copy and paste these commands one at a time-



'''        sudo touch /etc/systemd/zram-generator.conf

'''        sudo dnf remove zram-generator-defaults

'''        reboot

'''        sudo dd if=/dev/zero of=/swapfile bs=1G count=16
  
'''        sudo truncate -s 0 /swapfile

'''        sudo chattr +C /swapfile

'''        sudo dd if=/dev/zero of=/swapfile bs=1G count=16

'''        sudo chmod 600 /swapfile

'''        sudo mkswap /swapfile

'''        sudo swapon /swapfile

now enter

'''        sudo nano /etc/fstab

If there is a line that contains anything with the word  swap in it, delete the whole line then,

Add this to the end of the lines thats there,


'''        /swapfile swap swap defaults 0 0


'''        Press cntl + O push enter to write the line in then Cntl + x so save and exit


'''        Reboot


Now open cyroutils thats on your desktop enter your password and click apply recommened settings.



CONGRATULATIONS NOW ENJOY YOUR STEAMALLY!

EXTRA INFO

Recommend display scaling set to 125 percent

Recommended APPS-

XCG for xbox gamepass full screen game streaming

Geforce now electron  for nvidia streaming

I hope this guide has helped you!!!



