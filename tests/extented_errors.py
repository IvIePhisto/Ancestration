from ancestration import family, family_class

family("tests.errors")

try:
    @family_class
    class TestC(object):
        FAMILY_INHERIT = ('a')
except FamilyInheritanceError:
    pass
else:
    raise RuntimeError(FamilyInheritanceError)

try:
    @family_class
    class TestA(object):
        FAMILY_INHERIT = ('a')
except FamilyInheritanceError:
    pass
else:
    raise RuntimeError(FamilyInheritanceError)
