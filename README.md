# Remember by folders

A lib that allow you to schedule reminders that will appear as desktop folders

## How to use

You have two options:

### Manually

Just click at Remember.sh file

### Automatically

#### Using linux with gnome

If you are using Linux with gnome, you can do the following shell command:

1. Go to auto-start folder `$ cd /etc/xdg/autostart`

2. Create a new remember_by_folders desktop file `$ sudo nano remember_by_folders.sh`

3. Paste this code in the file, save it, and restart your computer

[Desktop Entry]

Name=RememberByFolders

GenericName=Remember by folders

Comment=A lib that allow you to schedule reminders that will appear as desktop folders

Exec=watch -n 1 'cd "/home/admotos/Área de trabalho/Agora"; python3 ./.remember_by_folders/index.py'

Terminal=true

Type=Application

X-GNOME-Autostart-enabled=true