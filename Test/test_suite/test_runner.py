import sys
import os

sys.path.append(sys.path[0] + "/...")
sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.test_demo_page import PHPTravelDemoHomePage
from Test.Scripts.test_authentication import AuthenticationAdminUser
from Test.Scripts.test_add_admin import AddNewAdmin
from Test.Scripts.test_edit_new_admin_permissions import EditNewAdmin
from Test.Scripts.test_login_with_new_admin import AuthenticationNewAdminUser

if __name__ == "__main__":
 
    test_loader = TestLoader()
    test_suite = TestSuite((
        #test_loader.loadTestsFromTestCase(PHPTravelDemoHomePage),
        test_loader.loadTestsFromTestCase(AuthenticationAdminUser),
        test_loader.loadTestsFromTestCase(AddNewAdmin),
        test_loader.loadTestsFromTestCase(EditNewAdmin),
        test_loader.loadTestsFromTestCase(AuthenticationNewAdminUser)
        ))
 
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
