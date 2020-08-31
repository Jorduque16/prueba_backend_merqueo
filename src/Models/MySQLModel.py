import mysql.connector

from Models.Model import Model


class MySQLModel(Model):
    def __init__(self, host: str, database: str, user: str, password: str):
        self.connector = mysql.connector.connect(host=host, database=database, user=user, password=password)
        self.cursor = self.connector.cursor(dictionary=True)

    def get_order_by_id(self, order_id: int):
        sql = f'SELECT `id`, `user_id`, `priority`, `address`, `delivery_date` FROM `order_products` ' \
              f'WHERE `id` = {order_id}'
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_order_products(self, order_id: int):
        sql = f'SELECT `id`, `product_id`, `order_id`, `quantity` FROM `order_products` WHERE `order_id` = {order_id}'
        self.cursor.execute(sql)
        return self.cursor.fetchone()
