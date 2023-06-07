import ccxt
import time

# Replace with your Binance API key and secret
API_KEY = 'API_KEY_HERE'
API_SECRET = 'API_SECRET_HERE'

# Initialize the Binance exchange
exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'enableRateLimit': True,
})

# Configure trading parameters
symbol = 'BTC/USDT'  # Replace with the trading pair you want to trade
amount = 0.01  # Replace with the amount you want to trade
risk_ratio = 2  # Risk management ratio (reward:lost)
stop_loss_percentage = 0.02  # Stop loss percentage
take_profit_percentage = 0.04  # Take profit percentage

# Define the triple moving average strategy
def triple_moving_average_strategy(closes, short_period, medium_period, long_period):
    sma_short = sum(closes[-short_period:]) / short_period
    sma_medium = sum(closes[-medium_period:]) / medium_period
    sma_long = sum(closes[-long_period:]) / long_period

    if sma_short > sma_medium > sma_long:
        return 'buy'
    elif sma_short < sma_medium < sma_long:
        return 'sell'
    else:
        return None

# Initialize trading variables
last_action = None
stop_loss_price = None
take_profit_price = None

# Start the trading loop
while True:
    try:
        # Fetch the latest candlesticks data
        candles = exchange.fetch_ohlcv(symbol, timeframe='1h', limit=100)
        closes = [candle[4] for candle in candles]

        # Calculate the trading decision using the triple moving average strategy
        signal = triple_moving_average_strategy(closes, 10, 50, 200)

        if signal == 'buy' and last_action != 'buy':
            # Calculate stop loss and take profit prices
            stop_loss_price = closes[-1] * (1 - stop_loss_percentage)
            take_profit_price = closes[-1] * (1 + take_profit_percentage)

            # Place the buy order
            order = exchange.create_market_buy_order(symbol, amount)

            # Store the order details
            last_action = 'buy'
            print('Buy order placed at', order['price'])

        elif signal == 'sell' and last_action != 'sell':
            # Place the sell order
            order = exchange.create_market_sell_order(symbol, amount)

            # Store the order details
            last_action = 'sell'
            print('Sell order placed at', order['price'])

        # Check if a stop loss or take profit order needs to be updated
        if last_action == 'buy' and stop_loss_price and take_profit_price:
            positions = exchange.fetch_open_orders(symbol)
            for position in positions:
                if position['side'] == 'sell' and position['type'] == 'stop_loss_limit':
                    # Update the stop loss and take profit prices
                    exchange.edit_order(position['id'], symbol, 'stop_loss_limit', 'sell', None, None, stop_loss_price)
                    exchange.edit_order(position['id'], symbol, 'take_profit_limit', 'sell', None, take_profit_price)
                    print('Stop loss and take profit updated.')

    except Exception as e:
        print('An error occurred:', str(e))

    time.sleep(3600)  # Wait for 1 hour before checking again
