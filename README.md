# GabomaZone
My multivendor app just like LeBonCoin

# Create venv
virtualenv venv-gabomazone
source venv-gabomazone/bin/activate (Linux)
source venv-gabomazone/Script/activate (Windows)

# Install Requirements
pip install -r requirements.txt

# Small fixes to do
1) Replace 'ugettext' by 'gettext' library
2) Replace 'force_text' by 'force_str'
3) Make sure django and pillow libs versions are compatible

# Launch server (in virtualenv)
python3 manage.py runserver 8001

