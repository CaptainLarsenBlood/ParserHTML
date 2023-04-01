import sys
import requests
from parse import HTMLParserArticle
from inout import save_txt, get_text


def main() -> None:

    url = "https://www.gazeta.ru/social/news/2023/04/01/20113447.shtml"  # sys.argv[1]
    html_page = get_text(url)
    main_txt = HTMLParserArticle(html_page).get_text()
    save_txt(main_txt, url)


if __name__ == '__main__':
    main()



