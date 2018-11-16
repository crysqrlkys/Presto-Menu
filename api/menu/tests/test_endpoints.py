from rest_framework import test, status

from api.menu.models import Restaurant, MenuItem, Modifier


class PrestoAPITestCase(test.APITestCase):
    def setUp(self):
        super().setUp()
        self.first_venue = Restaurant(title='Burger King')
        self.first_venue.save()
        
        self.second_venue = Restaurant(title='KFC')
        self.second_venue.save()
        
        self.hamburger = MenuItem(
            title='Hamburger',
            cost=5,
            restaurant=self.first_venue
        )
        self.hamburger.save()
        
        self.french_fries = MenuItem(
            title='French fries',
            cost=2,
            restaurant=self.first_venue
        )
        self.french_fries.save()
        
        self.chicken = MenuItem(
            title='Chicken wings',
            cost=3,
            restaurant=self.second_venue
        )
        self.chicken.save()
        
        self.cheese = Modifier(
            title='Cheese',
            menu_item=self.hamburger
        )
        self.cheese.save()
        
        self.more_cheese = Modifier(
            title='Extra Cheese',
            menu_item=self.hamburger,
            parent=self.cheese
        )
        self.more_cheese.save()
        
        self.ketchup = Modifier(title='Ketchup', menu_item=self.chicken)
        self.ketchup.save()

    def get_resp(self, _id=None):
        return self.client.get('/restaurants/' + ('{}/item/'.format(_id) if _id else ''))

    def get_resp_restaurant(self, _id):
        return self.client.get('/restaurants/{}/'.format(_id))

    def test_restaurant_list(self):
        resp = self.get_resp()
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_restaurant_inst_ok(self):
        resp = self.get_resp_restaurant(self.first_venue.id)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_restaurant_inst_fail(self):
        resp = self.get_resp_restaurant(999)
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_restaurant_menu_list_ok(self):
        resp = self.get_resp(self.first_venue.id)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_restaurant_menu_list_fail(self):
        resp = self.get_resp(999)
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)


