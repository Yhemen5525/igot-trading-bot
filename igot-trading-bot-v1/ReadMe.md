# Crypto Trading Bot

This is a simple Python script that implements a crypto trading bot using the Binance API. The bot uses the triple moving average indicator to determine buy and sell signals and incorporates risk management with a 2:1 reward-to-risk ratio and trailing stop loss.

## Prerequisites

- Python 3.x
- ccxt library: `pip install ccxt`

## Getting Started

1. Clone the repository or download the script file: `crypto_trading_bot.py`
2. Install the required dependencies: `pip install ccxt`
3. Open the `crypto_trading_bot.py` file in a text editor.
4. Replace the placeholders `API_KEY` and `API_SECRET` with your Binance API credentials.
5. Configure the trading parameters as needed: symbol, amount, risk ratio, stop loss percentage, and take profit percentage.
6. Save the changes to the file.

## Usage

To run the script, open a terminal or command prompt and navigate to the directory where the `crypto_trading_bot.py` file is located. Then execute the following command:


The bot will start running and monitor the market for trading opportunities based on the triple moving average strategy. It will place buy and sell orders on the configured trading pair using the specified risk management and trailing stop loss.

## Important Notes

- This script is provided as a starting point and should be thoroughly tested and customized before using it with real funds.
- Trading bots involve risks, and it's essential to have a good understanding of trading strategies, risk management, and API interactions.
- Use this script responsibly and at your own risk. The author and contributors are not responsible for any financial losses incurred.
- Ensure that you have adequate knowledge and experience in trading and cryptocurrency markets before using this script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
