import credentials
import currency

# tests
if __name__ == '__main__':
    client = currency.Client(credentials.API_KEY)
    print(client.status())

    client.get_currencies()
    client.get_currencies(['USD', 'EUR', 'GBP'])

    print(client.latest())
    print(client.latest(base_currency='TRY'))
    print(client.latest(currencies=['USD', 'EUR', 'GBP']))
    print(client.latest(amount=10))
    print(client.latest(base_currency='EUR', currencies=['USD', 'EUR', 'TRY'], amount=10))

    print(client.historical('2020-01-01'))
    print(client.historical('2020-01-01', base_currency='TRY'))
    print(client.historical('2020-01-01', currencies=['USD', 'EUR', 'GBP']))
    print(client.historical('2020-01-01', base_currency='TRY', currencies=['USD', 'EUR', 'GBP']))
    print(client.historical('2020-01-01', amount=10))
