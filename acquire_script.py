# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
import zipfile
import io
import shutil
import math
import re
import xml.etree.ElementTree as ET
from pyquery import PyQuery as pq
import json
import os
import traceback


# %%
# https://www.imsdb.com/feeds/alphabetical.php?letter=A

# rss->channel->items->item->link
def load_scripts(start="A", dir="./data"):
    os.makedirs(dir,exist_ok=True)
    start = ord(start)
    for c in range(26+65-start):
        r = requests.get(
            'https://www.imsdb.com/feeds/alphabetical.php?letter={letter}'.format(letter=chr(start+c)))
        links = []
        root = ET.fromstring(r.text)
        for item in root[0].iter('link'):
            link = item.text
            print(item.text)
            links.append(link)
        links.remove("http://www.imsdb.com")
        for link in links:
            try:
                r_script = requests.get(link)
                d = pq(r_script.text)
                pre = d("pre")
                pre_html = pre.html()
                if pre_html:
                    # good ones
                    genres = []
                    for a_elem in d("a"):
                        title = a_elem.get("title")
                        if title and re.match(".* Scripts", title):
                            genres.append(a_elem.text)
                    print(genres)
                    script = re.sub(r"<(|/)b>", r"", pre_html, flags=re.S)
                    title = re.sub(r"\.html", "", re.sub(
                        r"http://.*/", "", link))
                    with open('./data/{title}.json'.format(title=title), "w") as outfile:
                        json.dump({"link": link, "script": script, "genres": genres,
                                   "title": title}, outfile, sort_keys=True, indent=4)
                    print("Written", title)
                else:
                    continue
            except:
                print("Error on loading, skipping...",
                      link, traceback.format_exc())
