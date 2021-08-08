from typing import Any
from pathlib import Path
import urllib.request
import urllib.response
import xml.etree.ElementTree as ET

sitemap_url: str = 'https://blog.abarabakuhatsu.com/sitemap/sitemap-0.xml'

local_sitemap: Path = Path('sitemap_sample.xml')
old_sitemap: Path = Path('/sitemap_old/sitemap_sample.xml')

latest_sitemap = urllib.request.urlopen(sitemap_url)


def convert_sitemap_url_list(
        sitemap: Any,
        tag: str = 'loc',
        name_space: str = '{http://www.sitemaps.org/schemas/sitemap/0.9}') -> list[str]:
    element_tree = ET.parse(sitemap)
    return [i.text for i in element_tree.iter(f'{name_space}{tag}') if isinstance(i.text, str)]


def compare_two_lists(list1: list[Any], list2: list[Any]) -> bool:
    return set(list1) == set(list2)


local_sitemap_list = convert_sitemap_url_list(local_sitemap)
latest_sitemap_list = convert_sitemap_url_list(latest_sitemap)

print(f"{latest_sitemap_list}")

print(f"{compare_two_lists(local_sitemap_list, latest_sitemap_list)=}")
