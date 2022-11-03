# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from qiime2.plugin import SemanticType
from q2_types_genomics.plugin_setup import plugin

ReferenceDB = SemanticType('ReferenceDB', field_names='type')
Diamond = SemanticType('Diamond', variant_of=ReferenceDB.field['type'])
Eggnog = SemanticType('Eggnog', variant_of=ReferenceDB.field['type'])
MMseq = SemanticType('MMseq', variant_of=ReferenceDB.field['type'])

plugin.register_semantic_types(ReferenceDB, Diamond, Eggnog, MMseq)
