from ancestration import (family, family_class, family_function, class_module,
    adopt)


family()


@family_function
def a():
    return ClassA


ClassA = family_class('ClassA', (object,), {
    'a': lambda self: 'family_a: A',
    'b': lambda self: 'family_a: A',
    'c': lambda self: 'family_a: A',
})


@family_class
class ClassB(ClassA):
    module = class_module

    def b(self):
        return 'family_a: B'

    def class_a(self):
        return self.module.ClassA

    def override(self):
        return 'family_a: B'


def b():
    return ClassB


class ClassC(ClassB):
    def c(self):
        return 'family_a: C'

    @classmethod
    def class_b(cls):
        return cls.module.ClassB

    def class_c(self):
        return class_module(self).ClassC

    def override(self):
        return 'family_a: C'

adopt(b, 'ClassC')