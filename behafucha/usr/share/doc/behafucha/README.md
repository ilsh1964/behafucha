# Behafucha - Ver 0.9.4 (support Python3, Xorg and Wayland)
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

#### Set suid bit so any user can run ydotool with root permission:
* sudo chmod +s /usr/local/bin/ydotool

#### Install systemd service
* sudo ln -s /usr/lib/systemd/user/ydotool.service /etc/systemd/system/
* sudo systemctl daemon-reload
* sudo systemctl start ydotool
* sudo systemctl enable ydotool
* sudo systemctl status ydotool

### Arch (AUR)
 - https://aur.archlinux.org/packages/behafucha

### Fedora 36, 37:
 - extract install.tar.gz
 - run install.sh

## Usage:
   - Define a keyboard shortcut that run /usr/bin/behafucha
   - Mark the text
   - Run the keyboard shortcut

## Archive: Create (from git) a new ydotool deb package:
* sudo apt install cmake scdoc pkg-config checkinstall git
* git clone  https://github.com/ReimuNotMoe/ydotool
* cd ydotool
* mkdir build && cd build
* cmake ..
* make -j `nproc`
* sudo checkinstall --install=no
* sudo apt install ./ydotool*.deb
* Follow Debian\Ubuntu section for the following steps

