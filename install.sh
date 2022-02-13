
# Database
sudo apt install mariadb-server

# Libarys for the Sensors
git clone https://github.com/Seeed-Studio/grove.py
cd grove.py
# Python2 (This command line does not provide for Raspberrypi OS 10 (Buster) >= 2020-12-02)
sudo pip install .
# Python3 
sudo pip3 install .


#grafana 
sudo apt-get install -y grafana
sudo /bin/systemctl enable grafana-server
sudo /bin/systemctl start grafana-server

# postgresql
sudo apt install postgresql