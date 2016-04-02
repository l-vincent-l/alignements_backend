from alignements_backend.db import DB

class Variable(object):
    @classmethod
    def make_id(cls, var_name):
        return 'variable:{}'.format(var_name)

    @classmethod
    def get_from_id(cls, var_name):
        id_ = DB.get(cls.make_id(var_name))
        if id_:
            return id_.decode('utf8')
        return None
