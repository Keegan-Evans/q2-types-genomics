# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from qiime2.plugin import model
from q2_types_genomics.plugin_setup import plugin
from q2_types_genomics.reference_db import ReferenceDB, MMseq

class MMseqDatabaseFileFmt(model.BinaryFileFormat):
    def _validate_(self, level):
        # TODO: have native diamond validation run on db/self.path
        pass


class MMseqRefDatabaseDirFmt(model.DirectoryFormat):
    main_db = model.File(r'mmseqs',
                         format=MMseqDatabaseFileFmt)
    db_type = model.File(r'mmseqs\.dbtype',
                         format=MMseqDatabaseFileFmt)
    lookup = model.File(r'mmseqs\.lookup',
                        format=MMseqDatabaseFileFmt)
    source = model.File(r'mmseqs\.source',
                        format=MMseqDatabaseFileFmt)
    idx = model.File(r'mmseqs\.index',
                     format=MMseqDatabaseFileFmt)
    mmseqs_h = model.File(r'mmseqs_h',
                         format=MMseqDatabaseFileFmt)
    db_h_type = model.File(r'mmseqs_h\.dbtype',
                         format=MMseqDatabaseFileFmt)
    idx_h = model.File(r'mmseqs_h\.index',
                        format=MMseqDatabaseFileFmt)

#        name_components = split_on_multiple(name, ".", "_")
#
#        name_components[0] = "mmseqs"
#        name_components.insert(1, "db")
#
#        if name_components[2] == "db":
#            name_components.pop(2)
#
#        if "h" in name_components:
#            name_components.pop(name_components.index("h"))
#            name_components[1] = "db_h"
#        out_name =  ".".join(name_components)
#        return out_name


    # @mmseqs.set_path_maker
    # def mmseqs_pathmaker(self, name):
    #     name_components = name.split(".")
    #     if 'db' in name_components:
    #         name_components.remove(name_components.index('db'))
    #     if len(name_components) == 1:
    #         out_name = "mmseqs.db"
    #     else:
    #         out_name = "mmseqs.db" + ".".join(name_components[1:])

    #     return str(out_name)

# # replace with general directory format
# MMseqRefDatabaseDirFmt = model.SingleFileDirectoryFormat(
#     'MMseqRefDatabaseDirFmt', 'ref_db.dmnd', MMseqDatabaseFileFmt)

plugin.register_formats(MMseqDatabaseFileFmt, MMseqRefDatabaseDirFmt)
plugin.register_semantic_type_to_format(ReferenceDB[MMseq],
                                        MMseqRefDatabaseDirFmt)
