# Discord Nitro Generator

## Overview
This project provides tools to generate Discord Nitro URLs, aiming to enhance your and your friends' Discord experience. Please note that the use of these tools should align with Discord's Terms of Service and ethical standards.

## Features

### `main_with_proxy.py`
- **Proxy Integration**: Utilizes a list of proxies from `proxy.txt`, managing and cycling through them to avoid rate limiting.
- **Automatic Proxy Retrieval**: Automatically retrieves and utilizes stored proxies.
- **Proxy Validation**: Invalid or non-functioning proxies are automatically removed and replaced with new ones.

### `main_no_proxy.py`
- **Direct Access**: Operates without the use of proxies.
- **Rate Limit Warning**: Likely to encounter rate limiting (504 error) from Discord after a few URL generations.

## Important Notice
- The usage of this tool to generate Discord Nitro URLs or to bypass Discord's rate limits might be against Discord's Terms of Service.
- Users should be aware of and comply with Discord's policies to avoid potential account suspension or other penalties.
- This project is intended for educational purposes only.

## Getting Started
To get started with this project:
1. Clone the repository to your local machine.
2. Ensure you have the necessary Python environment to run the scripts. (Specify Python version and any dependencies)
3. For `main_with_proxy.py`, create a `proxy.txt`.
4. Run `main_with_proxy.py` or `main_no_proxy.py` as per your requirement.
5. Follow any on-screen instructions to proceed.

## Contributing
Every contribution to this project is appreciated. Feel free to fork the repository, make changes, and submit a pull request.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=flaryx32/DiscordNitroGenerator&type=Date)](https://star-history.com/#flaryx32/DiscordNitroGenerator&Date)
