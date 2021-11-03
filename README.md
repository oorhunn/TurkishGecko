# This repo is for only side hustlers

- create a conifg.py that looks like this
    
        COIN_CHOICES = [('ETHUSDT'), ('BTCUSDT')]
        INTERVAL_CHOICES = [ ('15MIN'), ('1HOUR'),('4HOUR'),('1DAY')]
            class Config(object):
                API_KEY = 'aaaaaa'
                API_SECRET = 'aaaaaa'
                SECRET_KEY = '#$%^&*'
# Basic endpoints
- /dataref/
    - This endpoint can be used for download any coin data from binance.api. You can select from 
    COIN_CHOICES array.