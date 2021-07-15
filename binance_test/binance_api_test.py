import json
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

from jarvix import jprint

with open('secret.json') as f:
    secret = json.load(f)

api_key = secret['api_key']
api_secret = secret['secret_key']

client = Client(api_key, api_secret)
btc_price = {'error': False}

# # client.API_URL = 'https://testnet.binance.vision/api'
#
# # get balances for all assets & some account information
# jprint(client.get_account())
#
# # get balance for a specific asset only (BTC)
# print(client.get_asset_balance(asset='BTC'))
#
# # get balances for futures account
# # print(client.futures_account_balance())
#
# # get balances for margin account
# jprint(client.get_margin_account())

# jprint(client.get_symbol_ticker(symbol="DOGEUSDT"))

####################################

# def btc_trade_history(msg):
#     """define how to process incoming WebSocket messages"""
#     if msg['e'] != 'error':
#         print(msg['c'])
#         btc_price['last'] = msg['c']
#         btc_price['bid'] = msg['b']
#         btc_price['last'] = msg['a']
#     else:
#         btc_price['error'] = True
#
#
# # init and start the WebSocket
# bsm = BinanceSocketManager(client)
# conn_key = bsm.start_symbol_ticker_socket('DOGEUSDT', btc_trade_history)
# bsm.start()
# from time import sleep
# sleep(10)
#
# # stop websocket
# bsm.stop_socket(conn_key)
#
# # properly terminate WebSocket
# reactor.stop()

#####################################x

# valid intervals - 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M

# get timestamp of earliest date data is available
timestamp = client._get_earliest_valid_timestamp('BTCUSDT', '1d')
print(timestamp)
# request historical candle (or klines) data
bars = client.get_historical_klines('BTCUSDT', '1d', timestamp, limit=1000)

print(bars)
