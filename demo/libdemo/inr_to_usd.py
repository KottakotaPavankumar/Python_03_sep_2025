import requests

def convert_inr_to_usd(amount_in_inr):
    url = "https://open.er-api.com/v6/latest/INR"
    resp = requests.get(url)
    data = resp.json()

    if resp.status_code == 200 and data.get("result") == "success":
        rate = data["rates"].get("USD")
        if rate:
            converted = amount_in_inr * rate
            #print(f"{amount_in_inr} INR = {converted:.2f} USD (Rate: {rate:.4f})")
            return converted
        else:
            print("USD rate missing in response")
            return None
    else:
        print("Error:", data.get("error-type") or data)
        return None

def convert_inr_to_aud(amount_in_inr):
    url = "https://open.er-api.com/v6/latest/INR"
    resp = requests.get(url)
    data = resp.json()

    if resp.status_code == 200 and data.get("result") == "success":
        rate = data["rates"].get("AUD")
        return  amount_in_inr * rate
    else:
        raise ValueError('AUD rate is not available')

# Example:
inr = 10000
usd = convert_inr_to_usd(inr)
print(f'INR {inr} = USD {usd:.2f}')
aud = convert_inr_to_aud(inr)
print(f'INR {inr} = AUD {aud:.2f}')