#!/usr/bin/env python
#encoding: utf-8

import unittest
import TW
import testcase as tc




class mytest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testgetSnapshot(self):
        self.assertEqual(TW.getSnapshot(tc.tcidata1, tc.tciid1), tc.tco1,
                         'error from testcase 1')
        self.assertEqual(TW.getSnapshot(tc.tcidata2, tc.tciid2), tc.tco2,
                         'error from testcase 2')
        self.assertEqual(TW.getSnapshot(tc.tcidata3, tc.tciid3), tc.tco3,
                         'error from testcase 3')
        self.assertEqual(TW.getSnapshot(tc.tcidata4, tc.tciid4), tc.tco4,
                         'error from testcase 4')
        self.assertEqual(TW.getSnapshot(tc.tcidata5, tc.tciid5), tc.tco5,
                         'error from testcase 5')
        self.assertEqual(TW.getSnapshot(tc.tcidata6, tc.tciid6), tc.tco6,
                         'error from testcase 6')
        self.assertEqual(TW.getSnapshot(tc.tcidata7, tc.tciid7), tc.tco7,
                         'error from testcase 7')


if __name__ == '__main__':
    unittest.main()