# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import importlib

from ._format import (
        EggnogRefTextFileFmt, 
        EggnogOutputDirFmt, PfamDirFmt, DiamondRefDirFmt, MMseqsDirFmt,
        ArbitraryHeaderTSVFmt, ArbitraryHeaderTSVDirFmt, BinaryReferenceDBDirFmt, OrthologDirFmt, DiamondIndexFileFmt, DiamondIndexDirFmt
        )

from ._type import (
        Ortholog, Seed, ReferenceDB, Annotation, NOG, KEGG, OG, Eggnog, Diamond, MMseq2,
        )


__all__ = [
        'EggnogRefDirFmt',
        'EggnogOutputDirFmt', 'Eggnog', 'ReferenceDB', 'PfamDirFmt',
        'DiamondRefDirFmt',  'MMseqsDirFmt', 'Ortholog', 'Seed', 'ArbitraryHeaderTSVFmt',
        'ArbitraryHeaderTSVDirFmt', 'KEGG', 'OG', 'Diamond', 'MMseq2',
        'NOG', 'BinaryReferenceDBDirFmt', 'OrthologDirFmt',  'DiamondIndexFileFmt', 'DiamondIndexDirFmt',
        ]

importlib.import_module('q2_types_genomics.eggnog._transformer')
importlib.import_module('q2_types_genomics.eggnog._validator')
    #'ArbitraryHeaderTSVDirFmt',
     #'BinaryReferenceDBFmt',
    #'BinaryReferenceDBDirFmt',
    #ArbitraryHeaderTSVDirFmt, #BinaryReferenceDBFmt, BinaryReferenceDBDirFmt,
