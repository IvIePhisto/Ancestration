from ancestration import family

super_family = family.tests.family_a()


ClassA = family_class('ClassA', (object,), {
    'a': lambda self: 'family_b: A',
    'd': lambda self: 'family_b: A',
})

adopt(module='tests.adopt_into_b')