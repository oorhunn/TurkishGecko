from binance.client import Client
from config import Config

class BinanceService():
    def init_app(self, Config):
        self.Config = Config
        self.client = Client(Config.API_KEY, Config.API_SECRET)

    def get_client(self):
        if not self.client:
            self.client = Client(self.Config.API_KEY, self.Config.API_SECRET)
        return self.client

binance_service = BinanceService()
