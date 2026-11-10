import yfinance as yf
import matplotlib.pyplot as plt

def analyze_stock(ticker_symbol):
    """
    Downloads historical stock data, calculates the 5-day moving average,
    and visualizes the price trend.
    """
    print(f"Downloading data for {ticker_symbol}...")
    
    # Download 1 month of daily data (auto_adjust=False to avoid warning)
    data = yf.download(ticker_symbol, period="1mo", interval="1d", auto_adjust=False)
    
    # Calculate the 5-day moving average
    data['MA5'] = data['Close'].rolling(window=5).mean()
    
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['MA5'], label='5-Day MA', color='orange', linestyle='--')
    plt.title(f'{ticker_symbol} Price & 5-Day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Show the plot
    plt.show()
    
    print("Analysis complete!")

if __name__ == "__main__":
    # Run the analysis for Apple Inc.
    analyze_stock("AAPL")
