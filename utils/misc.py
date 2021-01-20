""" Various auxiliary utilities """


def rename_dict_key(dct, src_key, dst_key):
    dct[dst_key] = dct[src_key]
    del dct[src_key]
    return dct
