import requests

def convert_inr_to_other(amount_in_inr, other):
    url = "https://open.er-api.com/v6/latest/INR"
    resp = requests.get(url)
    data = resp.json()

    if resp.status_code == 200:
        rate = data["rates"].get(other)
        if rate:
            converted = amount_in_inr * rate
            return converted
        else:
            raise ValueError('Invalid target currency!')
    else:
        raise ValueError('Could not get details!')


# Example:
inr = 10000
try :
    usd = convert_inr_to_other(inr, 'USD')
    print(f'INR {inr} = USD {usd:.2f}')
except Exception as ex:
    print('Error : ' + str(ex))

try :
    aud = convert_inr_to_other(inr, 'AUD')
    print(f'INR {inr} = AUD {aud:.2f}')
except Exception as ex:
    print('Error : ' + str(ex))

try :
    abc = convert_inr_to_other(inr, 'ABC')
    print(f'INR {inr} = ABC {aud:.2f}')
except Exception as ex:
    print('Error : ' + str(ex))
