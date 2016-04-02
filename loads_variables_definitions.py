import json, sys
from alignements_backend.db import DB
from alignements_backend.variable import Variable

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        j = json.load(f)
    for k, v in j.items():
        DB.set(Variable.make_id(k), json.dumps(v))

