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


Fan controls-
Open Nobara Package Manager  (3rd icon box with star, bottom left) search for asusctl, there will be two options-

'''      Asusctl 

'''      rog-gui

Select both and install. ROG will now be availible in your applications.
Now reboot the Ally to allow the changes to be made.



Set up Steampatch.
 This will allow you to use the Ally controller just like steam deck.

Open Konsole and copy and paste the following. NB this wont work on steam beta client yet but it is being worked on and will soon! 


curl -L https://github.com/jlobue10/steam-patch/raw/main/install.sh | sh



Copy the following command to downlod Deckyloader 



DeckyLoader-

'''         curl -L https://github.com/SteamDeckHomebrew/decky-loader/raw/main/dist/install_release.sh | sh



If you want to set up a 16GB swap file follow the incructions below, highly recommended!

Open Konsole and copy and paste the following one line at a time.


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

To enable Sleep with the power button

open Dolphin and navigate here

sudo nano /etc/systemd/logind.conf.d/00-handheld-power.conf

edit the file 


[Login]
HandlePowerKey=ignore
HandlePowerKeyLongPress=ignore

and change it to 


[Login]
HandlePowerKey=suspend
HandlePowerKeyLongPress=ignore

press ctrl o
Enter to make the changes
press ctrl x to exit 





CONGRATULATIONS NOW ENJOY YOUR STEAMALLY!

EXTRA INFO

Recommend display scaling set to 125 percent

Recommended APPS-

XCG for xbox gamepass full screen game streaming

Geforce now electron  for nvidia streaming

I hope this guide has helped you!!!



