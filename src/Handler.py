import json

from Models.ModelFactory import ModelFactory


def process(event, context):
    model = ModelFactory.get_model('mysql')
    order = model.get_order_by_id(1)
    print(order)
    exit()
    # Get the order products
    # Get the inventory
    # Get the provider products
    # Eval if the inventory has the product
    # Search which provider has the product

    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "success"
        })
    }
