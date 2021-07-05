# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os.path
import unittest

from q2_types_genomics.eggnog._format import (
    EggnogBase, EggnogFmt, HeaderlessEggnogFmt, EggnogDirFmt,
)

from qiime2.plugin.testing import TestPluginBase



class TestBase(TestPluginBase):
    package = 'q2_types_genomics.eggnog.tests'

    def test_base_eggnog(self):
        filename = 'sample_eggnog_annotations.annotations'
        filepath = self.get_data_path(filename)

        fmt = EggnogBase(filepath, 'r')

        fmt.validate(level='max')

    def test_separator_incorrect(self):
        filename = 'sample_csv.csv'
        filepath = self.get_data_path(filename)

        fmt = EggnogBase(filepath, 'r')

        with self.assertRaisesRegex(ValueError,
                                    "Incorrect separator in file"
                                    ):
            fmt.validate()
        

    def test_encoding(self):
        pass

if __name__ == '__main__':
    unittest.main()
