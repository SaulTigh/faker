# coding=utf-8
from __future__ import unicode_literals
from ..ssn import Provider as SsnProvider


# Note: as there no SSN in Ukraine
# we get Value Added Tax Identification Number (VATIN) here.
# It is also called "Ідентифікаційний Номер Платника Податків" (in ukrainian).
# It is 12 digits long.


class Provider(SsnProvider):
    ssn_formats = ("############",)

    @classmethod
    def ssn(cls):
        return cls.numerify(cls.random_element(cls.ssn_formats))
