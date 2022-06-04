from unittest import TestCase

from flask import request, Flask

from app import db, app
from app.models import User
from app.controllers import user_controller, product_controller
from tests import logger


class TestUserController(TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.user_info = {'sub': '115456682461578988139', 'name': 'Pool Moros Anacona', 'given_name': 'Pool', 'family_name': 'Moros Anacona',
                          'picture': 'https://lh3.googleusercontent.com/a-/AOh14GjVGj2spt5qyANo_yrJEWhCJWuVLyio1uTxT_2RGWI=s96-c', 'email': 'sitovivemoros@gmail.com', 'email_verified': True, 'locale': 'es-419'}

    def tearDown(self):
        self.app_context.pop()

    def test_create_user(self):
        user = user_controller.create_user(self.user_info)
        logger.debug("User is %s with email %s", user, user.email)
        self.assertEqual(user.sub, self.user_info['sub'])

    def test_get_user(self):
        user = user_controller.get_user(self.user_info)
        logger.debug("User is %s with email %s", user, user.email)
        self.assertEqual(user.sub, self.user_info['sub'])


class TestProductController(TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.product = {'id': 1, 'name': 'Product 1',
                        'description': 'Description 1', 'price': 1.0, 'image': 'image1.jpg'}
        self.product_list = [{'id': 1, 'name': 'Product 1', 'description': 'Description 1', 'price': 1.0, 'image': 'image1.jpg'}, {
            'id': 2, 'name': 'Product 2', 'description': 'Description 2', 'price': 2.0, 'image': 'image2.jpg'}]

    def tearDown(self):
        self.app_context.pop()

    def test_get_all_products(self):
        result = product_controller.get_all_products()
        self.assertEqual(len(result), 2)

    def test_get_product(self):
        result = product_controller.get_product(1)
        self.assertEqual(result.id, 1)

    def test_get_products_ordered_by(self):
        result = product_controller.get_products_ordered_by('name')
        self.assertEqual(result[0].name, 'Product 1')
