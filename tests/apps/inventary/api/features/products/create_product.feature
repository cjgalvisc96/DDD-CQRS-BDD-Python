Feature: Create a new product
    Scenario: A invalid product_id
        Given I send a POST request to "/api/products/" with body:
            {
                "product_id": "-8d7f-49cc-abec-78e0d05af80a",
                "name": "Invalid ID", 
                "status": 1,
                "stock": 10,
                "description": "Test description",
                "price": 100.0
            }
        Then The response status code should be "422"
        And The response body should be:
            {
                "detail": [
                    {
                        "msg":"product_id need to be a valid uuid",
                        "type": "value_error" 
                    }
                ]
            } 
        And Logger DEBUG was called "1" time(s)
        And Logger INFO was called "2" time(s)

    Scenario: A invalid status
        Given I send a POST request to "/api/products/" with body:
            {
                "product_id": "ef8ac118-8d7f-49cc-abec-78e0d05af80a",
                "name": "Invalid Status", 
                "status": 3,
                "stock": 10,
                "description": "Test description",
                "price": 100.0
            }
        Then The response status code should be "422"
        And The response body should be:
            {
                "detail": [
                    {
                        "msg":"status needs to be 1 or 0",
                        "type": "value_error" 
                    }
                ]
            } 
        And Logger DEBUG was called "1" time(s)
        And Logger INFO was called "2" time(s)

    Scenario: A valid non-existent product
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
        And The response body should be empty
        And Logger DEBUG was called "1" time(s)
        And Logger INFO was called "2" time(s)

    Scenario: A valid existent product
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
        Given I send a POST request to "/api/products/" with body:
            {
                "product_id": "ef8ac118-8d7f-49cc-abec-78e0d05af80a",
                "name": "Valid Product", 
                "status": 1,
                "stock": 10,
                "description": "Test description",
                "price": 100.0
            }
        Then The response status code should be "400"
        And The response body should be:
            {
                "error": "Product already exists",
                "type": "domain_error" 
            } 
        And Logger DEBUG was called "2" time(s)
        And Logger INFO was called "4" time(s)

