import requests
import uuid
import json
import threading

def generate_random_userid():
    return str(uuid.uuid4())

def fetch_proxy():
    try:
        proxy_api_url = "https://gimmeproxy.com/api/getProxy?protocol=http"
        response = requests.get(proxy_api_url)
        data = response.json()
        if data.get('supportsHttps') and 'ip' in data and 'port' in data:
            proxy = f"{data['ip']}:{data['port']}"
            with open("proxy.txt", "a") as file:
                file.write(f'{proxy}\n')
            return {'https': f'http://{proxy}'}
    except Exception as e:
        print(f"Error fetching proxy: {e}")
    return None

def read_proxies():
    try:
        with open("proxy.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def remove_proxy(proxy):
    proxies = read_proxies()
    with open("proxy.txt", "w") as file:
        file.writelines([f"{p}\n" for p in proxies if p != proxy])

def make_request(user_id, proxy=None):
    try:
        url = 'https://api.discord.gx.games/v1/direct-fulfillment'
        headers = {
            'authority': 'api.discord.gx.games',
            'accept': '/',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://www.opera.com',
            'referer': 'https://www.opera.com/',
        }
        data = {'partnerUserId': user_id}
        if proxy:
            response = requests.post(url, headers=headers, json=data, proxies=proxy)
            if response.status_code != 200:
                remove_proxy(proxy['https'].split('//')[1])
            return response
        else:
            return requests.post(url, headers=headers, json=data)
    except:
        if proxy:
            remove_proxy(proxy['https'].split('//')[1])
        return None

def append_token_to_url(token):
    base_url = "https://discord.com/billing/partner-promotions/1180231712274387115/"
    return f"{base_url}{token}"

def attempt_request(index, user_id, results, event):
    proxies = read_proxies()
    for proxy in proxies:
        if event.is_set():
            break
        proxy_dict = {'https': f'http://{proxy}'}
        response = make_request(user_id, proxy_dict)
        if response and not event.is_set():
            try:
                response_data = json.loads(response.text)
                token = response_data.get("token")
                if token:
                    result = f"{index + 1}.) URL with Token: {append_token_to_url(token)}"
                    results[index] = result
                    event.set()
            except json.JSONDecodeError:
                pass

    if not event.is_set():
        for _ in range(3):
            if event.is_set():
                break
            proxy = fetch_proxy()
            if proxy:
                response = make_request(user_id, proxy)
                if response and not event.is_set():
                    try:
                        response_data = json.loads(response.text)
                        token = response_data.get("token")
                        if token:
                            result = f"{index + 1}.) URL with Token: {append_token_to_url(token)}"
                            results[index] = result
                            event.set()
                    except json.JSONDecodeError:
                        pass

def process_token(index, results):
    user_id = generate_random_userid()
    event = threading.Event()

    attempt_request(index, user_id, results, event)

    if not results[index]:
        results[index] = f"{index + 1}.) Failed to make a request after 3 attempts."

def main():
    num_tokens = int(input("Enter the number of tokens to generate: "))
    results = [None] * num_tokens
    threads = [threading.Thread(target=process_token, args=(i, results)) for i in range(num_tokens)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    for result in results:
        if result:
            print(result)

if __name__ == "__main__":
    main()
