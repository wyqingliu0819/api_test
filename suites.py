import unittest

from testcase.test_reg import TestReg

from testcase.test_login import TestLogin

# suite = unittest.TestSuite()
# suite.addTest(TestLogin('test_login_normal'))
# suite.addTests([TestLogin('test_login_normal'),
#                TestLogin('test_login_password_wrong')])

smoke_suite = unittest.TestSuite()
smoke_suite.addTests([TestLogin('test_login_normal'),
                     TestReg('test_reg_normal')])

if __name__ == '__main__':
    # print(suite)
    # print(suite.countTestCases())

    unittest.TextTestRunner(verbosity=2).run(smoke_suite)