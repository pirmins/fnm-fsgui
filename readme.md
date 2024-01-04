## Flowspec-GUI: create Flowspec rules & deploy to FNM Adv.

### Run it

Clone the git repository
```bash
git clone https://github.com/pirmins/fnm-fsgui.git
```
Create a Python virtual environment (developped with Python 3.11)
```bash
cd fsgui
python3 -m venv myenv
```

Activate the virtual environment
```bash 
. myenv/bin/activate
```

Install the dependencies from requirements.txt
```bash 
pip install -r requirements.txt
```

Define your own Fastnetmon API env. variables

```bash 
export FNM_API_ENDPOINT="http://127.0.0.1:10007"
export FNM_API_USER=admin
export FNM_API_PASSWORD=password
```

Hardcoded defaults if no ENV VARs found are:
```python
DEFAULT_API_ENDPOINT = "http://127.0.0.1:10007"
DEFAULT_API_USER = "fnmadmin"
DEFAULT_API_PASSWORD = "fnmpassword"
```

Create a Django superuser
```bash 
python3 manage.py createsuperuser
```

Start the Django app with runserver
```bash 
python3 manage.py runserver "0.0.0.0:8000"
```

## GUI

Login page

![Screenshot 2023-10-12 151459](https://github.com/pirmins/fnm-fsgui/assets/49155818/77f5a6ce-eb41-42b0-8e89-5037e5ee2cd1)





Welcome page

![Screenshot 2023-10-12 150155](https://github.com/pirmins/fnm-fsgui/assets/49155818/a7b42a4d-1a93-470c-859e-048eeb011df1)






### Admin View

Admin Networks Panel (sees all networks allocated)

![Screenshot 2023-10-12 150155](https://github.com/pirmins/fnm-fsgui/assets/49155818/81552a1f-3a84-4fda-9d75-5b1daeaf33c8)



Admin Flowspec Panel (sees all flowspec rules created)

![Screenshot 2023-10-12 151011](https://github.com/pirmins/fnm-fsgui/assets/49155818/e4bd9633-60a8-48a5-bf74-f7651de74af4)







### User View

User Networks page (sees only what networks he's been allocated)

![Screenshot 2023-10-12 150354](https://github.com/pirmins/fnm-fsgui/assets/49155818/4b598fe8-5d7b-405c-a07a-ac9b8bfa392e)




User Flowspec panel (sees/can create flowspec rules for his allocated networks)

![Screenshot 2023-10-12 150626](https://github.com/pirmins/fnm-fsgui/assets/49155818/0973872c-2343-4966-8b33-714001cc86c0)




