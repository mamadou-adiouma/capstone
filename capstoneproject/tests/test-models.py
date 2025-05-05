from django.test import TestCase
from capstoneapp.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice Cream2", price=14.00, iventory=100)
        self.assertEqual(item, "Ice Cream2 : 14.00")
