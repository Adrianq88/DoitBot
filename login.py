# login.py

import requests

def login(email, password):
    get_site = requests.get('https://sklep.sizeer.com/')
    s = requests.session()
    payload = {
        'email': email,
        'password': password,
    }
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    headers = {
        'Authority': 'sklep.sizeer.com',
        'Method': 'POST',
        'Path': '/api/customers/login',
        'User-Agent': user_agent,
        'Content-Type': 'application/json',
        'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
        'Referer': 'https://sklep.sizeer.com/login?_gl=1%2anie6pc%2a_up%2aMQ..&gclid=CjwKCAiA0PuuBhBsEiwAS7fsNapOrhgHgnVbh0uGF0nHNB3jAF6BxBEq6zhNkOvGoe2tjyTtF3iq2BoCPKsQAvD_BwE',
    }

    response = s.post('https://sklep.sizeer.com/login', json=payload, headers=headers)

    print(response.content)
    print("Status code: ", response.status_code)
    if response.ok:
        print("Logged in.")
    else:
        print("Something went wrong.")
    return s
