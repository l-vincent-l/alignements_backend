from .db import DB
from itertools import permutations
from hashlib import md5

class Notion(object):
    def __init__(self, *uris):
        if len(uris) < 2:
            raise ValueError()
        self.uris = list(filter(lambda s: s and len(s) > 0, uris))
        self.add_to_db()
        self.uris = self.get_uris(self.uris[0])

    def add_to_db(self):
        list(map(self.add_uri, permutations(self.uris)))

    @classmethod
    def make_id(cls, uri):
       return 'notion:' + str(md5(uri.encode('utf-8')).hexdigest())

    @classmethod
    def add_uri(cls, uris):
        DB.sadd(cls.make_id(uris[0]), *uris[1:])

    @classmethod
    def get_uris(cls, uri):
        return list(map(lambda b: b.decode('utf8'),
            DB.sscan_iter(cls.make_id(uri))))
