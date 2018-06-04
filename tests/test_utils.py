from test_plus.test import TestCase

from referrals import utils

from uuid import uuid4


class TestValidateUUID4(TestCase):

    def setUp(self):
        self.valid_uuid = str(uuid4())
        self.invalid_uuid = 'FAKE_STRING'

    def test_with_valid_uuid4(self):
        self.assertTrue(utils.validate_uuid4(self.valid_uuid))

    def test_with_invalid_uuid4(self):
        self.assertFalse(utils.validate_uuid4(self.invalid_uuid))

    def test_without_uuid4(self):
        self.assertFalse(utils.validate_uuid4(''))
