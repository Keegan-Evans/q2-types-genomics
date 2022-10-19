# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------



from ._format import EggnogRefDirFmt, EggnogOutputDirFmt, BinaryReferenceDBDirFmt, ArbitraryHeaderTSVDirFmt, ArbitraryHeaderTSVFmt, DiamondRefDirFmt, OrthologDirFmt
# ._format
#from q2_types_genomics.eggnog import EggnogRefDirFmt, EggnogOutputDirFmt, BinaryReferenceDBDirFmt
from qiime2.plugin import SemanticType, model

from ..plugin_setup import plugin




Ortholog = SemanticType('Ortholog', field_names='type')
Seed = SemanticType('Seed', variant_of=Ortholog.field['type'])

plugin.register_semantic_types(Ortholog, Seed)

plugin.register_semantic_type_to_format(
    Ortholog[Seed],
    artifact_format=OrthologDirFmt)

# TODO: ortholog validator

# FROM ORIGINAL DEFINITION IN FEATURE DATA

# NOG stuff

AnnotationDirFmt = model.SingleFileDirectoryFormat(
                       'AnnotationDirFmt',
                       'annotation.tsv',
                       ArbitraryHeaderTSVFmt)
plugin.register_formats(AnnotationDirFmt)

Annotation = SemanticType('Annotation', field_names='type')

plugin.register_semantic_types(Annotation)


NOG = SemanticType('NOG', variant_of=Annotation.field['type'])
plugin.register_semantic_types(NOG)
plugin.register_semantic_type_to_format(
    semantic_type=Annotation[NOG],
    artifact_format=AnnotationDirFmt
)

# KEGG stuff
KEGG = SemanticType('KEGG', variant_of=Annotation.field['type'])
plugin.register_semantic_types(KEGG)
plugin.register_semantic_type_to_format(
        semantic_type=Annotation[KEGG],
        artifact_format=AnnotationDirFmt
)

# OG stuff
OG = SemanticType('OG', variant_of=Annotation.field['type'])
plugin.register_semantic_types(OG)
plugin.register_semantic_type_to_format(
        semantic_type=Annotation[OG],
        artifact_format=AnnotationDirFmt
)

# types for downloading the databases eggnogmapper is using.
# base
ReferenceDB = SemanticType('ReferenceDB', field_names='type')
# eggnog

Eggnog = SemanticType('Eggnog', variant_of=ReferenceDB.field['type'])

plugin.register_semantic_types(ReferenceDB, Eggnog)

plugin.register_semantic_type_to_format(
    ReferenceDB[Eggnog],
    artifact_format=EggnogRefDirFmt
    )

# diamond
Diamond = SemanticType('Diamond', variant_of=ReferenceDB.field['type'])

plugin.register_semantic_types(Diamond)

plugin.register_semantic_type_to_format(
        ReferenceDB[Diamond],
        artifact_format=DiamondRefDirFmt
)


# mmseq2
MMseq2 = SemanticType('MMseq2', variant_of=ReferenceDB.field['type'])
plugin.register_semantic_types(MMseq2)
plugin.register_semantic_type_to_format(
        ReferenceDB[MMseq2],
        artifact_format=BinaryReferenceDBDirFmt
)

# EggnogDB = SemanticType('EggnogDB', variant_of=ReferenceDB.field['type'])
# plugin.register_semantic_types(EggnogDB)
# plugin.register_semantic_type_to_format(
#          EggnogDB,
#          artifact_format=BinaryReferenceDBDirFmt
#  )
