import os
import hashlib # For md5, sha1, sha256
import crc32

md5    = hashlib.md5()
sha1   = hashlib.sha1()
sha256 = hashlib.sha256()
crc32  = hashlib.crc32()

def getMd5():
    return md5.hexdigest()

def getSha1():
    return sha1.hexdigest()

def getSha256():
    return sha256.hexdigest()

def getCrc32():
    return crc32.hexdigest()

def updateHashes(t):
    md5.update(t)
    crc32.update(t)
    sha1.update(t)
    sha256.update(t)

def resetHashes():
    md5    = hashlib.md5()
    sha1   = hashlib.sha1()
    sha256 = hashlib.sha256()
    crc32  = hashlib.crc32()

def showResult(flac, cue):
    print os.path.basename(flac), ":"
    print "md5\t-", getMd5()
    print "sha1\t-", getSha1()
    print "sha256\t-", getSha256()
    print "crc32\t-", getCrc32()
    print ""
    print "Associating with", os.path.basename(cue)
    print ""
