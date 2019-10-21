from django.urls import reverse, resolve


class TestUrls:

    def test_user_detail_url(self):
        path = reverse('user-detail', kwargs={'pk': 'eve@space.com'})
        assert resolve(path).view_name == 'user-detail'

    def test_pet_detail_url(self):
        path = reverse('pet-detail', kwargs={'pk': '5'})
        assert resolve(path).view_name == 'pet-detail'

    def test_user_list_url(self):
        path = reverse('user-list')
        assert resolve(path).view_name == 'user-list'

    def test_pet_list_url(self):
        path = reverse('pet-list')
        assert resolve(path).view_name == 'pet-list'
