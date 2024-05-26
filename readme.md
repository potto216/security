cd ~/security/
source .security/bin/activate

pip install wheel

cat << "EOF" > requirements.txt
# pip install -r requirements.txt
jupyterlab
numpy
matplotlib
# https://cryptography.io/en/latest/
cryptography
# apt install libmpfr-dev libmpc-dev libgmp-dev python3-gmpy2
gmpy2
EOF

pip install -r requirements.txt


jupyter lab --generate-config
vi ~/.jupyter/jupyter_lab_config.py

## Set the Access-Control-Allow-Origin header
#
#          Use '*' to allow any origin to access your server.
#
#          Takes precedence over allow_origin_pat.
#  Default: ''
c.ServerApp.allow_origin = '*'


## The IP address the Jupyter server will listen on.
#  Default: 'localhost'
c.ServerApp.ip = '*'


jupyter lab --LabApp.token=''

# To run
cd ~/crypto/
source .crypto/bin/activate
jupyter lab --LabApp.token=''

http://192.168.242.128:8888/lab
