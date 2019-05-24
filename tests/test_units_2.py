import unittest
import logging


### Logging
log_lvl = logging.DEBUG
logging.basicConfig(filename='test.log', level=log_lvl, filemode='w')
logging.getLogger().addHandler(logging.StreamHandler())
logging.debug("LOGGING LEVEL: " + str(log_lvl))

class Unit2Tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Unit2Tests, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        # declaring params so we can easily modify them for all tests
        # stuff that's we don't need to reset between tests
        pass

    @classmethod
    def tearDownClass(cls):
        # stop things / shutdown
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        print("Unit 2 test 1 fails")
        self.assertTrue(False)

    def test_2(self):
        print("Unit 2 test 2 succeeds")
        self.assertTrue(True)

unittest.main()
