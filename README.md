# cmp3111m
Software Engineering Assignment

## Program Requirements 
The program depends on the following packages:

Package Name | Purpose
--- | ---
Tkinter | Render UI
newsapi-python | Getting news articles
spotipy | Getting list of spotify songs

Install the required packages using the command

```python
python3 -m pip install [PACKAGE_NAME]
```

## API Keys
The program relies on two API keys: one for news and one for spotify.

It will search for the API keys in a file called `keys.json`, stored within a directory called `config`.

The key for the news api will be called `news`, the key for spotify Api is called `client_id` and `client_secret`.

## Runnning the Program
To run the program you run the main.py file. The program will not run as the API keys are not stored in this Git Repository as it is not a safe practice.

The program currently takes the top news headings from the week, selects a random work of greater than 3 letter length and creates a spotify playlist based on these words.


