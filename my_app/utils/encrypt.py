from django.conf import settings
import hashlib


def md5(data_string):
    
    if data_string is not None:
        obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
        obj.update(data_string.encode('utf-8'))
        return obj.hexdigest()
    else:
        data_string = ''
