import os
import os.path

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

license = "# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.\n# SPDX-License-Identifier: Apache-2.0"
print(license)
print(type(license))
base_path = "/Users/fewu/Documents/tensorpack-mask-rcnn"
for dirpath, dirnames, filenames in os.walk(base_path):
    for filename in [f for f in filenames if f.endswith(".sh")]:
        file = dirpath + '/' +  filename
        line_prepender(file, license)
