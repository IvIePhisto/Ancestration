import unittest
import doctest

class TestFamilyInheritance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import tests.family_a, tests.family_b
        cls._family_a = tests.family_a
        cls._family_b = tests.family_b
        cls._class_a_a = tests.family_a.ClassA()
        cls._class_a_b = tests.family_a.ClassB()
        cls._class_a_c = tests.family_a.ClassC()
        cls._class_b_a = tests.family_b.ClassA()
        cls._class_b_b = tests.family_b.ClassB()
        cls._class_b_c = tests.family_b.ClassC()

    def test_family_a_class_b(self):
        self.assertEqual(self._class_a_a.a(), self._class_a_b.a())
        self.assertNotEqual(self._class_a_a.b(), self._class_a_b.b())
        self.assertEqual(self._class_a_a.c(), self._class_a_b.c())

    def test_family_a_class_c(self):
        self.assertEqual(self._class_a_b.a(), self._class_a_c.a())
        self.assertEqual(self._class_a_b.b(), self._class_a_c.b())
        self.assertNotEqual(self._class_a_b.c(), self._class_a_c.c())

    def test_family_b_class_a(self):
        self.assertNotEqual(self._class_a_a.a(), self._class_b_a.a())
        self.assertEqual(self._class_a_a.b(), self._class_b_a.b())
        self.assertEqual(self._class_a_a.c(), self._class_b_a.c())

    def test_family_b_class_b(self):
        self.assertEqual(self._class_b_a.a(), self._class_b_b.a())
        self.assertEqual(self._class_a_b.b(), self._class_b_b.b())
        self.assertEqual(self._class_b_a.c(), self._class_b_b.c())
        self.assertEqual(self._class_b_a.d(), self._class_b_b.d())

    def test_family_b_class_c(self):
        self.assertEqual(self._class_a_c.a(), self._class_b_c.a())
        self.assertEqual(self._class_b_b.b(), self._class_b_c.b())
        self.assertNotEqual(self._class_b_b.c(), self._class_b_c.c())
        self.assertEqual(self._class_b_b.d(), self._class_b_c.d())

    def test_deferral(self):
        self.assertEqual(self._class_a_b.class_a(), self._family_a.ClassA)
        self.assertEqual(self._class_a_c.class_a(), self._family_a.ClassA)
        self.assertEqual(self._class_a_c.class_b(), self._family_a.ClassB)
        self.assertEqual(self._class_a_c.class_c(), self._family_a.ClassC)
        self.assertEqual(self._class_b_b.class_a(), self._family_b.ClassA)
        self.assertEqual(self._class_b_c.class_a(), self._family_b.ClassA)
        self.assertEqual(self._class_b_c.class_b(), self._family_b.ClassB)
        self.assertEqual(self._class_b_c.class_c(), self._family_b.ClassC)

    def test_family_function(self):
        self.assertEqual(self._family_a.a(), self._family_a.ClassA)
        self.assertEqual(self._family_b.a(), self._family_b.ClassA)
        self.assertEqual(self._family_a.b(), self._family_a.ClassB)
        self.assertEqual(self._family_b.b(), self._family_b.ClassB)

    def test_super_family(self):
        self.assertEqual(self._family_b.ClassC.super_family(), self._family_a)

    def test_class_override(self):
        a_b = self._family_a.ClassB()
        a_c = self._family_a.ClassC()
        self.assertNotEqual(a_b.override(), a_c.override())
        b_b = self._family_b.ClassB()
        b_c = self._family_b.ClassC()
        self.assertNotEqual(b_b.override(), b_c.override())
        self.assertEqual(a_b.override(), b_b.override())
        self.assertEqual(a_c.override(), b_c.override())

    def test_reload_family(self):
        self._family_a.reload_family()
        self._family_b.reload_family()

    def test_errors(self):
        from tests import errors
        from tests import extented_errors

def test_suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFamilyInheritance)
    import ancestration
    from doctest import DocTestSuite
    suite.addTests(DocTestSuite(ancestration))
    return suite
