
import hmac
import hashlib
import binascii
import random

class Hmac_functions:
    def generate_key(self):
        return binascii.hexlify(random.randbytes(16)).decode()

    def generate_hmac(self, key, message):
        key_bytes = key.encode('utf-8')
        message_bytes = message.encode('utf-8')
        hmac_obj = hmac.new(key_bytes, message_bytes, hashlib.sha256)
        return hmac_obj.hexdigest()