cd ~
cd Documents/

# sudo apt install nmcli
# nmcli dev wifi
sudo apt install wpasupplicant
wpa_passphrase LAPTOP-PM moijepeux > /etc/wpa_supplicant.conf
wpa_supplicant

sudo apt install git
sudo apt install python3

git clone https://github.com/PierreMo/ADR

python3 -m pip install --upgrade pip

python3 pip install python3-venv
python3 -m venv env
source ./env/bin/activate

python3 -m pip install requests

python3 ./ADR/client.py
