import requests
import html2text
from bs4 import BeautifulSoup


def clean_text(title, text):
    h = html2text.HTML2Text()
    h.ignore_links = False
    lines = (h.handle(line) for line in text)
    lines = [line.replace('\n', '') for line in lines if line != '']
    lines = [line for line in lines if len(line) > 0]
    cleaned = h.handle(title) + '\n'.join(lines)
    return cleaned


# Resolver a questão das tags de imagem, que serão traduzidas se forem mandadas pro tradutor
def extract_text(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = str(soup.find('h1', class_='fs-3xl m:fs-4xl l:fs-5xl fw-bold s:fw-heavy lh-tight mb-2 medium'))
            article_content = str(soup.find('div', class_='crayons-article__body')).splitlines()
            text = clean_text(title, article_content)
            return text
        else:
            print(f'Failed to fetch URL. Status code: {response.status_code}')
    except Exception as e:
        print(f'Not possible access the url. Exception: {e}')
        return None
