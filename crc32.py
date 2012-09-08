import hashlib # For md5, sha1, sha256
import zlib    # For crc32

class CRC32(object):
    name = 'crc32'
    digest_size = 4
    block_size = 64

    def __init__(self, arg=''):
        self.__hash = 0
        self.update(arg)

    def copy(self):
        return self

    def digest(self):
        return self.__hash & 0xffffffff

    def hexdigest(self):
        return '%08x' % (self.digest())

    def update(self, arg):
        self.__hash = zlib.crc32(arg, self.__hash)

hashlib.crc32 = CRC32
