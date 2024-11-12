import Scrapping
import Translator

ARTICLE_URL = "https://dev.to/cloudtech/machine-learning-lifecycle-process-547p"

text = Scrapping.extract_text(ARTICLE_URL)
translated_text = Translator.translator_text(text)

with open("../article_ptbr.md", "w", encoding="utf-8") as file:
    file.write(translated_text)

