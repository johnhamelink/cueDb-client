import hashes
import api

# For Walking through the directory and finding cues
import fnmatch
import os

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


print "Finding flacs with cuesheets..."
files = find_files(os.getcwd(), '*.flac')
for filename in files:

    cues =  find_files(os.path.dirname(filename), '*.cue')

    for cue in cues:
        f = file(filename, 'r')
        while True:
            t = f.read(1024)
            if len(t) == 0: break
            hashes.updateHashes(t)

        hashes.showResult(filename, cue)
        api.sendToApi(filename, cue)
        hashes.resetHashes()
