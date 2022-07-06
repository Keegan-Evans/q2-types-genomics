# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib
from ._type import NOG

from ._format import (
    ArbitraryHeaderTSVFmt, ArbitraryHeaderTSVDirFmt
)
from q2_types.feature_data import FeatureData
from ..plugin_setup import plugin

plugin.register_semantic_type_to_format(
    semantic_type=FeatureData[NOG],
    artifact_format=ArbitraryHeaderTSVDirFmt
)
importlib.import_module('q2_types_genomics.eggnog._transformer')
importlib.import_module('q2_types_genomics.eggnog._validator')


__all__ = [
    'NOG', 'ArbitraryHeaderTSVFmt', 'ArbitraryHeaderTSVDirFmt',
]
