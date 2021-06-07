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

    test_features =  [
        '#query_name',
        'seed_eggNOG_ortholog',
        'seed_ortholog_evalue',
        'seed_ortholog_score',
        'eggNOG OGs',
        'narr_og_name',
        'narr_og_cat',
        'narr_og_desc',
        'best_og_name',
        'best_og_cat',
        'best_og_desc',
        'Preferred_name',
        'GOs',
        'EC',
        'KEGG_ko',
        'KEGG_Pathway',
        'KEGG_Module',
        'KEGG_Reaction',
        'KEGG_rclass',
        'BRITE',
        'KEGG_TC',
        'CAZy',
        'BiGG_Reaction',
        'PFAMs',
        ]


    def _validate_(self, level):
        record_count = {'min': 5, 'max': None}
        self._check_schema()

    def _check_schema(self, header: bool = True):

        with self.open() as fh:

            previous_line = None

            for i, line in enumerate(fh, 0):
                if i > 10:
                    break

                parsed_line = line.split('\t')

                if parsed_line[0] == '#query_name':
                    self._check_features(file_features=parsed_line,
                                        test_features=self.test_features)
                elif parsed_line[0][1] == '#':
                    continue
                else:
                    ValidationError('No header information found')

    def _check_features(self, file_features, test_features):
        print('number in input file: %s' % len(file_features))
        print('number in test file: %s' % len(test_features))
        if file_features == test_features:
            True
        else:
            ValidationError('Incorrect features in data')

EggnogDirFmt = model.SingleFileDirectoryFormat(
                   'EggnogDirFmt', 'annotated.tsv', EggnogFmt)


plugin.register_formats(EggnogFmt, EggnogDirFmt)
