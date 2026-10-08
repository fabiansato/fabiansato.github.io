#!/usr/bin/env python3
"""Check generated HTML, internal destinations and language alternatives offline."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import sys
import xml.etree.ElementTree as ET

SITE_URL = "https://fabiansato.github.io"
# The shared bilingual error page and the old /about landing route are not
# translated content documents. Their links still receive the regular checks.
UNPAIRED_ROUTES = {"/404.html", "/about.html"}
root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
errors = []


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        relative = path.relative_to(root).as_posix()
        self.url = "/" + relative.removesuffix("index.html") if relative.endswith("index.html") else "/" + relative
        self.ids = set()
        self.links = []
        self.alternates = {}
        self.lang = None
        self.redirect = False
        source = path.read_text(encoding="utf-8")
        self.verification = source.strip() == f"google-site-verification: {path.name}"
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            self.redirect = True
        identifier = attrs.get("id") or (attrs.get("name") if tag == "a" else None)
        if identifier:
            self.ids.add(identifier)
        for attribute in ("href", "src", "poster"):
            if attrs.get(attribute):
                self.links.append(attrs[attribute])
        if attrs.get("srcset") and not attrs["srcset"].startswith("data:"):
            self.links.extend(item.strip().split()[0] for item in attrs["srcset"].split(",") if item.strip())
        if tag == "link" and "alternate" in attrs.get("rel", "").split() and attrs.get("hreflang"):
            self.alternates[attrs["hreflang"]] = attrs.get("href", "")


pages = {path.resolve(): Page(path) for path in sorted(root.rglob("*.html")) if "assets" not in path.relative_to(root).parts}


def destination(url, page):
    parsed = urlsplit(urljoin(SITE_URL + page.url, url))
    if parsed.scheme not in ("http", "https") or parsed.netloc != "fabiansato.github.io":
        return None, None
    target = root / unquote(parsed.path).lstrip("/")
    if target.is_dir():
        target /= "index.html"
    elif not target.suffix and target.with_suffix(".html").is_file():
        target = target.with_suffix(".html")
    return target.resolve(), unquote(parsed.fragment)


for page in pages.values():
    if page.verification:
        continue
    if not page.redirect and page.lang not in ("es", "en"):
        errors.append(f"{page.url}: expected html lang es/en, found {page.lang!r}")
    for link in page.links:
        target, fragment = destination(link, page)
        if target is None:
            continue
        if not target.is_relative_to(root) or not target.is_file():
            errors.append(f"{page.url}: missing local destination {link}")
        elif fragment and target in pages and fragment not in pages[target].ids:
            errors.append(f"{page.url}: missing anchor {link}")
    if page.alternates and page.url not in UNPAIRED_ROUTES:
        for language in ("es", "en"):
            link = page.alternates.get(language)
            if not link:
                errors.append(f"{page.url}: missing {language} language alternative")
                continue
            target, _ = destination(link, page)
            translated = pages.get(target)
            if translated is None or translated.lang != language:
                errors.append(f"{page.url}: invalid {language} language alternative {link}")
                continue
            backlink = translated.alternates.get(page.lang)
            if not backlink or destination(backlink, translated)[0] != page.path.resolve():
                errors.append(f"{page.url}: language alternative does not link back: {link}")

for route in ("index.html", "en/index.html", "projects/index.html", "en/projects/index.html", "blog/index.html", "en/blog/index.html"):
    if not (root / route).is_file():
        errors.append(f"Missing required page: /{route}")

xml_files = sorted(root.glob("**/*.xml"))
for path in xml_files:
    try:
        ET.parse(path)
    except ET.ParseError as error:
        errors.append(f"{path.relative_to(root)}: invalid XML: {error}")

if errors:
    for error in sorted(set(errors)):
        print(f"FAIL {error}")
    raise SystemExit(1)
print(f"OK: {len(pages)} HTML pages, internal links and ES/EN alternatives; {len(xml_files)} valid XML files.")
