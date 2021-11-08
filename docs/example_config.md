Uygulamanin calismasi icin asagidaki bir dosya olusturun:
```
# config/local.py
import os

API_KEY = "xxx"
API_SECRET = "xxxx"
SECRET_KEY = '#$%^&*'

PSG_PASSWORD = os.environ.get("PSG_PASSWORD", "password")
PSG_USER = os.environ.get("PSG_USER", "user")
PSG_HOST = os.environ.get("PSG_HOST", "localhost")
SQLALCHEMY_DATABASE_URI = f"postgresql://{PSG_USER}:{PSG_PASSWORD}@{PSG_HOST}:5432/turk_force"
SQLALCHEMY_TRACK_MODIFICATIONS = False

```