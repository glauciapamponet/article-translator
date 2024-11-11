import requests
import html2text
from bs4 import BeautifulSoup


def clean_text(text):
    lines = (line.strip() for line in text.splitlines())
    parts = (phrase.strip() for line in lines for phrase in line.split(" "))
    cleaned = '\n'.join(part for part in parts if part)

    return cleaned

# Resolver a questão das tags de imagem, que serão traduzidas se forem mandadas pro tradutor
def extract_text(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            h = html2text.HTML2Text()
            h.ignore_links = False
            soup = BeautifulSoup(response.text, 'html.parser')
            title = str(soup.find('h1', class_='fs-3xl m:fs-4xl l:fs-5xl fw-bold s:fw-heavy lh-tight mb-2 medium'))
            article_content = str(soup.find('div', class_='crayons-article__body'))
            text = h.handle(title) + '\n' + h.handle(article_content)
            return text
        else:
            print(f'Failed to fetch URL. Status code: {response.status_code}')
    except Exception as e:
        print(f'Not possible access the url. Exception: {e}')
        return None
