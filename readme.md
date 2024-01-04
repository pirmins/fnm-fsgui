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

![image](https://github.com/pirmins/fnm-fsgui/assets/49155818/72e4974d-f50c-4261-ae3e-759b355b290b)



Welcome page

![image](https://github.com/pirmins/fnm-fsgui/assets/49155818/894996ba-bd1d-4e3b-b9a5-2188e10e2283)





### Admin View

Admin Networks Panel (sees all networks allocated)

![image](https://github.com/pirmins/fnm-fsgui/assets/49155818/619f42b3-55c0-45e1-875c-645ede5d1f27)


Admin Flowspec Panel (sees all flowspec rules created)

![image](https://github.com/pirmins/fnm-fsgui/assets/49155818/a1475635-5909-45b5-96f2-b807a8ab530a)





### User View

User Networks page (sees only what networks he's been allocated)

![image](https://github.com/pirmins/fnm-fsgui/assets/49155818/4a874e3a-5b32-4ec4-baec-790de0cab820)


User Flowspec panel (sees/can create flowspec rules for his allocated networks)

![image](https://github.com/pirmins/fnm-fsgui/assets/49155818/17674455-4801-4992-a751-3c1cb5b1ccfb)



