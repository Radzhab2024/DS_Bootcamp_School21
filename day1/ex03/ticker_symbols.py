def get_ticker_and_price():
    import sys
    if len(sys.argv) == 2:
        ticker_name = sys.argv[1].upper()
        find_by_ticker(ticker_name)
    else:
        return


def find_by_ticker(ticker):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    if ticker not in STOCKS:
        print('Unknown ticker')
    else:
        for item in COMPANIES:
            if COMPANIES[item] == ticker:
                print(item, STOCKS[ticker])


if __name__ == '__main__':
    get_ticker_and_price()
