# food delivery service
Web service for food delivery purposes

    default host: localhost
    default port: 8000

## *API:*

#### Menu

    method: GET
    description: Get full menu (or filtered using query params)
    path: /menu
    params: restaurant_name <str>, restaurant_id <int>


#### Shopping cart

    method: POST
    description: Adding positions to your cart
    path: /cart
    body:   {
                "dish_id": <int>,
                "quantity": <int>
            }

    method: GET
    description: Get your current cart positions
    path: /cart

    method: DELETE
    description: DELETE positions from your cart
    path: /cart
    body:   {
                "dish_id": <int>,
                "quantity": <int>
            }


#### Order
    method: POST
    description: Create order from your current cart
    path: /orders

    method: GET
    description: Get your orders statictics and last 10 orders
    path: /order


*Users:*

    1. admin admin

*Run server:*
    
    docker-compose up --build