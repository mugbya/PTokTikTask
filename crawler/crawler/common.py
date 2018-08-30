# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import binascii
import base64, hashlib
from crawler.settings import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD
import redis
import sys
from you_get import common as you_get

AES_KEY = b'1qazXSW@3edcVFR$'
AES_IV = b'0okmNJI(8uhbVGY&'
CHUNKSIZE = 10000

CNT = 0


def decrypt(message):
    cipher = AES.new(AES_KEY, mode=AES.MODE_CBC, IV=AES_IV)
    bytestr = binascii.a2b_hex(message)
    plaintext = cipher.decrypt(bytestr)
    return to_str(plaintext.rstrip())


def encrypt(message):
    cipher = AES.new(AES_KEY, mode=AES.MODE_CBC, IV=AES_IV)

    length = len(message)
    mod = length % AES.block_size
    if mod > 0:
        width = length + AES.block_size - mod
        message = message.ljust(width)
    encrypted_message = cipher.encrypt(message)
    return binascii.b2a_hex(encrypted_message)


def hash(str):
    return hashlib.sha1(str.encode('utf-8')).hexdigest()


def get_redis_client(redis_db=None):
    pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, password=to_str(decrypt(REDIS_PASSWORD)))
    if redis_db:
        pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, password=to_str(decrypt(REDIS_PASSWORD)),
                                    db=redis_db)
    rc = redis.Redis(connection_pool=pool)
    return rc


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


def download(uri):
    '''
    视频下载
    :param self:
    :param uri:
    :return:
    '''
    sys.argv = ['you-get', uri]
    you_get.main()


redis_client = get_redis_client(redis_db=REDIS_DB)
