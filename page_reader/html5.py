import requests
import logging
from bs4 import BeautifulSoup

ELEMENTS_TO_ANALYSE_FOR_LINKS = [
    {
        "selectors": ["article a", ".article a"],
        "selector_name": "article_links"
    },
    {
        "selectors": ["header a", ".header a"],
        "selector_name": "header_nav_links"
    },
    {
        "selectors": ["footer a", ".footer a"],
        "selector_name": "footer_nav_links"
    },
    {
        "selectors": ["nav a", ".nav a"],
        "selector_name": "all_nav_links"
    },
    {
        "selectors": ["aside a", ".aside a"],
        "selector_name": "aside_nav_links"
    },
    # {
    #     "selectors": ["a"],
    #     "selector_name": "all_links"
    # }

]


def read_page(url=None, headers=None):
    """
    this method just reads a page and returns text of the page

    :param url: url to read
    :param headers: dictionary of header data
    :return: text of the webpage
    """
    logging.debug("reading the page {}".format(url))
    if url is None:
        return None
    if headers is None:
        headers = {}
    try:
        res = requests.get(url, headers=headers)
    except:
        res = None

    if res is None:
        return None
    else:
        return res.text


def analyse_links(soup=None, analyse_elements=None):
    links = {}
    for element in analyse_elements:
        selected_elems_data = []
        for selector in element['selectors']:
            selected_elems = soup.select(selector)
            for elem in selected_elems:
                el_href = elem.get('href')
                el_title = elem.get('title')
                # TODO - make the url absolute url
                if el_href:
                    selected_elems_data.append({
                        'url': el_href,
                        'title': el_title
                    })
        links[element['selector_name']] = selected_elems_data
    return links


def analyse(url=None, headers=None, analyse_elements=None):
    if analyse_elements is None:
        analyse_elements = ELEMENTS_TO_ANALYSE_FOR_LINKS

    page_text = read_page(url=url, headers=headers)
    if page_text is None:
        return {
            "status": "cannot_read_page",
            "result": {}
        }
    soup = BeautifulSoup(page_text, 'html.parser')

    result = {}
    result['title'] = soup.title.string
    result['url'] = url
    links = analyse_links(soup=soup, analyse_elements=analyse_elements)
    result['links'] = links
    return {
        "status": "success",
        "result": result
    }
