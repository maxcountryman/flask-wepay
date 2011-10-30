import unittest
import flask

from flaskext.wepay import WePay


class BasicTestCase(unittest.TestCase):
    
    def setUp(self):
        app = flask.Flask(__name__)
        wepay = WePay(app)


if __name__ == '__main__':
    unittest.main()
