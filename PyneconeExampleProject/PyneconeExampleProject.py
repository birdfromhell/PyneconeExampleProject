import pynecone as pc
from pcconfig import config
import requests
import json

class QuotesState(pc.State):
    quotes = "Push For Quotes"
    def getquotes(self):
        r = requests.get("https://api.kanye.rest/")
        x = r.json()
        self.quotes = x['quote']


def index():
    return pc.vstack(
        pc.heading("Kanye Quotes",color="red",font_weight="bold"),
        pc.image(src="https://e3.365dm.com/21/10/1600x900/skynews-kanye-west-news_5551306.jpg?20211019035017",)
        pc.text(QuotesState.quotes,font_size="16px",color="black",as_="i"),
        pc.button("Refresh", on_click=QuotesState.getquotes, _hover={"color": "red"}),
    )


app = pc.App(state=QuotesState)
app.add_page(index)
app.compile()
