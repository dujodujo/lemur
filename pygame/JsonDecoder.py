import json

class JsonDecoder(object):
    @classmethod
    def load(cls, path):
        def decode_list(lst):
            newlist = []
            for i in lst:
                if isinstance(i, unicode):
                    i = i.encode('utf-8')
                elif isinstance(i, list):
                    i = decode_list(i)
                newlist.append(i)
            return newlist

        def decode_dict(dct):
            newdict = {}
            for k, v in dct.iteritems():
                if isinstance(k, unicode):
                    try:
                        k = int(k)
                    except ValueError:
                        k = k.encode('utf-8')
                if isinstance(v, unicode):
                    v = v.encode('utf-8')
                elif isinstance(v, list):
                    v = decode_list(v)
                newdict[k] = v
            return newdict

        with open(path, "rb") as file:
            return json.load(file, encoding="ascii", object_hook=decode_dict)