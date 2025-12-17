# Request-Based URL Shortener

A simple Python CLI utility to shorten URLs using the Bitly API.

## Prerequisites

- Python 3.x installed.
- Internet connection.
- A free Bitly account.

## Setup & Running

1.  **Get API Token**:
    - Sign up at [Bitly](https://bitly.com/).
    - Go to Settings -> API which generates a Generic Access Token.
    - *Note*: This project already has a token configured in `.env`.

2.  **Install Dependencies**:
    - This script uses the standard `requests` library. If you don't have it, install it:
      ```bash
      pip install requests
      ```

3.  **Run the Script**:
    - Open your terminal or command prompt in this folder.
    - Run the following command:
      ```bash
      python URLShortener.py
      ```

4.  **Usage**:
    - When prompted, paste a long URL (starting with `http://` or `https://`).
    - The script will output the shortened Bitly link.
    - Type `exit` to close the program.

## Troubleshooting

- **"Module not found" error**: Run `pip install requests` to install the missing library.
- **"Error: BITLY_ACCESS_TOKEN not found"**: Ensure the `.env` file exists in the same folder and contains `BITLY_ACCESS_TOKEN=your_token`.

**App LIMITS**
Yes, the Bitly Free Tier has specific credits and limits (as of late 2024):

API Requests: You are limited to 1,000 API calls per month.
Short Links: You can create approx. 5 to 10 new bit.ly links per month (it fluctuates, but it's low).


**Tips**
If you hit the limit, you can:

* Wait for the first of the next month.
* Switch to TinyURL (unlimited creation, but fewer features).
* Create a new free Bitly account.