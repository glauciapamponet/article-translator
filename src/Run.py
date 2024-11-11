import Scrapping

ARTICLE_URL = "https://dev.to/cloudtech/machine-learning-lifecycle-process-547p"


def translating_article(url):
    # chamar o tradutor da Azure aqui
    return Scrapping.extract_text(url)


print(translating_article(ARTICLE_URL))
