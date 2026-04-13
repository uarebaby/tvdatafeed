import logging
import os
from tvDatafeed import TvDatafeed, Interval

TOKEN_FILE = "tv_auth_token.json"

logging.basicConfig(level=logging.INFO)

# Prefer environment variables so real credentials are not committed.
username = os.environ.get("TRADINGVIEW_USERNAME", "xxxx")
password = os.environ.get("TRADINGVIEW_PASSWORD", "xxxx")

try:
    tv = TvDatafeed(
        #username=username,
        #password=password,
        autologin=True
    )

    logged_in = tv.token != "unauthorized_user_token"
    if logged_in:
        print("TradingView sign-in OK (auth token received).")
    else:
        print(
            "Sign-in did not return a token; using nologin (unauthorized_user_token). "
            "Data may still work for public symbols."
        )

    data = tv.get_hist(
        symbol="AAPL",
        exchange="NASDAQ",
        interval=Interval.in_daily,
        n_bars=1,
    )

    if data is not None and not data.empty:
        print("get_hist OK (received bars).")
        print(data)
        if logged_in:
            print("Overall: login + data OK.")
        else:
            print(
                "Overall: data OK without login. "
                "To test real login, set TRADINGVIEW_USERNAME and TRADINGVIEW_PASSWORD and run again."
            )
    else:
        print("Failed to retrieve data (empty or None).")
        if os.path.exists(TOKEN_FILE):
            os.remove(TOKEN_FILE)
            print(f"Removed token file: {TOKEN_FILE}")

except Exception as e:
    print(f"An error occurred: {e}")
