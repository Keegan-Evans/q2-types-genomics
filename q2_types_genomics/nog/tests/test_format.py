# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import os
import unittest

from .. import EggnogFmt

from qiime2.core.exceptions import ValidationError
from qiime2.plugin.testing import TestPluginBase

class TestNog(TestPluginBase):
    package = 'q2_types_genomics.nog.tests'

    def test_with_header_correct_columns(self):
        filename = 'eggnog_annotations.tsv'
        filepath = self.get_data_path(filename)
        egg = EggnogFmt(filepath, mode='r')
        egg.validate()

    def test_with_header_wrong_columns(self):
        filename = 'eggnog_annotations_incorrect_headers.tsv'
        filepath = self.get_data_path(filename)
        egg = EggnogFmt()
        with open(filepath, mode='r') as fh:
            egg = fh.readlines()
        print(egg)
        with self.assertRaisesRegex(ValidationError, 'EggnogFmt'):
            egg.validate()

class TestGOs:
    pass

class TestKegg:
    pass

if __name__ == '__main__':
    unittest.main()
