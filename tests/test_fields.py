from test_plus.test import TestCase
from referrals import fields


class TestReferralField(TestCase):

    def setUp(self):
        pass

    def test_field_label(self):
        field = fields.ReferralField()
        self.assertEqual(
            field.label,
            ''
        )
