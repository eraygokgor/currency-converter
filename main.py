import credentials
import currency


if __name__ == '__main__':
    client = currency.Client(credentials.API_KEY)
    print(client.status())
    print(client.historical(date='2023-1101', base_currency='USD', currencies=['TRY']))
