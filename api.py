import hashes
from mutagen.flac import FLAC # For reading flac metadata
# For uploading the Cuesheets to the API
import pycurl
from cStringIO import StringIO
import json

def sendToApi(flac, cue):
    audio = FLAC(flac)

    if ("artist" in audio and "album" in audio ):
        artist = str(audio["artist"][0])
        album = str(audio["album"][0])
    else:
        print "Skipped", flac, "because it doesn't have an artist or album tag"
        return -1

    c = pycurl.Curl()
    c.setopt(pycurl.URL, 'http://cuedb.local/index.php/add')
    c.setopt(c.POST, 1)
    c.setopt(c.HTTPPOST, [
        ('md5', hashes.getMd5()),
        ('sha1', hashes.getSha1()),
        ('sha256', hashes.getSha256()),
        ('crc32', hashes.getCrc32()),
        ('artist', artist),
        ('album', album),
        ('cuesheet', (pycurl.FORM_FILE, cue))
    ])

    response = StringIO()
    c.setopt(c.WRITEFUNCTION, response.write)
    c.perform()
    response = json.loads(response.getvalue())

    if (response['success'] == False):
        response['success'] = "Unsuccessful"
    else:
        response['success'] = "Successful"

    print response['success'] , " - ", response['message']
    print ""
    print "---"
    print ""
