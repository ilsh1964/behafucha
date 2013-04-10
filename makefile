all:

install:
	mkdir /usr/lib/Behafucha
	cp Behafucha.py /usr/lib/Behafucha
	cp behafucha /usr/bin
	cp behafucha.desktop /usr/share/applications/
	cp behafucha.png /usr/share/pixmaps/

uninstall:
	rm -fr /usr/lib/Behafucha
	rm -f /usr/bin/behafucha
	rm -f /usr/share/pixmaps/behafucha.png
	rm -f /usr/share/applications/behafucha.desktop
