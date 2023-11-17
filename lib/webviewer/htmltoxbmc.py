import re
from html import unescape

class HTMLConverter:
    def __init__(self):
        self.regex_patterns = {
            'title': re.compile(r'<title>(.*?)</title>', re.I),
            'links': re.compile(r'<a href=["\']?([^"\' >]+)["\']?[^>]*>(.*?)</a>', re.I),
            'images': re.compile(r'<img src=["\']?([^"\' >]+)["\']?[^>]*>', re.I),
            'remove_tags': re.compile(r'<[^>]+>'),
            'reduce_whitespace': re.compile(r'\s{2,}')
        }

    def convert(self, html):
        title = self._extract_title(html)
        content = self._process_content(html)
        return title, content

    def _extract_title(self, html):
        match = self.regex_patterns['title'].search(html)
        return unescape(match.group(1)) if match else "No Title"

    def _process_content(self, html):
        html = self.regex_patterns['links'].sub(r'Link: \2 (\1)', html)
        html = self.regex_patterns['images'].sub(r'Image: \1', html)
        html = self.regex_patterns['remove_tags'].sub('', html)
        html = self.regex_patterns['reduce_whitespace'].sub(' ', html)
        return unescape(html).strip()

# Usage example
converter = HTMLConverter()
title, content = converter.convert("<html><head><title>Sample Page</title></head><body><p>Hello <a href='https://example.com'>world</a>!</p><img src='image.jpg'/></body></html>")
print("Title:", title)
print("Content:", content)
