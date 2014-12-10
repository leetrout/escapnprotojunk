@0xb116bd708919598b;

using V1 = import "../v1/pizza.capnp";

struct Pizza {
    toppings @0 :List(V1.Toppings);
    crust @1 :Text;
}

struct Order {
    when @0 :Text;
    complete @1 :Bool = false;
    delivery @2 :Bool = false;
    pizzas @3 :List(Pizza);
    customer @4 :V1.Customer;
}
