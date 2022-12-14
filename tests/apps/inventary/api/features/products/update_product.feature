Feature: Update a new product
    Scenario: A non-existent product
        Given I send a PUT request to "/api/products/ef8ac118-8d7f-49cc-abec-78e0d05af80a" with body:
            {
                "name": "Update Name", 
                "status": 1,
                "stock": 10,
                "description": "Update description",
                "price": 100.0
            }
        Then The response status code should be "400"
        And The response body should be:
            {
                "error": "Product don't exists",
                "type": "domain_error" 
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
        Given I send a PUT request to "/api/products/ef8ac118-8d7f-49cc-abec-78e0d05af80a" with body:
            {
                "name": "Update Name", 
                "status": 0,
                "stock": 20,
                "description": "Update description",
                "price": 200.0
            }
        Then The response status code should be "200"
        Given External discount service with response "20" 
        Given I send a GET request to "/api/products/ef8ac118-8d7f-49cc-abec-78e0d05af80a"
        Then The response status code should be "200"
        And The response body should be:
            {
                "product_id": "ef8ac118-8d7f-49cc-abec-78e0d05af80a",
                "name": "Update Name", 
                "status": "Inactive",
                "stock": 20,
                "description": "Update description",
                "price": 200.0,
                "discount": 20.0,
                "final_price": 160.0
            }
        And Logger DEBUG was called "9" time(s)
        And Logger INFO was called "6" time(s)