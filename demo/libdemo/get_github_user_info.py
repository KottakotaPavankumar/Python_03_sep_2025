import requests

userid = input("Enter github userid :")
response = requests.get(f"https://api.github.com/users/{userid}")
if response.status_code != 200:
    print('Sorry! Could not get details!')
    exit()

details = response.json()   # Convert JSON response to dict

print('Name    : ', details['name'])
print('Company : ', details['company'])
print('Location: ', details['location'])