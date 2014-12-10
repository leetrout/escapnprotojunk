@0xd34088e3f9cc7999;

enum Toppings {
    cheese @0;
    pepperoni @1;
    sausage @2;
}

struct  Pizza {
    toppings @0 :List(Toppings);
}

struct Customer {
    name @0 :Text;
    email @1 :Text;
    phone @2 :Text;
}

struct Order {
    when @0 :Text;
    complete @1 :Bool = false;
    delivery @2 :Bool = false;
    pizzas @3 :List(Pizza);
    customer @4 :Customer;
}
