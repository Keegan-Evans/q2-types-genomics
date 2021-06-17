# import os
# import unittest
# import pkg_resources
# 
# from qiime2.plugin import ValidationError
# 
# class TestUtils(unittest.TestCase):
#     package = 'q2_types_genomics.util.tests'
# 
#     cases = {
#         'pound_commented_labels': ('#', True, 3, False),
#         'pound_uncommented_labels': ('#', False, 3, False),
#     }
# 
#     def test_missing_features(self):
#         input_features = ['one', 'two', 'three']
#         required_features = ['one', 'two', 'four']
# 
#         with self.assertRaisesRegex(ValidationError, 'Required feature'):
#             _util.verify_features(input_features, required_features)
# 
#     def required_features_present(self):
#         input_features = ['one', 'two', 'three']
#         required_features = ['one', 'two', 'three']
# 
#         self.assertIsNone(
#             util.verify_features(input_features, required_features)
#         )
# 
# 
# 
#     def test_first_data_line(self, data):
# 
#         for filename, params in self.cases.items():
# 
#             filepath = pkg_resources.resource_filename(self.package,
#                                                        'data/%s' % filename)
#             filepath = self.get_data_path(filename=filename)
#             with open(filepath, 'r') as fh:
#                 data = fh.readlines()
# 
#             first_data_line = util.index_of_first_data_line(data,
#                                                                params[0],
#                                                                params[1]
#                                                                )
#             self.assertEqual(first_data_line, params[2])
# 
#     def test_get_feature_labels(self):
#         exp = ['Feature one', 'dos', 'third']
# 
#         for filename, params in self.cases.items():
#             filepath = self.get_data_path(filename=filename)
#             with open(filepath, 'r') as fh:
#                 data = fh.readlines()
# 
#             obs = util.find_feature_labels(data,
#                                       comment_character=params[0],
#                                       commented_labels=params[1],
#                                       headerless=params[3])
#             self.assertEqual(exp, obs)
# 
# if __name__ == '__main__':
#     unittest.main()
