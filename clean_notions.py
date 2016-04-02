from alignements_backend.db import DB

if __name__ == '__main__':
    for k in DB.iterscan(match='notion*'):
        DB.srem(k, "")
