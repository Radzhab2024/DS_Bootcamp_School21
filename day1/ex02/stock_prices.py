def get_price():
    import sys
    if len(sys.argv) == 2:
        company_name = sys.argv[1].capitalize()
        companies_and_stocks(company_name)
    else:
        return


def companies_and_stocks(company_name):
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

    if company_name not in COMPANIES:
        print('Unknown company')
    else:
        print(STOCKS[COMPANIES[company_name]])


if __name__ == '__main__':
    get_price()
