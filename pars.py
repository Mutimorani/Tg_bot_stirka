import requests
import lxml.html


def get_count(html_text):
    tree = lxml.html.document_fromstring(html_text)
    text_st = tree.xpath("//*[@class='text-center']/ text()")
    return text_st

html_text = requests.get("https://cabinet.unimetriq.com/client/b56d061dabed69baa9b52aef98304fbf")

if html_text.status_code == 200:
    spisok = list(map(str.strip, get_count(html_text.text)))
    res = []
    for i, x in enumerate(spisok):
        r = f'{i + 1} {"стир" if i <7 else "суш"}: {x}'
        res.append(r) 

