wget http://kdl.cc.ksosoft.com/wps-community/download/6757/wps-office_10.1.0.6757_amd64.deb
dpkg -i wps-office_10.1.0.6757_amd64.deb
add-apt-repository ppa:notepadqq-team/notepadqq -y
apt-get update -y
apt-get install notepadqq -y
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb
wget http://download.teamviewer.com/download/version_12x/teamviewer_i386.deb
dpkg -i teamviewer_i386.deb
apt install -f -y
apt install vim -y
apt install rdesktop -y
apt install nmap -y
apt install openvpn -y
apt install speedtest-cli -y
apt install gimp -y
snap install vlc -y
apt install -f -y
apt-get install gnome-tweak-tool -y
apt install playonlinux -y
apt install net-tools -y
apt update -y
apt upgrade -y
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list -y
apt-get update -y
apt-get install -y mongodb-org -y
wget https://downloads.mongodb.com/compass/mongodb-compass_1.15.1_amd64.deb
sudo dpkg -i mongodb-compass_1.15.1_amd64.deb
apt install -f -y
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
apt-add-repository "deb https://download.sublimetext.com/ apt/stable/"
apt update -y
apt install sublime-text -y
apt install nodejs -y
apt install npm -y
apt install filezilla -y
apt install git -y
snap install spotify
sudo snap install chromium
snap install vscode --classic
snap install vscode --edge
snap refresh vscode
snap install vlc
snap install remmina
snap connect remmina:avahi-observe :avahi-observe
snap connect remmina:cups-control :cups-control
snap connect remmina:mount-observe :mount-observe
snap connect remmina:password-manager-service :password-manager-service
snap install brackets --classic
apt update -y
apt upgrade -y
apt autoremove -y
reboot
