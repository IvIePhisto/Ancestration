from ancestration import (family, family_class, family_function, class_module,
    FamilyInheritanceError)

try:
    @family_class
    class Test(object):
        pass
except FamilyInheritanceError:
    pass
else:
    raise RuntimeError(FamilyInheritanceError)

try:
    @family_function
    def test():
        pass
except FamilyInheritanceError:
    pass
else:
    raise RuntimeError(FamilyInheritanceError)

try:
    family('NONEXISTENT')
except ImportError:
    pass
else:
    raise RuntimeError(ImportError)

try:
    import ancestration
    family(ancestration)
except FamilyInheritanceError:
    pass
else:
    raise RuntimeError(FamilyInheritanceError)

family()

try:
    family()
except FamilyInheritanceError:
    pass
else:
    raise RuntimeError(FamilyInheritanceError)


@family_class
class TestA(object):
    module = class_module

a = TestA()
try:
    del a.module
except AttributeError:
    pass
else:
    raise RuntimeError(AttributeError)
try:
    a.module = None
except AttributeError:
    pass
else:
    raise RuntimeError(AttributeError)
del a

@family_class
class TestB(object):
    pass

try:
    @family_class
    class TestC(TestA, TestB):
        pass
except FamilyInheritanceError:
    pass
else:
    raise RuntimeError(FamilyInheritanceError)

try:
    @family_class
    class TestB(TestA):
        pass
except FamilyInheritanceError:
    pass
else:
    raise RuntimeError(FamilyInheritanceError)

try:
    @family_class
    class TestC(TestA):
        FAMILY_INHERIT = ('a')
except FamilyInheritanceError:
    pass
else:
    raise RuntimeError(FamilyInheritanceError)
