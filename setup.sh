cd ~
cd Documents/

echo "----- INSTALLING GIT AND PYTHON -----"
sudo apt install git
sudo apt install python3

echo "----- CLONING THE REPOSITORY -----"
git clone https://github.com/PierreMo/ADR

echo "----- INSTALLING PIP -----"
python3 -m pip install --upgrade pip

echo "----- INSTALLING VENV AND SETTING IT UP -----"
python3 pip install python3-venv
python3 -m venv env
source ./env/bin/activate

echo "----- INSTALLING COMMUNICATIONS LIBs -----"
python3 -m pip install socket
python3 -m pip install datetime

echo "----- RUNNING THE CLIENT PROGRAM -----"
python3 ./ADR/client.py