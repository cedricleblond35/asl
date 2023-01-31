import unittest
from model.admin import Admin
        
class TestAdmin(unittest.TestCase):
    def test_verifyName(self):
        admin = Admin()
        self.assertTrue(admin.verifyName("eva"))
        self.assertTrue(admin.verifyName("EvA"))
        self.assertTrue(admin.verifyName("eva-duchesse"))

        self.assertFalse(admin.verifyName("eva!"))
        self.assertFalse(admin.verifyName("eva essai"))
        self.assertFalse(admin.verifyName("eva@"))
    

    def test_verifyEmail(self):
        admin = Admin()
        self.assertTrue(admin.verifyEmail("evaili@yahoo.com"))
        self.assertTrue(admin.verifyEmail("eva.ili@yahoo.com"))
        self.assertFalse(admin.verifyEmail("eva.iliyahoo.com"))
        self.assertFalse(admin.verifyEmail("eva.ili@yahoo"))
        self.assertFalse(admin.verifyEmail("eva.ili@@yahoo.com"))
        
    def test_verifyPassword(self):
        admin = Admin()
        self.assertTrue(admin.verifyPassword("123soleil"))
        self.assertTrue(admin.verifyPassword("soleil!"))
        self.assertTrue(admin.verifyPassword("SolEil"))
        self.assertTrue(admin.verifyPassword("soleil!"))
        self.assertTrue(admin.verifyPassword("@soleil!"))
        self.assertTrue(admin.verifyPassword("soleil!+="))
        self.assertTrue(admin.verifyPassword("soleil!+=œ"))
        self.assertTrue(admin.verifyPassword("soleil!+=é"))
        self.assertFalse(admin.verifyPassword("so"))

