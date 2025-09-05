def input_func():
    import sys
    if len(sys.argv) != 2:
        return

    incoming_args = sys.argv[1].strip()

    if ',,' in incoming_args:
        return

    expressions = []
    for expr in incoming_args.split(','):
        if expr:
            expressions.append(expr.strip())

    init_func(expressions)


def init_func(words):
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

    for word in words:
        if not word:
            return
    for word in words:
        word_clear = word.strip().capitalize()
        if word_clear in COMPANIES:
            print(word_clear, 'stock price is', STOCKS[COMPANIES[word_clear]])
        elif word_clear.upper() in STOCKS:
            ticker = word_clear.upper()
            for company_name in COMPANIES:
                if COMPANIES[company_name] == ticker:
                    print(f'{COMPANIES[company_name]} is a ticker symbol for {company_name}')
        else:
            print(f'{word} is an unknown company or an unknown ticker symbol')


if __name__ == '__main__':
    input_func()
