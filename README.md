# VarieTee Bot

![Tee Bot [TEST]](https://github.com/frascu/varieteebot/workflows/Tee%20Bot%20%5BTEST%5D/badge.svg)
![Tee Bot [PROD]](https://github.com/frascu/varieteebot/workflows/Tee%20Bot%20%5BPROD%5D/badge.svg)


If you know me personally, you can see that I love nerd tee-shirts.
There are lots of websites that sell tees with several designs.
In particular, I prefer tee websites that propose t-shirts having designs made by little designers.
It means that any person can create a design and send it to one of these websites. If the project is very voted by the users of online tee shop, the administrators can decide to put on sale for 24 hours. Therefore, Every day a different t-shirt is sold.

Then, I decided to create a tee bot that sends today's tees sold by different tee shops.

## How it works
Every day the telegram bot extracts today's tees with web scraping and sends the images and the titles on a public telegram channel.

## Implementation
The repository contains mainly three files:
* **tee.py**: it contains the function `get_tees` that returns a list of objects of type `Image`.
Each object contains: 
  * tee title
  * URL of the image source
  * URL of the tee shop
* **run.py**: it sends the list of tees to the public telegram channel using the Telegram API. This script has two parameters:
  * bot token
  * channel id 
* **python-app-test.yml**: Github action that on the event `push` of the branch `main` installs the pip dependencies and executes the script using the GitHub secrets `BOT_TOKEN` and `CHANNEL_TEST_ID`. This action is used for the test.
* **python-app-prod.yml**: Github action that on the event `schedule` (every day at 7 UTC) installs the pip dependencies and executes the script using the GitHub secrets `BOT_TOKEN` and `CHANNEL_ID`.  This action is used for the main channel.

## Configuration
1. Create the telegram bot using [BotFather](https://t.me/botfather)
2. Create a public telegram channel
3. Add the bot as the administrator of the channel
4. Fork my GitHub repository [varieteebot](https://github.com/frascu/varieteebot)
5. In the repository settings create 3 secrets:
    * `BOT_TOKEN`: the token returned by the BotFather and used to call the Telegram Bot API
    * `CHANNEL_ID`: the public telegram channel id on which the tees are sent (_@channelname_)
    * `CHANNEL_ID_TEST`: the channel id for the test (I used my personal chat id)
6. Test opening the section *Actions* of the repository and clicking on *Tee Bot [TEST]* and on *Run workflow*
7. Test in your local environment by typing the following command
    ```bash
    python run.py {BOT_TOKEN} {CHANNEL_ID}
    ```

## My tee's channel
My fantastic channel is [VarieTee](http://t.me/varietee).
If you like it you can follow the channel and give me feedback.

