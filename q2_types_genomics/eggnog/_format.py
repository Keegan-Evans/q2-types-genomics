# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from qiime2.plugin import model
from q2_types_genomics.feature_data._util import (
        parse_header_line, parse_footer_line,
        )

from qiime2.plugin import ValidationError

from ..plugin_setup import plugin

import re

class DiamondIndexFileFmt(model.BinaryFileFormat):
    def _validate_(self, level):
        pass


plugin.register_formats(DiamondIndexFileFmt)

class EggnogRefTextFileFmt(model.TextFileFormat):
    def _validate_(self, level):
        pass


plugin.register_formats(EggnogRefTextFileFmt)

# Below is the definition for a Directory Format to hold all of the refer
# databases for eggnog mapper, this probably should be moved somewhere else in
# the future, possibly an eggnog specificy module in this plugin

class HmmerDirFmt(model.DirectoryFormat):
    pass


plugin.register_formats(HmmerDirFmt)


class MMseqsDirFmt(model.DirectoryFormat):
    mmseqs_db=model.File(r"mmseqs.db",
                      format=EggnogRefBinFileFmt,
                      optional=False)

    mmseqs_dbtype=model.File(r"mmseqs.db.dbtype",
                      format=EggnogRefBinFileFmt,
                      optional=False)

    mmseqs_index=model.File(r"mmseqs.db.index",
                            format=EggnogRefBinFileFmt,
                            optional=False)

    mmseqs_lookup=model.File(r"mmseqs.db.lookup",
                             format=EggnogRefBinFileFmt,
                             optional=True)

    mmseqs_source=model.File(r"mmseqs.db.source",
                             format=EggnogRefBinFileFmt,
                             optional=True)

    mmseqs_h_db=model.File(r"mmseqs.db_h",
                           format=EggnogRefBinFileFmt,
                           optional=True)

    mmseqs_h_dbtype=model.File(r"mmseqs.db_h.dbtype",
                               format=EggnogRefBinFileFmt,
                               optional=True)

    mmseqs_h_index=model.File(r"mmseqs.db_h.index",
                              format=EggnogRefBinFileFmt,
                              optional=True)


plugin.register_formats(MMseqsDirFmt)


class PfamDirFmt(model.DirectoryFormat):

    clans=model.File(r"Pfam-A.clans.tsv.gz",
                       format=EggnogRefBinFileFmt,
                       optional=False)

    base=model.File(r"Pfam-A.hmm",
                       format=EggnogRefBinFileFmt,
                       optional=False)

    h3f=model.File(r"Pfam-A.hmm.h3f",
                       format=EggnogRefBinFileFmt,
                       optional=False)

    h3i=model.File(r"Pfam-A.hmm.h3i",
                    format=EggnogRefBinFileFmt,
                    optional=False)

    h3m=model.File(r"Pfam-A.hmm.h3m",
                     format=EggnogRefBinFileFmt,
                     optional=False)

    ssi=model.File(r"Pfam-A.hmm.h3m.ssi",
                       format=EggnogRefBinFileFmt,
                       optional=False)

    h3p=model.File(r"Pfam-A.hmm.h3p",
                       format=EggnogRefBinFileFmt,
                       optional=False)

    idmap=model.File(r"Pfam-A.hmm.idmap",
                       format=EggnogRefBinFileFmt,
                       optional=False)


plugin.register_formats(PfamDirFmt)


DiamondIndexDirFmt = model.SingleFileDirectoryFormat('index.dmnd', DiamondIndexFileFmt)

plugin.register_formats(DiamondIndexDirFmt)



class EggnogRefDirFmt(model.DirectoryFormat):

    eggnog_db = model.File(r"eggnog\.db",
                           format=EggnogRefBinFileFmt,
                           optional=True)

    eggnog_taxa = model.File(r"eggnog\.taxa\.db",
                            format=EggnogRefBinFileFmt,
                            optional=True)

    eggnog_taxa_pkl = model.File(r"eggnog.taxa.db.traverse.pkl",
                                 format=EggnogRefBinFileFmt,
                                 optional=True)

"""
eggnog.db
eggnog.taxa.db
eggnog.taxa.db.traverse.pkl
eggnog_proteins.dmnd
novel_fams.dmnd

hmmer
mmseqs
pfam
"""

plugin.register_formats(EggnogRefDirFmt)


