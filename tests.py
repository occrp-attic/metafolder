import os
import shutil
import unittest
import tempfile

import metafolder

LOCAL_PATH = os.path.dirname(__file__)


class TestMetaFolder(unittest.TestCase):

    def setUp(self):
        self.mf_path = tempfile.mkdtemp()
        self.mf = metafolder.open(self.mf_path)

    def tearDown(self):
        self.mf.close()
        shutil.rmtree(self.mf_path)

    def test_basic(self):
        for item in self.mf:
            raise KeyError("Already contains a thing!")

        ident = 'README'
        self.mf.add_file(os.path.join(LOCAL_PATH, 'README.md'),
                         identifier=ident, meta={'foo': 'bar'})

        item = self.mf.get(ident)
        assert 'README' in repr(item), repr(item)
        assert item.meta['foo'] == 'bar', item.meta

        for item in self.mf:
            assert item.identifier == ident

    def test_in_out(self):
        ident = 'banana foo'
        self.mf.add_file(__file__, identifier=ident, meta={'foo': 'bar'})
        item = self.mf.get(ident)
        assert ident in item.data, item.data


if __name__ == '__main__':
    unittest.main()
