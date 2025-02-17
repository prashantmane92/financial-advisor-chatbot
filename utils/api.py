import yfinance as yf
from typing import Dict, Optional

class StockAPI:
    def __init__(self):
        """Initialize the StockAPI class"""
        pass

    def get_stock_info(self, symbol: str) -> Optional[Dict]:
        """
        Fetch current stock information for a given symbol
        
        Args:
            symbol (str): Stock symbol (e.g., 'AAPL')
            
        Returns:
            dict: Stock information including current price, day's range, and volume
        """
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            
            return {
                'symbol': symbol,
                'current_price': info.get('currentPrice'),
                'day_high': info.get('dayHigh'),
                'day_low': info.get('dayLow'),
                'volume': info.get('volume'),
                'market_cap': info.get('marketCap'),
                'pe_ratio': info.get('forwardPE')
            }
        except Exception as e:
            print(f"Error fetching stock info: {e}")
            return None
