# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import qiime2.plugin.model as model
from qiime2.plugin import ValidationError

from ..plugin_setup import plugin


class EggnogFmt(model.TextFileFormat):

    def _check_n_features(self, n):
        pass

    def _validate(self, level):
        record_count = {'min': 5, 'max': None}
        self._check_n_features(record_count[level])
        
EggnogDirFmt = model.SingleFileDirectoryFormat(
                   'EggnogDirFmt', 'annotated.tsv', EggnogFmt)


plugin.register_formats(EggnogFmt, EggnogDirFmt)
