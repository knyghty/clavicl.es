AUTHOR = "Clavicles"
SITENAME = "Clav's Place"
SITEURL = "http://localhost:8000"

PATH = "content"
THEME = "themes/clavicles"

TIMEZONE = "Europe/Amsterdam"

DEFAULT_DATE_FORMAT = "%A %-d %B %Y"
DEFAULT_LANG = "en-GB"

DEFAULT_CATEGORY = "misc"
USE_FOLDER_AS_CATEGORY = False

DIRECT_TEMPLATES = ["index", "tags", "archives"]

ARCHIVES_SAVE_AS = "archives/index.html"
ARTICLE_PATHS = ["articles"]
ARTICLE_URL = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html"
PAGE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}/"
TAGS_SAVE_AS = "tags/index.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = []

# Social widget
SOCIAL = []

DEFAULT_PAGINATION = 10

# Sitemap.
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "pages": 0.5, "indexes": 0.2},
    "changefreqs": {"articles": "yearly", "pages": "monthly", "indexes": "weekly"},
}

# Webassets.
WEBASSETS_CONFIG = [
    ("url_expire", True),
]
