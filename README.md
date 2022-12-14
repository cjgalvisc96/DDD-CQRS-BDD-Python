# **DDD-CQRS-BDD-Python**
## **Installation**
0. *Requirements =>*
    [Docker](https://docs.docker.com/engine/install/) and
    [DockerCompose](https://docs.docker.com/compose/install/)

1. *Build app(Only one time)*
   ```sh
    >>[DirProject] make build
   ```
2. *Start app*
   ```sh
    >>[DirProject] make start
   ```

   <img src="./images/Docker.png"  width=90%/>

3. *Stop app*
   ```sh
    >>[DirProject] make stop
   ```
## **Usage**
*Check API Documentation =>* http://0.0.0.0:5000/docs

<img src="./images/docs.png"  width=50%/>

## **Unit Tests and Coverage**
```sh
>>[DirProject] make coverage 
```

```sh
>>[DirProject] make all_test 
```

```sh
>>[DirProject] make unit_test 
```

```sh
>>[DirProject] make feature_test 
```

## **Implementation**
### **0. Summary**
This project try to create a different actions (Create, Update and Read) for manage the prodcuts in a inventary, usign Clean Programming Practices like: Clena Architecture, CQRS(master/slave), TDD, BDD, SOLID, Desing Patters(Singlenton, Decorator, Factory, Repository)

### **1. Architecture**
The architecture used to do scalable and maintainable the project was *Hexagonal architecture* and oriented to *Bounded contexts* desing; in this case the Bounded Context *Inventary* with the module *products*.

<img src="./images/hexagonal.png"  width=20%/>

#### **Folder structure *SRC***
<img src="./images/treeSRC.png"  width=25%/>

#### **Folder structure *Tests***
<img src="./images/treeTests.png"  width=25%/>

### **2. Persitence**
Using the library [beanie](https://github.com/roman-right/beanie) with the  asyncronous implementation using the driver [motor](https://motor.readthedocs.io/en/stable/) with CQRS master/slave strategy

*Implementation*
<img src="./images/persistenceImplementation.png" width=100%/>

*File =>* [MongoConnection](./src/contexts/inventary/products/infrastructure/persistence/MongoConnection.py)

*File =>* [MongoProductWriteRepository](./src/contexts/inventary/products/infrastructure/persistence/master/MongoProductWriteRepository.py)

*File =>* [MongoProductReadRepository](./src/contexts/inventary/products/infrastructure/persistence/slave/MongoProductReadRepository.py)
### **3. Cache**
Using the library [fastapi_cache](https://github.com/comeuplater/fastapi_cache) with *MemoryCache*

*Implementation*

<img src="./images/cacheServiceImplementation.png" width=40%/>

*File =>* [MemoryCacheService](./src/contexts/inventary/products/infrastructure/cache/MemoryCacheService.py)


### **4. Web server**
Using the asynchronous framework [fastapi](https://fastapi.tiangolo.com/) with ASGI web server [uvicorn](https://www.uvicorn.org/) 

*Implementation*

<img src="./images/fastapiImplementation.png"  width=30%/>

*File =>* [InventaryFastAPI](./src/apps/inventary/api/InventaryFastAPI.py)

### **5. Logger**
Check the file in *[DirProject]/log/logs.txt*

<img src="./images/logFile.png"  width=50% height=50%/>

*Implementation*

<img src="./images/loggerImplementation.png"  width=30%/>

*File =>* [LoggingLogger](./src/contexts/shared/infrastucture/LoggingLogger.py)


### **6. External Discount Service**
Check the mock api => https://638391421ada9475c80319c0.mockapi.io/api/discounts

*Implementation*

<img src="./images/ExternalDiscountServiceImplementation.png"  width=50% height=50%/>

*File =>* [MockAPIIOExternalDiscountService](./src/contexts/inventary/products/infrastructure/external_services/discounts/MockAPIIOExternalDiscountService.py)

## **Stack**
The technologies used for this project were the following:
* [Python3](https://www.python.org/) 
* [FastAPI](https://fastapi.tiangolo.com/)
* [Mongo](https://www.mongodb.com/)
* [Docker](https://www.docker.com/)
