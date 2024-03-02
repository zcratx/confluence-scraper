# From Atlassian Developer console
CLIENT_ID = "…"
CLIENT_SECRET = "…"

# You can use an URL that does not exist! We don't run a webserver, we'll just manually copy
# the callback data to the terminal
CALLBACK_URL = "https://confluence-scraper.rami.io"

# Folder on disk where we store the downloaded content
DATA_FOLDER = "data"

# Exclude download of very large attachments:
MAX_ATTACHMENT_SIZE = 1024 * 1024 * 1024  # 1 GB