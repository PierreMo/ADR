cd ~
cd Documents/

echo "----- INSTALLING GIT AND PYTHON -----"
sudo apt install git
sudo apt install python3

echo "----- CLONING THE REPOSITORY -----"
git clone https://github.com/PierreMo/ADR

echo "----- INSTALLING PIP -----"
sudo apt install python3-pip -y

echo "----- INSTALLING VENV AND SETTING IT UP -----"
sudo apt install python3-venv
python3 -m venv env
source ./env/bin/activate

echo "----- CUTTING NTP -----"
# to deactivate the ntp that synchronise time
sudo timedatectl set-ntp false

echo "----- INSTALLING HARDWARE LIBs -----"
sudo apt install python3-smbus
python3 -m pip install mpu6050-raspberrypi



echo "----- RUNNING THE CLIENT PROGRAM -----"
python3 ./ADR/client/main.py
