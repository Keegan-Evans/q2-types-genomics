# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from collections import deque

def split_on_multiple(input_str, *seps):
    parts = deque([])
    parts.append(input_str)

    for sep in seps:
        for i in range(len(parts)):
            split_components = deque(parts.popleft().split(sep))
            while split_components:
                parts.append(split_components.popleft())
    return parts
