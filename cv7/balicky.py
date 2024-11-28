from forex_python.bitcoin import BtcConverter

b = BtcConverter()  # force_decimal=True to get Decimal rates
print(b.get_latest_price("USD"))
