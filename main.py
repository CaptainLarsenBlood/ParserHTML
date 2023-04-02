import sys
import requests
from parse import HTMLParserArticle
from inout import save_txt, get_text


def main() -> None:

    url = "https://www.rbc.ru/rbcfreenews/6428e5799a7947d8182c6660?utm_source=yxnews&utm_medium=desktop"  # sys.argv[1]
    html_page = get_text(url)
    main_txt = HTMLParserArticle(html_page).get_text_article()
    save_txt(main_txt, url)


if __name__ == '__main__':
    main()



