# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:47:10 2020

@author: Aayushi Shah
"""

from client import FtxClient, FtxWebsocketClient
YOUR_API_KEY = 'YOUR_API_KEY' 
YOUR_API_SECRET = 'YOUR_API_SECRET'

# Initialise a new client called 'rest'
rest = FtxClient(api_key=YOUR_API_KEY,api_secret=YOUR_API_SECRET)

# Mention the market of interest
market_name = 'BCH-PERP' # Bitcoin Cash Perpetual Futures

# Get orderbook for that market
rest_orderbook = rest.get_orderbook(market_name)

# Initialise a new client called 'socket'
socket = FtxWebsocketClient()

# Get orderbook for that market
socket_orderbook = socket.get_orderbook(market_name)

# Prints the orderbook on REST and on Socket 
print(f'Order book on REST\n{rest_orderbook}')
print(f'Order book on Socket\n{socket_orderbook}')

# Places market order
try:
    rest.place_order(market=market_name,
                     side="buy",
                     size=0.01,
                     type='market')
except:
    print('Something went wrong while placing the order')
    
input('Press Any Key To Exit')