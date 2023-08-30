from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from sale.models import Seller
from users.models import User


# запуск тестов: python manage.py test
# запуск подсчёта покрытия кода тестами: coverage run --source='.' manage.py test
# вывод отчёта о покрытии тестами: coverage report
class UserTestCase(APITestCase):
    """Тест для контроллера UserCreateView"""
    def setUp(self):
        """Заполняем БД перед началом тестов"""
        self.userdata = {
            'email': 'test@test.ru',
            'password': '12345',
        }

    def test_user_create(self):
        # создаём пользователя
        response = self.client.post(
            reverse('users:create_user'),
            data=self.userdata
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_user_token_create(self):
        user = User.objects.create(
            email=self.userdata.get('email'),
            is_active=True
        )
        user.set_password(self.userdata.get('password'))
        user.save()
        response = self.client.post(
            reverse('users:token_obtain_pair'),
            self.userdata
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_token_refresh(self):
        user = User.objects.create(
            email=self.userdata.get('email'),
            is_active=True
        )
        user.set_password(self.userdata.get('password'))
        user.save()
        tokens = self.client.post(
            reverse('users:token_obtain_pair'),
            self.userdata
        )
        response = self.client.post(
            reverse('users:token_refresh'),
            {'refresh': tokens.json().get('refresh')}
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class SellerTestCase(APITestCase):
    """Тест для контроллера SellerSet"""
    def setUp(self):
        """Заполняем БД перед началом тестов"""
        self.userdata = {
            'email': 'test@test.ru',
            'password': '12345',
        }
        # создаём пользователя
        user = User.objects.create(
            email=self.userdata.get('email'),
            is_active=True
        )
        user.set_password(self.userdata.get('password'))
        user.save()
        # получаем токен
        response = self.client.post(
            reverse('users:token_obtain_pair'),
            self.userdata
        )
        # добавляем токен к авторизации
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.json().get('access'))
        # шаблон для создания нового поставщика
        self.factory_data = {
            'title': 'Big',
            'email': 'big@big.ru',
            'country': 'Russia',
            'city': 'Moscow',
            'street': 'Tverskaya',
            'house': 10,
            'type': 'factory',
        }
        self.reseller_data = {
            'title': 'Mega',
            'email': 'mega@mega.ru',
            'country': 'Russia',
            'city': 'Moscow',
            'street': 'Tverskaya',
            'house': 5,
            'type': 'seller',
        }

    def test_seller_create(self):
        """Тест создания поставщика"""
        response = self.client.post(
            reverse('sale:seller-list'),
            data=self.factory_data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_wrong_factory_with_supplier_create(self):
        """Тест валидатора создания поставщика с присвоением задолженности заводу"""
        data = self.factory_data
        data['debt'] = 50
        response = self.client.post(
            reverse('sale:seller-list'),
            data=data
        )
        self.assertEqual(
            {'non_field_errors': ['Завод не может быть должником по закупкам']},
            response.json()
        )

    def test_wrong_factory_with_debt_create(self):
        """Тест валидатора создания поставщика с присвоением заводу поставщика"""
        self.factory = Seller.objects.create(**self.factory_data)
        data = self.factory_data
        data['title'] = 'Big1'
        data['supplier'] = self.factory.id
        response = self.client.post(
            reverse('sale:seller-list'),
            data=data
        )
        self.assertEqual(
            {'non_field_errors': ['Завод не может закупать товары для реализации']},
            response.json()
        )

    def test_wrong_debt_update(self):
        """Тест валидации изменения debt (запрещено)"""
        self.reseller = Seller.objects.create(**self.reseller_data)
        response = self.client.patch(
            reverse('sale:seller-detail', kwargs={'pk': self.reseller.id}),
            {'debt': 5000}
        )
        self.assertEqual(
            {'debt': ['Задолженность не может быть изменена по API']},
            response.json()
        )

    def test_supplier_delete(self):
        """Тест удаления поставщика"""
        self.factory = Seller.objects.create(**self.factory_data)
        response = self.client.delete(
            reverse('sale:seller-detail', kwargs={'pk': self.factory.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_seller_detail(self):
        """Тест получения одного объекта модели Seller"""
        self.factory = Seller.objects.create(**self.factory_data)
        response = self.client.get(
            reverse('sale:seller-detail', kwargs={'pk': self.factory.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_seller_list(self):
        """Тест получения всех объектов модели Seller"""
        self.factory = Seller.objects.create(**self.factory_data)
        response = self.client.get(
            reverse('sale:seller-list'),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
