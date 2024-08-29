# Shopify Product Creation and Edit App

Shopify Developer Support interview test app. Built using Python with a combination of REST and GraphQL requests to display both methods.


# Features

The app currently contains 3 functions:

1. `create_product()` which takes user input for the product name and creates a product with some predefined fields. (REST API)
2. `add_metafield()` which adds an unstructured metafield to the newly created product. (REST API)
3. `set_product_category()` which sets the products category to software. (GraphQL API)

# Cloning
To replicate the app also requires a creds.py file with the variables:

api_key = 'XXX'
api_secret = 'XXX'
api_token = 'XXX'
