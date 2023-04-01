from typing import Iterable, Union

from lxml.etree import Element
from lxml.html import document_fromstring
from textwrap import fill


class HTMLParserArticle:
    title = ".//title"
    paragraphs = ".//p"
    headers = ".//*[self::h2 or self::h3 or self::h4]"
    paragraph_with_headers = ".//*[self::p or self::h2 or self::h3 or self::h4]"

    def __init__(self, html: str, len_string: int = 80, add_link: bool = True, with_headers: bool = False):
        self.tree_html = document_fromstring(html)
        self.len_string = len_string
        self.add_link = add_link
        self.with_headers = with_headers

    def get_title(self) -> str:

        return self.tree_html.findtext(self.title)

    def get_text(self) -> str:

        lst_text_elm = []
        for el in self.tree_html.xpath(self.paragraph_with_headers):
            if el.tag == 'p' or self.with_headers:
                if 'class' in el.attrib:
                    continue
                lst_text_elm.append(el.text)
                for sub_el in el:
                    if sub_el.tag == 'a':
                        lst_text_elm.append(sub_el.text)
                        if self.add_link:
                            lst_text_elm.append(f' [{sub_el.attrib["href"]}]')
                            lst_text_elm.append(sub_el.tail)

                lst_text_elm.append("\n\n")
            else:
                lst_text_elm.append("\n\n")

        return fill("".join(lst_text_elm), self.len_string, replace_whitespace=False)

    def get_headers(self) -> str:

        lst_headers = [self.get_title()]+[el.text for el in self.tree_html.xpath(self.headers)]
        return "\n".join(lst_headers)
