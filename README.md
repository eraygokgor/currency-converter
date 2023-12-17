# freecurrencyapi Usage

## Registration
First, register the website from [here](https://freecurrencyapi.net/register) to get your API key.
After registration, you will find your api key [here](https://freecurrencyapi.net/dashboard).


## Usage
```python
import currency

client = currency.Client('YOUR_API_KEY')
```
To get the status of your account:
```python
print(client.status())
```
You can get the list of all the currencies supported by the API:
```python
print(client.get_currencies())
```
If you want to get specific currencies:
```python
print(client.get_currencies(currencies=['USD', 'EUR']))
```
To get the latest exchange rates:
```python
print(client.get_rates(base_currency='USD', currency=['EUR', 'GBP']))
```
To get the latest converted amount of a currency:
```python
print(client.convert(base_currency='USD', currency=['EUR', 'GBP'], amount=10))
```
To get the historical exchange rates:
```python
print(client.historical(date='2020-01-01', base_currency='USD', currencies=['EUR', 'GBP'], amount=10))
```
