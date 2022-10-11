# Behafucha - Ver 0.9.4 - For Python 3 and Wayland support
Converts English/Hebrew to Hebrew/English text

## Authors
* Ilan Shavit
* Meir Kriheli
* Moshe Wagner
* Amiad Bareli


## Install
### Debian/Ubuntu
Debian and ubuntu repositories have a very old version of ydotool (virtual
keyboard for X and Wayland display server). You need to install version 1.0:
* sudo dpkg -i ./ydotool_1.0-1_amd64.deb
* sudo dpkg -i ./behafucha_0.9.4.deb
* sudo apt install -f

#### Set the suid bit so ydotool can be run by any user:
* sudo chmod +s /usr/local/bin/ydotool

#### Install systemd service
* sudo ln -s /usr/lib/systemd/user/ydotool.service /etc/systemd/system/
* sudo systemctl daemon-reload
* sudo systemctl start ydotool
* sudo systemctl enable ydotool
* sudo systemctl status ydotool

### Arch (AUR)
 - https://aur.archlinux.org/packages/behafucha

## Usage:
   - Define a keyboard shortcut that run /usr/bin/behafucha
   - Mark the text
   - Run the keyboard shortcut

### Other distributions:
 - install.tar.gz include a script to install behafucha on non Debian\Ubuntu OS

### Creating a new version of DEB file (from git):
* sudo apt install cmake scdoc pkg-config checkinstall git
* git clone  https://github.com/ReimuNotMoe/ydotool
* cd ydotool
* mkdir build && cd build
* cmake ..
* make -j `nproc`
* sudo checkinstall --install=no
* sudo apt install ./ydotool*.deb
* Follow Debian\Ubuntu section for the following steps

