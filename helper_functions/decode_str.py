import chardet


def decode_str(string):
    encoding = None
    try:
        enc = chardet.detect(string)
    except:
        pass
    try:
        if enc["confidence"] < 0.75:
            encoding = "cp1251"
        else:
            encoding = enc["encoding"]
    except:
        pass    
    try:
        return string.decode(encoding=encoding)
    except:
        return string