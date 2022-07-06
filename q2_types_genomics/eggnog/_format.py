# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import re
from ._util import parse_header_line, parse_footer_line

import qiime2.plugin.model as model

from ..plugin_setup import plugin


class ArbitraryHeaderTSVFmt(model.TextFileFormat):
    def _check_seperator(self, level):
        with self.open() as fh:
            for i, line in enumerate(fh, 1):
                if (not re.search(r'\t', line) and
                        i >= self.header + 1 and i < self.footer):
                    raise ValueError("No correct separator detected in input "
                                     "file on line: {}".format(i))

                if i == level:
                    break

    def _validate_(self, level):
        self._check_seperator(level={'min': 5, 'max': None}[level])

    @property
    def header(self):
        return parse_header_line(self)

    @property
    def footer(self):
        return parse_footer_line(self)


class HeaderlessArbitraryHeaderTSVFmt(ArbitraryHeaderTSVFmt):
    pass


plugin.register_formats(ArbitraryHeaderTSVFmt)

ArbitraryHeaderTSVDirFmt = model.SingleFileDirectoryFormat(
                                 'ArbitraryHeaderTSVDirFmt',
                                 'eggnog.tsv',
                                 ArbitraryHeaderTSVFmt)

plugin.register_formats(ArbitraryHeaderTSVDirFmt)
