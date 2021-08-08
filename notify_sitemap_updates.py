#!/usr/bin/env python
from typing import Any
from pathlib import Path
import urllib.request
import urllib.response
import xml.etree.ElementTree as ET


def convert_sitemap_url_list(
        sitemap: Any,
        tag: str = 'loc',
        name_space: str = '{http://www.sitemaps.org/schemas/sitemap/0.9}') -> list[str]:
    """サイトマップから登録されているurlのリストを制作する

    Args:
        sitemap (Any): サイトマップのパス
        tag (str, optional): 検索するタグ. Defaults to 'loc'.
        name_space (str, optional): [description]. Defaults to '{http://www.sitemaps.org/schemas/sitemap/0.9}'.

    Returns:
        list[str]: [description]
    """
    element_tree = ET.parse(sitemap)
    return [i.text for i in element_tree.iter(f'{name_space}{tag}') if isinstance(i.text, str)]


def compare_two_lists(list1: list[Any], list2: list[Any]) -> bool:
    """2つのリストの内容を比較（重複無視）

    Args:
        list1 (list[Any])
        list2 (list[Any])

    Returns:
        bool: 2つのリストの要素が全て同じならTrue
    """
    return set(list1) == set(list2)


def main() -> None:
    sitemap_url = 'https://blog.abarabakuhatsu.com/sitemap/sitemap-0.xml'
    sitemap_index_url = 'https://blog.abarabakuhatsu.com/sitemap/sitemap-index.xml'
    google_request_url = 'https://www.google.com/ping?sitemap='

    local_sitemap: Path = Path('sitemap.xml')
    temp_file: Path = Path('temp.xml')

    latest_sitemap: str = urllib.request.urlopen(sitemap_url).read().decode('utf-8')

    if not local_sitemap.exists():
        local_sitemap.write_text(latest_sitemap)
        print("Downloaded the sitemap from the site for the first run")
        return print("notify_sitemap_updates.py exit")

    temp_file.write_text(latest_sitemap)

    local_sitemap_list: list[str] = convert_sitemap_url_list(local_sitemap)
    latest_sitemap_list: list[str] = convert_sitemap_url_list(temp_file)

    if not compare_two_lists(local_sitemap_list, latest_sitemap_list):
        print("** Sitemap has been updated **")
        print("Update local sitemap")
        local_sitemap.write_text(latest_sitemap)

        print("Notify Google of sitemap updates")
        response = urllib.request.urlopen(google_request_url + sitemap_index_url)
        print("--------------------------------")
        print(response.read().decode('utf-8'))
        print("--------------------------------")
    else:
        print("Sitemap has not been updated")

    temp_file.unlink() if temp_file.exists() else None
    return print("notify_sitemap_updates.py exit")


if __name__ == '__main__':
    main()
