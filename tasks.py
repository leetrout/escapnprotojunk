from invoke import task

@task
def populate_es():
    from random import choice

    import elasticsearch
    from elasticsearch.helpers import bulk
    es = elasticsearch.Elasticsearch([{'host':'leetroutwrw2-9200.terminal.com', 'port':'80'}])

    es.indices.create(index='pizzas', ignore=400)
    pizza_ids = []

    # Add 5 pizzas
    for pizza_doc in [
        {
            'crust': 'thin',
            'sauce': 'red',
            'toppings': ['cheese', 'pepperoni'],
        },
        {
            'crust': 'pan',
            'sauce': 'red',
            'toppings': ['cheese', 'pepperoni', 'sausage'],
        },
        {
            'crust': 'pan',
            'sauce': 'white',
            'toppings': ['cheese'],
        },
        {
            'crust': 'hand',
            'sauce': 'white',
            'toppings': ['cheese', 'sausage'],
        },
        {
            'crust': 'thin',
            'sauce': 'red',
            'toppings': ['cheese', 'pepperoni', 'mushroom'],
        },
    ]:
        pizza_res = es.index(index="pizzas", doc_type='pizza', body=pizza_doc)
        pizza_ids.append(pizza_res['_id'])

    # Make some customers
    cust_ids = []
    for cust in [
        {
            'name': 'Bob Smith',
            'phone': '123-456-7890',
            'email': 'nobody@nowhere.com',

        },
        {
            'name': 'Sally Sanders',
            'phone': '123-456-7890',
            'email': 'nobody@nowhere.com',

        },
        {
            'name': 'John Doe',
            'phone': '123-456-7890',
            'email': 'nobody@nowhere.com',

        },
    ]:
        cust_res = es.index(index="pizzas", doc_type='customer', body=cust)
        cust_ids.append(cust_res['_id'])

    # Make some orders
    for pizza_order in [
        {
            'customer': cust_ids[0],
            'pizzas': pizza_ids[:2]
        },
        {
            'customer': cust_ids[1],
            'pizzas': pizza_ids[2]
        },
        {
            'customer': cust_ids[0],
            'pizzas': pizza_ids[3]
        },
        {
            'customer': cust_ids[1],
            'pizzas': pizza_ids[4]
        },
    ]:
        cust_res = es.index(index="pizzas", doc_type='order', body=pizza_order)

    