class EggnogOutputDirFmt(model.DirectoryFormat):
    annotations = model.File(r".*\..*\.annotations",
                             format=EggnogRefBinFileFmt)

    gene_pred_seqs = model.File(r".*\.*\.genepred\.fasta",
                                format=EggnogRefTextFileFmt
                                )

    gene_pred_gff = model.File(r".*\..*\.genepred.gff",
                               format=EggnogRefTextFileFmt
                               )

    seed_orthologs = model.File(r".*\..*\.seed_orthologs",
                                format=EggnogRefTextFileFmt
                                )


plugin.register_formats(EggnogOutputDirFmt)


# GenericTSVfmt
class ArbitraryHeaderTSVFmt(model.TextFileFormat):
    """This format is for files written as TSVs with arbitrary header and/or
    footer lengths and locations, verification of content should be performed
    using Semantic Validators"""

    def _check_seperator(self, level):
        with self.open() as fh:
            for i, line in enumerate(fh, 1):
                if (not re.search(r'\t', line) and
                        self.header + 1 <= i < self.footer):
                    raise ValidationError("No correct separator detected in"
                                          " input file on line: {}".format(i))

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


plugin.register_formats(ArbitraryHeaderTSVFmt)

ArbitraryHeaderTSVDirFmt = model.SingleFileDirectoryFormat(
                                 'ArbitraryHeaderTSVDirFmt',
                                 'data.tsv',
                                 ArbitraryHeaderTSVFmt)

plugin.register_formats(ArbitraryHeaderTSVDirFmt)


# binary reference
## I THINK WE CAN REMOVE, each reference database needs own definition given the variety of files which could be in each
class BinaryReferenceDBFmt(model.BinaryFileFormat):
    """A format to hold reference data, originally created for the diamond
    formatted reference database information needed for Eggnog Mapper"""

    def _validate_(self, level):
        bad_lines = []
        try:
            contents = self.open().readlines()
            for line, content in enumerate(contents, 1):
                if not isinstance(content, bytes):
                    bad_lines.append(line)
            if bad_lines:
                raise ValueError
        except ValueError:
            raise ValueError("Your reference database appears to contain"
                             " non-byte strings on lines: {}".format(
                                 ", ".join(bad_lines)))
        except Exception as e:
            raise e


BinaryReferenceDBDirFmt = model.SingleFileDirectoryFormat(
        'BinaryReferenceDBDirFmt', 'reference_database',
        BinaryReferenceDBFmt)

plugin.register_formats(
    BinaryReferenceDBFmt, BinaryReferenceDBDirFmt
    )


#   /Users/keeganevans/Desktop/search_diamond/manual.emapper.genepred.fasta
#   /Users/keeganevans/Desktop/search_diamond/manual.emapper.genepred.gff
#   /Users/keeganevans/Desktop/search_diamond/manual.emapper.hits
#   /Users/keeganevans/Desktop/search_diamond/manual.emapper.seed_orthologs
class OrthologDirFmt(model.DirectoryFormat):
    orthologs = model.FileCollection(r'.+\.emapper\.seed_orthologs$',
                                     format=EggnogRefTextFileFmt,
                                     optional=True)
    @orthologs.set_path_maker
    def orthologs_path_maker(self, sample_id):
        return r'%s\.seed_ortholog' % sample_id


    hits = model.FileCollection(r'.+\.hits$',
                                format=EggnogRefTextFileFmt,
                                optional=True)

    @hits.set_path_maker
    def hits_path_maker(self, sample_id):
        return r'%s\.hits' % sample_id

    genepred_gff = model.FileCollection(r'.+\.emapper\.genepred\.gff$',
                                        format=EggnogRefBinFileFmt,
                                        optional=True)
    @genepred_gff.set_path_maker
    def hits_path_maker(self, sample_id):
        return r'%s\.genepred\.gff' % sample_id

    genepred_fasta = model.FileCollection(r'.+\.emapper\.genepred\.(fa|fasta)$',
                                          format=EggnogRefTextFileFmt,
                                          optional=True)
    @genepred_fasta.set_path_maker
    def hits_path_maker(self, sample_id):
        return r'%s\.genepred\.fasta' % sample_id


#OrthologDirFmt = model.SingleFileDirectoryFormat(
#                     'OrthologDirFmt',
#                     'orthologs.tsv',
#                     ArbitraryHeaderTSVFmt)

plugin.register_formats(OrthologDirFmt)
