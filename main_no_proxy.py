

import requests
import uuid
import json

def generate_random_userid():
    return str(uuid.uuid4())

def make_request(user_id):
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
        'authority': 'api.discord.gx.games',
        'accept': '/',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        # Add other headers as required
    }
    data = {'partnerUserId': user_id}
    response = requests.post(url, headers=headers, json=data)
    return response

def append_token_to_url(token):
    base_url = "https://discord.com/billing/partner-promotions/1180231712274387115/"
    return f"{base_url}{token}"

def main():
    num_tokens = int(input("Enter the number of tokens to generate: "))
    for i in range(num_tokens):
        user_id = generate_random_userid()
        response = make_request(user_id)

        try:
            response_data = json.loads(response.text)
            token = response_data.get("token")
            if token:
                full_url = append_token_to_url(token)
                print(f"{i+1}.) URL with Token: {full_url}")
            else:
                print(f"{i+1}.) No token received in response.")
        except json.JSONDecodeError:
            print(f"{i+1}.) Error processing response: {response.text}")

if __name__ == "__main__":
    main()
