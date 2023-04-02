#!/usr/bin/env python
# coding:utf-8

import configparser
import sys
from parse import HTMLParserArticle
from inout import save_txt, get_text

conf = configparser.RawConfigParser()
conf.read("config")
len_st = conf.getint("HEADER", "len_string")
link = conf.getboolean("HEADER", "add_link")
title = conf.getboolean("HEADER", "add_title")
headers = conf.getboolean("HEADER", "with_headers")


def main() -> None:

    url = input("Вставьте ссылку: ")
    #url = sys.argv[1]
    html_page = get_text(url)
    doc_html = HTMLParserArticle(html_page, len_string=len_st, add_link=link, with_headers=headers, with_title=title)
    main_txt = doc_html.get_text_article()
    save_txt(main_txt, url)


if __name__ == '__main__':
    main()
