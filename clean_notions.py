from alignements_backend.db import DB

if __name__ == '__main__':
    for k in DB.scan_iter(match='notion*'):
        DB.srem(k, "")
