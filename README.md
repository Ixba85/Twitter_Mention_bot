# Twitter Bot README
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
  [![Generic badge](https://img.shields.io/badge/OpenSource-yes!-<COLOR>.svg)](https://shields.io/)



![Project Image](https://github.com/Ixba85/Twitter_Mention_bot/blob/main/Twitter%20bot%20Tw.PNG)

> Twitter bot Project when you use specific #(Hashtag) it will send you a random recipe.:speech_balloon:

---

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [Requirements](#Requirements)
- [Installation](#Installation)
- [License](#license)
- [Author Info](#author-info)

---

## Description

I'm Learning Python so I'm making bots to learn and practice, this bot was made to send you a reply when the bot is mentioned and has a specific hashtag. You can use any reply or link that you want the bot to reply to. Feel free to use it. 


---

## How To Use

Create your Twitter account, mention the bot without running the code first so it will have some mentions to look for. Then run the code “Get_mention_ID.py”. You will have the ID of all the mentions, stored in “last_seen.txt” the first ID that the bot will give you. 
In credentials.py add the API from Twitter developers. 
Once you have all your information you can run “recipe_bot.py”. You will see that “last_seen.txt” changed and will respond to all your mentions. 


[Back To The Top](#Twitter-Bot-README)

---

## Requirements 

1.	You need to install Python on your computer. 
2.	Sign in to [Twitter Developers](https://developer.twitter.com/en)
3.	Then install [Tweepy]( https://github.com/tweepy/tweepy) with pip install
```html
pip install tweepy
```
4.	In “Get_mention_ID.py” add your API keys 
```python
CONSUMER_KEY = "YOUR CONSUMER_KEY"
CONSUMER_SECRET = "YOUR CONSUMER_SECRET"
ACCESS_TOKEN = "YOUR ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR ACCESS_TOKEN_SECRET"
```

[Back To The Top](#Twitter-Bot-README)

---

## Installation

1.	Run “Get_mention_ID.py”.
2.	Copy the ID and save it in “last_seen.txt”
3.	In recipe_bot.py, change the hashtag

```html
store_last_seen_id(since_id, FILE_NAME)
        if '#randomrecipe' in mention.full_text.lower():
            print('found #randomrecipe')
```
4.	Run the file recipe_bot.py
5.	Check if you get the response 
If you do congrats, the bot is working well. 

[Back To The Top](#Twitter-Bot-README)

---
## License

MIT License

Copyright (c) [2022] [Chory Codes]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#Twitter-Bot-README)

---

## Author Info

- Twitter - [@ChoryCodes](https://twitter.com/ChoryCodes)
- Bot - [@getRecipe_Bot]( https://twitter.com/getRecipe_Bot)

[Back To The Top](#Twitter-Bot-README)

