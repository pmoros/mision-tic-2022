from unittest import TestCase

from flask import request, Flask

from app import db, app
from app.models import Product, User
from app.controllers import user_controller, product_controller
from app.routes import products_edit
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
        self.product = {'name': 'Product 10', 'description': 'Description', 'image': 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                        'price': 1.0, 'stock': 0, 'available': True, 'store_id': 1, 'productLine_id': 1}

    def tearDown(self):
        self.app_context.pop()

    def test_create_product(self):
        result = product_controller.create_product(self.product)
        stored_product = Product.query.get(result)
        logger.info("Created product %s", stored_product.name)
        self.assertEqual(self.product.get("name"), stored_product.name)

    def test_get_all_products(self):
        result = product_controller.get_all_products()
        logger.info("Number of product stored are %d", len(result))
        self.assertIsNotNone(result)

    def test_get_product(self):
        result = product_controller.get_product(1)
        self.assertEqual(result.id, 1)

    def test_edit_product(self):
        product_edited = self.product.copy()
        product_edited["name"] = "Product 10 edited"
        product_controller.edit_product(10, product_edited)
        result = Product.query.get(10)
        self.assertNotEqual(result.name, self.product.get("name"))

    def test_delete_product(self):
        product_controller.delete_product(1)
        result = Product.query.get(1)
        self.assertIsNone(result)
