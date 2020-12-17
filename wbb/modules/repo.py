from wbb import app
from pyrogram import filters
from wbb.utils import cust_filter

__MODULE__ = "Repo"
__HELP__ = "/repo - To Get My Github Repository Link"


@app.on_message(cust_filter.command(commands=("repo")))
async def repo(client, message):
    app.set_parse_mode("markdown")
    await message.reply_text(f'''
```👨‍💻 Developer``` - @TheHamkerCat

```🔗 Repo``` - github.com/thehamkercat/WilliamButcherBot

```❤️ PRs Are Always Welcomed```''', disable_web_page_preview=True)
