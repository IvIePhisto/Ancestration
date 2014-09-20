class ClassC(object):
    FAMILY_INHERIT = {'a'}

    def c(self):
        return 'family_b: C'

    @classmethod
    def super_family(cls):
        return cls.module.super_family

