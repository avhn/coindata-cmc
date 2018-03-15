import unittest
import os
import coindata

_possible_input_formats = ('btc', 'BTC', 'bitcoin', 'BITCOIN')


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


class TestBuild(unittest.TestCase):
    
    def test_retrieve(self):
        """Try retrieve with all possible inputs."""

        for inp in _possible_input_formats:
            output = coindata.retrieve(inp)

            if not output:
                raise ValueError()
            
    def test_write_read(self):
        """Compare retrieve and read outputs."""
        
        # retrieve
        data = coindata.retrieve('btc')

        # write and read
        dir_test = os.path.dirname(os.path.realpath(__file__))
        file_path = coindata.write('btc', dir_test)
        data_comp = coindata.read(file_path)
        
        # clean up
        os.remove(file_path)

        # test
        if not is_same(data, data_comp):
            raise ValueError()


if __name__ == "__main__":
    unittest.main()

