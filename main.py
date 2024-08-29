import creds, requests


# Setup

base_url = 'https://just-alan-things.myshopify.com/admin/api'
api_version = '/2024-07'

headers = {
  'Content-Type': 'application/json',
  'X-Shopify-Access-Token': creds.api_token
}

request_url = base_url + api_version

# STEP 1: Create Product

def create_product():
    endpoint = request_url + '/products.json'
    global last_created_id
    name = input("Enter product name: ")
    product = {
        "product":{
            "title":name,
            "vendor": "API Challenge",
            "status":"draft",
            "variants":[
                {
                    "option1": "Default Title",
                    "price": "19.99"
                }
            ],
            "options": [
                {
                    "name": "Title",
                    "values": [
                    "Default Title"
                    ]
                }
            ]
        }
    }

    print('Creating product...')
    response = requests.post(endpoint, headers=headers, json=product)
    last_created_id = response.json()['product']['id']
    print('Product created!')
    print('Product ID:', last_created_id)
    return response.json()


# STEP 2: Add Metafield

def add_metafield():
    endpoint = request_url + '/products/' + str(last_created_id) + '/metafields.json'
    metafield = {
        "metafield":{
            "namespace":"custom",
            "key":"api_challenge",
            "type":"single_line_text_field",
            "value":"completed"
        }
    }

    print('Adding metafield...')
    response = requests.post(endpoint, headers=headers, json=metafield)
    print('Metafield added!')
    return response.json()

    
# STEP 3: Set Category

def set_product_category():
#     endpoint = request_url + '/products/' + str(last_created_id) + '.json'
#     product = {
#         "product":{
#             "id":last_created_id,
#             "product_type":"Software"
#         }
#     }

#     print('Setting product category...')
#     response = requests.put(endpoint, headers=headers, json=product)
#     print('Product category set!')
#     return response.json()

    endpoint = request_url + '/graphql.json'
    query = f'mutation {{ productUpdate(input: {{id: "gid://shopify/Product/{last_created_id}", category: "gid://shopify/TaxonomyCategory/so"}}) {{ product {{ id }} }} }}'

    print('Setting product category...')
    response = requests.post(endpoint, headers=headers, json={'query': query})
    print('Product category set!')
    return response.json()

create_product()
add_metafield()
set_product_category()
