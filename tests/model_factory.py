from factory.django import DjangoModelFactory


class QuarkFactory(DjangoModelFactory):
    class Meta:
        model = 'whatisthismess.Quark'

    name = 'test_name'
    mystery = 'test_mystery'
