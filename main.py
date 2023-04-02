import sys
import requests
from parse import HTMLParserArticle
from inout import save_txt, get_text


def main() -> None:

    url = "https://lenta.ru/news/2023/04/02/edinenie/"  # sys.argv[1]
    html_page = get_text(url)
    main_txt = HTMLParserArticle(html_page).get_text_article()
    save_txt(main_txt, url)


if __name__ == '__main__':
    main()



