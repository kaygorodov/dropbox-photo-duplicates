"""
Removing duplicate photos in the dropbox folder Camera Uploads
"""

import os
import re

cur_dir = os.path.dirname(os.path.realpath(__file__))
list_files = os.listdir(cur_dir)

counter = 0

for name in list_files:
    res = re.match(r'(^.*?)-\d+?\.jpg$', name)
    if res:
        if res.groups()[0] + ".jpg" in list_files:
            full_name = os.path.join(cur_dir, name)
            os.remove(full_name)
            counter += 1
            print name

print "\ntotally removed {} files".format(counter)
