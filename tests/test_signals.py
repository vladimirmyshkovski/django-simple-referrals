from referrals import signals, models
from test_plus.test import TestCase
from django.test import RequestFactory


class TestCreateFlatReferral(TestCase):

    def setUp(self):
        self.request_factory = RequestFactory()
        self.referrer = self.make_user('referrer')
        self.referred = self.make_user('referred')

        link = models.Link.objects.create(user=self.referrer)

        self.post_request = self.request_factory.post(
            '/fakeurl/', {'referral': link.token})
        self.get_request = self.request_factory.get(
            '/fakeurl/?ref={}'.format(link.token))
        self.post_request.user = self.referred
        self.get_request.user = self.referred

    def test_signal_with_post_requset(self):
        self.signal_was_called = False

        def handler(sender, request, user, **kwargs):
            self.signal_was_called = True

        signals.create_flat_referral.connect(handler)
        signals.create_flat_referral.send(
            sender=self.referrer.__class__,
            request=self.post_request,
            user=self.referred
        )

        referred = models.FlatReferral.objects.get(referred=self.referred)

        self.assertTrue(self.signal_was_called)
        self.assertTrue(referred in self.referrer.referreds.all())

        signals.create_flat_referral.disconnect(handler)

    def test_signal_with_get_requset(self):
        self.signal_was_called = False

        def handler(sender, request, user, **kwargs):
            self.signal_was_called = True

        signals.create_flat_referral.connect(handler)
        signals.create_flat_referral.send(
            sender=self.referrer.__class__,
            request=self.get_request,
            user=self.referred
        )

        referred = models.FlatReferral.objects.get(referred=self.referred)

        self.assertTrue(self.signal_was_called)
        self.assertTrue(referred in self.referrer.referreds.all())

        signals.create_flat_referral.disconnect(handler)

    def test_signal_without_referral_link(self):
        self.signal_was_called = False
        post_request = self.request_factory.post('/fakeurl/')

        def handler(sender, request, user, **kwargs):
            self.signal_was_called = True

        signals.create_flat_referral.connect(handler)
        signals.create_flat_referral.send(
            sender=self.referrer.__class__,
            request=post_request,
            user=self.referred
        )

        self.assertEqual(self.referrer.referreds.count(), 0)
        self.assertTrue(self.signal_was_called)

        signals.create_flat_referral.disconnect(handler)


class TestCreateMultiLevelReferral(TestCase):

    def setUp(self):
        self.request_factory = RequestFactory()
        self.referrer = self.make_user('referrer')
        self.referred = self.make_user('referred')

        link = models.Link.objects.create(user=self.referrer)

        self.post_request = self.request_factory.post(
            '/fakeurl/', {'referral': link.token})
        self.get_request = self.request_factory.get(
            '/fakeurl/?ref={}'.format(link.token))
        self.post_request.user = self.referred
        self.get_request.user = self.referred

        models.MultiLevelReferral.add_root(user=self.referrer)

    def test_signal_with_post_requset(self):
        self.signal_was_called = False

        def handler(sender, request, user, **kwargs):
            self.signal_was_called = True

        signals.create_multi_level_referral.connect(handler)
        signals.create_multi_level_referral.send(
            sender=self.referrer.__class__,
            request=self.post_request,
            user=self.referred,
            position='child'
        )

        referred = models.MultiLevelReferral.objects.get(user=self.referred)
        multi_level_referral = models.MultiLevelReferral.objects.get(
            user=self.referrer)

        self.assertTrue(self.signal_was_called)
        self.assertTrue(referred in multi_level_referral.get_children())

        signals.create_multi_level_referral.disconnect(handler)

    def test_signal_with_get_requset(self):
        self.signal_was_called = False

        def handler(sender, request, user, **kwargs):
            self.signal_was_called = True

        signals.create_multi_level_referral.connect(handler)
        signals.create_multi_level_referral.send(
            sender=self.referrer.__class__,
            request=self.get_request,
            user=self.referred,
            position='child'
        )

        referred = models.MultiLevelReferral.objects.get(user=self.referred)
        multi_level_referral = models.MultiLevelReferral.objects.get(
            user=self.referrer)

        self.assertTrue(self.signal_was_called)
        self.assertTrue(referred in multi_level_referral.get_children())

        signals.create_multi_level_referral.disconnect(handler)

    def test_signal_with_post_requset_and_position_sibling(self):
        self.signal_was_called = False

        def handler(sender, request, user, **kwargs):
            self.signal_was_called = True

        signals.create_multi_level_referral.connect(handler)
        signals.create_multi_level_referral.send(
            sender=self.referrer.__class__,
            request=self.get_request,
            user=self.referred,
            position='sibling'
        )

        referred = models.MultiLevelReferral.objects.get(user=self.referred)
        multi_level_referral = models.MultiLevelReferral.objects.get(
            user=self.referrer)

        self.assertTrue(self.signal_was_called)
        self.assertTrue(referred in multi_level_referral.get_siblings())
        self.assertEqual(
            referred,
            multi_level_referral.get_last_sibling()
        )

        signals.create_multi_level_referral.disconnect(handler)

    def test_signal_without_referral_link(self):
        self.signal_was_called = False
        post_request = self.request_factory.post('/fakeurl/')

        def handler(sender, request, user, **kwargs):
            self.signal_was_called = True

        signals.create_multi_level_referral.connect(handler)
        signals.create_multi_level_referral.send(
            sender=self.referrer.__class__,
            request=post_request,
            user=self.referred,
            position='child'
        )

        self.assertEqual(self.referrer.referreds.count(), 0)
        self.assertTrue(self.signal_was_called)

        signals.create_multi_level_referral.disconnect(handler)
