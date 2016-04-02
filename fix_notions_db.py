from alignements_backend.db import DB
from alignements_backend.notion import Notion

for notion in DB.scan_iter(match='notion:*'):
    n = Notion(list(DB.sscan_iter(notion)))

