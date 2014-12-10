from functools import partial

import elasticsearch

from models import v1, v2

es = elasticsearch.Elasticsearch(['leetroutwrw2-9200.terminal.com:80'])

# ES partials
es_search = partial(es.search, index="pizzas")
es_get_customer = partial(es.get, index="pizzas", doc_type="customer")
es_get_pizza = partial(es.get, index="pizzas", doc_type="pizza")


def get_orders():
    """Return order objects from es after gathering all related objects."""
    ret = []
    orders = es_search(body={"filter": {"type": {"value": "order"}}})
    for order in orders['hits']['hits']:
        data = order['_source']
        # Fetch the customer
        cust = es_get_customer(id=data['customer'])
        # Fetch the pizza(s)
        if hasattr(data['pizzas'], '__iter__'):
            pizza_ids = data['pizzas']
        else:
            pizza_ids = [data['pizzas']]
        pizzas = []
        pizza_objs = []
        for pid in pizza_ids:
            pizza = es_get_pizza(id=pid)
            pizzas.append(pizza)
            pizza_objs.append(v2.Pizza.new_message(**pizza['_source']))

        # Synthesize objects
        customer = v1.Customer.new_message(**cust['_source'])
        order_obj = v2.Order.new_message(customer=customer, pizzas=pizza_objs)

        ret.append(order_obj)

    return ret

