from typing import Union
from lxml.html import document_fromstring
from textwrap import fill


class HTMLParserArticle:
    title = ".//title"
    paragraphs = ".//p"
    headers = ".//*[self::h2 or self::h3 or self::h4]"
    paragraph_with_headers = ".//*[self::p or self::h2 or self::h3]"

    def __init__(self, html: str, len_string: int = 80, add_link: bool = True, with_headers: bool = False,
                 with_title: bool=True):

        self.tree_html = document_fromstring(html)
        self.len_string = len_string
        self.add_link = add_link
        self.with_headers = with_headers
        self.with_title = with_title

    def get_title(self) -> str:
        """Получить название статьи"""

        return self.tree_html.findtext(self.title)

    def get_paragraph_text(self, elem) -> Union[list[str], None]:
        """Получить текст параграфа
        :param elem - элемент html
        """

        lst_text = []
        if elem.tag == 'p' or self.with_headers:
            if 'class' in elem.attrib and 'description' in elem.attrib['class']:
                return
            lst_text.append(elem.text)
            for sub_el in elem:
                if sub_el.tag == 'a':
                    if sub_el.text is None:
                        for sub in sub_el:
                            lst_text.append(sub.text)
                    else:
                        lst_text.append(sub_el.text)
                    if self.add_link:
                        lst_text.append(f' [{sub_el.attrib["href"]}]')
                    lst_text.append(sub_el.tail)

            return lst_text

        else:
            return lst_text.append("\n\n")

    def get_text_article(self) -> str:
        """Получить текст всей статьи"""

        lst_all_text = []

        if self.with_title:
            lst_all_text.append(self.get_title())
            lst_all_text.append("\n\n")

        for el in self.tree_html.xpath(self.paragraph_with_headers):
            paragraph_text = self.get_paragraph_text(el)
            if paragraph_text is None:
                continue
            else:
                lst_all_text.append(paragraph_text)
            if el.getnext() is None:
                break
            lst_all_text.append("\n\n")

        return self.gum_paragraph(lst_all_text)

    def gum_paragraph(self, lst_paragraphs: list[list[str]]) -> str:
        """Склеить параграфы с учетом ширины строки"""

        lst_for_gum = []
        for paragraph in lst_paragraphs:
            if paragraph[0] is None:
                continue
            if paragraph != "\n\n":
                lst_for_gum.append(fill("".join(paragraph), self.len_string, replace_whitespace=False))
            else:
                lst_for_gum.append("\n\n")

        return "".join(lst_for_gum)

    def get_headers(self) -> str:
        """Получить заголовки статьи"""

        lst_headers = [self.get_title()]+[el.text for el in self.tree_html.xpath(self.headers)]
        return "\n".join(lst_headers)
