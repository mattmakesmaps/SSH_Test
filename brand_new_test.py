__author__ = 'matt'

import string

print 'Begin Count'

def countEm(input, express):
    cnt = string.count(input, express)
    return cnt

print countEm('hey hey hey', 'hey')