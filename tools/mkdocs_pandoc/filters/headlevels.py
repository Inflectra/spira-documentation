# Copyright 2015 Johannes Grassler <johannes@btw23.de>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import re

# TODO: Implement handling for Setext style headers.

class HeadlevelFilter(object):
    """Filter for increasing Markdown header levels (only Atx style)"""

    def __init__(self, pages):
        max_offset = 0

        # Determine maximum header level from nesting in mkdocs.yml
        for page in pages:
            if page['level'] > max_offset:
                max_offset = page['level']

        self.offset = max_offset


    def run(self, lines):
        """Filter method"""
        ret = []

        # ret = lines[1:]

        first_line = 0
        for line in lines:
            first_line = first_line + 1
            if len(line.strip())>0:
                break

        # Tanur
        # Make all ## Headers to be #### headers (i.e. 2,3,4 => 4, 5, 6)
        for line in lines[first_line:]:
            ret.append(re.sub(r'^#', '###', line))

#        for line in lines[1:]:
#            ret.append(re.sub(r'^#', '#' + ('#' * self.offset), line))

        return ret
