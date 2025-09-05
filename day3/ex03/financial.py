#!/usr/bin/env python3
import requests
import time
import sys
from bs4 import BeautifulSoup


def get_finance_data(ticker, field):
    try:
        url = f'https://finance.yahoo.com/quote/{ticker.upper()}/financials?p={ticker.upper()}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception('URL does not exist')
        soup = BeautifulSoup(response.text, 'html.parser')
        data_table = soup.find_all('div', {"class": 'row'})
        if not data_table:
            raise Exception('Could not find financial data table')

        for row in data_table:
            if field in row.text:
                values = row.find_all('div', class_='column yf-t22klz')
                values_alt = row.find_all('div', class_='column yf-t22klz alt')
                values += values_alt
                result_massage = tuple([field] + [value.text for value in values])
                return result_massage
        raise Exception('Requested field does not exist')

    except Exception as er:
        raise Exception(f"An error occurred: {er}")


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage: ./financial.py <TICKER> <FIELD>')
        sys.exit(1)
    ticker_name = sys.argv[1]
    field_name = sys.argv[2]

    time.sleep(5)

    try:
        result = get_finance_data(ticker_name, field_name)
        print(result)
    except Exception as e:
        print(e)
