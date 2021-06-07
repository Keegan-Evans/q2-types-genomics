# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from q2_types_genomics.nog import NOG
from qiime2.plugin.testing import TestPluginBase

class TestType(TestPluginBase):
    package = 'q2_types_genomics.nog.tests'

    def test_nog_semantic_type_registration(self):
        self.assertRegisteredSemanticType(NOG)

if __name__ == '__main__':
    unittest.main()
