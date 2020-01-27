## Brief Introduction

* The project contains APIs for foundations of a Warehouse Management System (WMS)
* It provides the following:
    * Modelling
    * Public API
    * Validation

## Models
* SKU
    * ID: Unique id (Integer Field)
    * Product_name: product name of SKU (Character Field)
* Storage
    * ID: Unique id (Integer Field)
    * Stock: Stock in storage (Character Field)
    * SKU: ID field of SKU model (Foreign Key for SKU.ID)
* Order
    * Customer_name: Customer name (Character Field)
    * ID: Unique id (Integer Field)
* Order Line
    * ID: Unique id (Integer Field)
    * SKU: ID field of SKU model (Foreign Key for SKU.ID)
    * Quantity: quantity of order (Integer Field)
    
## Endpoints
* POST
    * **/api/sku** - Create record in Sku model
    
        ``` Request Sample => { "skuid": 1, "product_name": "Product 1"}```
    
    * **/api/order** - Create record in Order model
    
        ``` Request Sample => {"orderid": 1, "customer_name": "Customer 1"}```
        
    * **/api/storage** - Create record in Storage model
    
        ``` Request Sample => {"storageid": 1, "stock": "Stock 1", "skuid": 1}```
      
    * **/api/orderline** - Create record in OrderLine model
        
        ``` Request Sample => {"orderlineid": 1, "skuid": 1, "quantity": 1}```
        
* GET
    * **/api/sku** - Fetch all records from Sku model
    * **/api/order** - Fetch all records from Order model
    * **/api/storage** - Fetch all records from Storage model
    * **/api/orderline** - Fetch all records from OrderLine model
    * **/api/placeorder** - Get data from storage based on picks
    
        ``` Request Sample => { lines: [ { sku: 'abc', quantity: 12 }, { sku: 'def', quantity: 2}] } ```
        ``` Response Sample => [ { id: 3, quantity: 5 }, { id: 4, quantity: 7}, { id: 5, quantity: 2} ]```
    
* PUT
    * **/api/sku** - Update record as per request in Sku model
    
        ``` Request Sample => { "skuid": 1, "product_name": "Product 11"}```
    
    * **/api/order** - Update record as per request in Order model
    
        ``` Request Sample => {"orderid": 1, "customer_name": "Customer 11"}```
        
    * **/api/storage** - Update record as per request in Storage model
    
        ``` Request Sample => {"storageid": 1, "stock": "Stock 11", "skuid": 1}```
      
    * **/api/orderline** - Update record as per request in OrderLine model
        
        ``` Request Sample => {"orderlineid": 1, "skuid": 1, "quantity": 12}```

* DELETE
    * **/api/sku/<id>** - Delete record from Sku model having id field as <id>
    * **/api/order/<id>** - Delete record from Order model having id field as <id>
    * **/api/storage/<id>** - Delete record from Storage model having id field as <id>
    * **/api/orderline/<id>** - Delete record from OrderLine model having id field as <id>
 

## URI
* **/** - Home page of application returns "Welcome to Flask home page"
* **/getcustomer?q=<customer_name>** - Customer details for matching name from order model 