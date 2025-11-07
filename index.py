import requests
from bs4 import BeautifulSoup
from pprint import pprint
import collections
import json


def extract_lyrics(url, word_lenght = 2):
    
    print(f"====== Fetching lyrics from {url} ======")
    r = requests.get(url)
    
    if r.status_code != 200 :
        print("Impossible de récuperer la page..")
        return []
    soup = BeautifulSoup(r.content, 'html.parser')
    lyrics = soup.find("div", class_="Lyrics__Container-sc-a49d8432-1 fBKwZw")
    
    if not lyrics :
        return extract_lyrics(url)
    
    all_words = []
    for sentence in lyrics.stripped_strings :
        sentence_words = [word.strip(",").strip(".").lower() for word in sentence.split() if len(word) > word_lenght]
        all_words.extend(sentence_words)

    count = collections.Counter(all_words)
    pprint(count.most_common(10))
    
    return all_words

def get_all_urls():
    
    page = 1
    links = []
    
    while True : 
        r = requests.get(f"https://genius.com/api/artists/2824236/songs?page={page}&sort=popularity")
    
        if r.status_code == 200 :
            
            print(f"===== Fetching data from pages {page} =====")
            
            response = r.json().get("response", {})
            next_page = response.get("next_page")
            
            songs = response.get("songs")
            links.extend([song.get("url") for song in songs])
            # pprint(links)
    
            page += 1
        
            if not next_page :
                print("No more pages to fetch...")
                break
    
    return links



def get_all_words():
    urls = get_all_urls()
    
    words = []
    for url in urls :
        lyrics = extract_lyrics(url=url)
        words.extend(lyrics)
    
    with open("data.json", "w") as f :
        json.dump(words, f, indent=4)
    
    count = collections.Counter(words)
    most_common_words = count.most_common(10)
    pprint(most_common_words)


get_all_words()

extract_lyrics(url="https://genius.com/Elyslime-interlude-lyrics")
       
       
       
