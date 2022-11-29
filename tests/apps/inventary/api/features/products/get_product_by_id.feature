Feature: Get a product by product_id
    Scenario: A non-existent product
        Given I send a GET request to "/api/products/ef8ac118-8d7f-49cc-abec-78e0d05af80a"
        Then The response status code should be "404"
        And The response body should be:
            {
                "detail": "Not Found"
            } 
        And Logger DEBUG was called "3" time(s)
        And Logger INFO was called "2" time(s)

    Scenario: A existent product
        Given I send a POST request to "/api/products/" with body:
            {
                "product_id": "ef8ac118-8d7f-49cc-abec-78e0d05af80a",
                "name": "Valid Product", 
                "status": 1,
                "stock": 10,
                "description": "Test description",
                "price": 100.0
            }
        Then The response status code should be "201"
        Given External discount service with response "10" 
        Given I send a GET request to "/api/products/ef8ac118-8d7f-49cc-abec-78e0d05af80a"
        Then The response status code should be "200"
        And The response body should be:
            {
                "product_id": "ef8ac118-8d7f-49cc-abec-78e0d05af80a",
                "name": "Valid Product", 
                "status": "Active",
                "stock": 10,
                "description": "Test description",
                "price": 100.0,
                "discount":10.0,
                "final_price":90.0
            }
        And Logger DEBUG was called "6" time(s)
        And Logger INFO was called "4" time(s)

