import mysql.connector

from Models.Model import Model


class MySQLModel(Model):
    def __init__(self, host: str, database: str, user: str, password: str):
        self.connector = mysql.connector.connect(host=host, database=database, user=user, password=password)
        self.cursor = self.connector.cursor(dictionary=True)

    def get_order_products(self, order_id: int) -> list:
        sql = f'SELECT id, product_id, quantity FROM order_products WHERE order_id = {order_id}'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_providers(self) -> list:
        sql = f'SELECT id, name FROM providers;'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_inventory_products(self) -> list:
        sql = f'SELECT inv.product_id, pro.name, inv.quantity, inv.date FROM inventory AS inv ' \
              f'JOIN products AS pro ON pro.id = inv.product_id ' \
              f'WHERE inv.quantity > 0'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_provider_products(self, provider_id: int) -> list:
        sql = f'SELECT pp.product_id, pro.name FROM provider_products AS pp ' \
              f'JOIN products AS pro ON pro.id = pp.product_id ' \
              f'WHERE pp.provider_id = {provider_id}'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_orders(self) -> list:
        sql = f'SELECT id, user_id, priority FROM orders ORDER BY priority DESC;'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
