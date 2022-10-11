# Behafucha - Ver 0.9.4 - For Python 3
Converts English/Hebrew to Hebrew/English text

## Authors
* Ilan Shavit
* Meir Kriheli
* Moshe Wagner
* Amiad Bareli


## Install
### Debian/Ubuntu
* sudo dpkg -i ./ydotool-custom_1.0-1_amd64.deb
* sudo dpkg -i ./Behafucha_0.9.4.deb
* sudo apt install -f

#### Set the suid bit so ydotool can be run by any user:
* sudo chmod +s /usr/local/bin/ydotool 

#### Install systemd service
* sudo ln -s /usr/lib/systemd/user/ydotool.service /etc/systemd/system/
* sudo systemctl daemon-reload
* sudo service ydotool start

### Arch (AUR)
 - https://aur.archlinux.org/packages/behafucha

### Other distributions:
 - install.tar.gz include a script to install behafucha on non Debian\Ubuntu OS

## Usage:
   - Define a keyboard shortcut to /usr/bin/behafucha
   - Mark the text
   - Run the keyboard shortcut

## Remark:
   - Behafucha works on X and Wayland

