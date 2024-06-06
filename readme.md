# Assuming the use of pyenv. First update it to see th elatest list
cd ~/.pyenv; git pull; cd -
pyenv install 3.10.14
pyenv local 3.10.14
python --version

git clone 
cd security
python -m venv .security
source .security/bin/activate

pip install pip --upgrade

pip install wheel

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
