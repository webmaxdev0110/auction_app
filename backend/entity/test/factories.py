import factory

from entity.constants import DONOR_TYPE_COMPANY
from entity.constants import DONOR_TYPE_CELEBRITY
from entity.constants import DONOR_TYPE_OTHER
from entity.models import Charity
from entity.models import Donor
from entity.models import Product
from storage.test.factories import MediumFactory


class CharityFactory(factory.DjangoModelFactory):
    class Meta:
        model = Charity

    title = factory.Sequence(
        lambda n: 'Charity {}'.format(n)
    )
    contact = factory.Sequence(
        lambda n: 'Charity Contact {}'.format(n)
    )
    phone = '123-456-7890'
    address = factory.Sequence(
        lambda n: 'Address {}'.format(n)
    )

    logo = factory.SubFactory(MediumFactory)


DONOR_TYPES = (DONOR_TYPE_COMPANY, DONOR_TYPE_CELEBRITY, DONOR_TYPE_OTHER)


class DonorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Donor

    title = factory.Sequence(
        lambda n: 'Donor {}'.format(n)
    )
    description = factory.Sequence(
        lambda n: 'Description for donor {}'.format(n)
    )
    type = factory.Sequence(
        lambda n: DONOR_TYPES[(n + 2) % len(DONOR_TYPES)]
    )

    @factory.post_generation
    def charities(self, create, extracted, **kwargs):
        if create:
            self.charities.add(CharityFactory.create())
            self.charities.add(CharityFactory.create())


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(
        lambda n: 'Product {}'.format(n)
    )
    description = factory.Sequence(
        lambda n: 'Description for donor {}'.format(n)
    )

    donor = factory.SubFactory(DonorFactory)
