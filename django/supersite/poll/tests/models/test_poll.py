from django.test import TestCase
from poll.models import Poll

class TestPollCase(TestCase):
    def setUp(self):
        Poll.objects.create(name='Mamad', family='Estakhri')
        Poll.objects.create(name='Ehsan', family='AliKhani')

    def test_valid_data(self):
        """Test data inserted"""
        user = Poll.objects.get(name='Mamad')
        self.assertEqual(user.family, 'Estakhri')