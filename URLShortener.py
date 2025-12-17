import requests
import json
import os
import sys

# Try to load .env file manually since we are avoiding external wrapper libraries like python-dotenv
def load_env():
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value

def shorten_url_bitly(long_url, token):
    """
    Shortens a URL using the Bitly V4 API.
    """
    endpoint = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "long_url": long_url,
        "domain": "bit.ly"
    }

    try:
        response = requests.post(endpoint, headers=headers, json=data)
        
        # Check for HTTP errors
        if response.status_code in [200, 201]:
            data = response.json()
            return data.get("link")
        elif response.status_code == 429:
            print("Error: API limit reached (429). You have exhausted your Bitly free tier limits for this month.")
            return None
        else:
            print(f"Error: Received status code {response.status_code}")
            try:
                error_detail = response.json()
                print(f"Details: {error_detail}")
            except:
                print(f"Raw Response: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        return None

def main():
    load_env()
    token = os.environ.get("BITLY_ACCESS_TOKEN")
    
    # Check if token is set and not default placeholder
    if not token or token == "YOUR_BITLY_ACCESS_TOKEN_HERE":
        print("Error: BITLY_ACCESS_TOKEN not found or invalid in .env file.")
        print("Please sign up at https://bitly.com/, get a Generic Access Token, and add it to the .env file.")
        return

    print("--- Request-Based URL Shortener (Bitly) ---")
    print("Type 'exit' to quit.")

    while True:
        long_url = input("\nEnter a long URL: ").strip()

        if long_url.lower() == 'exit':
            print("Exiting...")
            break

        if not long_url.startswith(('http://', 'https://')):
            print("Invalid URL. Please ensure it starts with http:// or https://")
            continue

        print("Shortening...")
        short_link = shorten_url_bitly(long_url, token)

        if short_link:
            print(f"Success! Short URL: {short_link}")

if __name__ == "__main__":
    main()
