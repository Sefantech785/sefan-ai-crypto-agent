
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BINANCE_API_URL = "https://api.binance.com/api/v3"

def get_price(symbol):
    """Get the current Binance price for a trading pair."""
    url = f"{BINANCE_API_URL}/ticker/price"
    response = requests.get(
        url,
        params={"symbol": symbol.upper()},
        timeout=10
    )
    response.raise_for_status()
    data = response.json()
    return float(data["price"])


def analyze_market(symbol):
    """Basic market-data function for the Sefan AI Crypto Agent."""
    try:
        price = get_price(symbol)

        return {
            "symbol": symbol.upper(),
            "price": price,
            "status": "success"
        }

    except requests.RequestException as error:
        return {
            "symbol": symbol.upper(),
            "status": "error",
            "message": str(error)
        }


def main():
    print("Sefan AI Crypto Agent")
    print("=====================")

    symbol = input("Enter trading pair (example: BTCUSDT): ").strip()

    if not symbol:
        print("Please enter a trading pair.")
        return

    result = analyze_market(symbol)

    if result["status"] == "success":
        print(f"\nSymbol: {result['symbol']}")
        print(f"Current Price: {result['price']}")
    else:
        print(f"\nError: {result['message']}")


if __name__ == "__main__":
    main()
