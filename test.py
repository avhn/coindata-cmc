import unittest
import os
import coindata


class TestBuild(unittest.TestCase):
    _possible_input_formats = ('btc', 'BTC', 'bitcoin', 'BITCOIN')

    @staticmethod
    def is_same(data1, data2):
        """Compare 2 coindata outputs."""

        # length case
        if not len(data1) == len(data2):
            return False

        # comparing keys
        for i in range(len(data1)):
            for key in data1[i]:
                if not data1[i][key] == data2[i][key]:
                    return False
    
                # passed
                return True

    def test_retrieve_with_all_input_formats(self):
        """Try retrieve with all possible input formats."""

        for inp in self._possible_input_formats:
            output = coindata.request.retrieve(inp)

            if not output:
                raise ValueError()
            
    def test_write_read(self):
        """Compare retrieve and read outputs."""
        
        # retrieve
        data = coindata.request.retrieve('btc')

        # write and read
        dir_test = os.path.dirname(os.path.realpath(__file__))
        file_path = coindata.request.write('btc', dir_test)
        data_comp = coindata.request.read(file_path)
        
        # clean up
        os.remove(file_path)

        # test
        if not self.is_same(data, data_comp):
            raise ValueError()

    def test_cache_and_get(self):
        """Compare cache and get's outputs."""

        coindata.cache('BITCOIN')
        coindata.get('btc')


if __name__ == "__main__":
    unittest.main()

