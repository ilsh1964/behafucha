# Behafucha - Ver 0.9.6 (support Python3, Xorg and Wayland)
Converts English/Hebrew to Hebrew/English text

## Authors
* Ilan Shavit
* Meir Kriheli
* Moshe Wagner
* Amiad Bareli

## Install
### Debian/Ubuntu
Behafucha depends on ydotool version 1.0 (a virtual keyboard that works on Xorg and Wayland display servers).
Debian\Ubuntu has a very old version of ydotool (0.18), so you need to install it manually: 

* sudo apt install xsel
* sudo dpkg -i ./ydotool_1.0-1_amd64.deb
* sudo dpkg -i ./behafucha_0.9.6.deb
* sudo chmod +s /usr/local/bin/ydotool
* sudo systemctl start ydotool
* sudo systemctl enable ydotool

### Arch (AUR) - not updated version
 - https://aur.archlinux.org/packages/behafucha

### Fedora 36, 37:
 - tar -xzf fedora_install.tar.gz
 - cd fedora_install 
 - ./install.sh

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

