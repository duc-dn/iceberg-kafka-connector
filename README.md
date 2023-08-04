## Test hudi kafka connect
- Tạo image kafa-connect: 
```
docker build -t kafka-connect .
```
- Build docker-compose
```
docker-compose up
```
Access akhq, in schema registry, you need to paste schema that is avaiable in producer/schema folder
After that, you producer/gen_data to generate data compatible with schema that you paste in schema registry
### 3. Chạy Sink connector worker (multiple workers can be run)
#### Minio
```
docker exec kafka-connect curl -X DELETE http://localhost:8083/connectors/hudi-sink
docker exec kafka-connect curl -X POST -H "Content-Type:application/json" -d @/home/ducdn/Desktop/workspace/iceberg-kafka-connector/connector-config/iceberg-config.json http://localhost:8083/connectors
```
- Check metastore (postgres):
```
mysql -u admin -p admin

use metastore_db;

show tables;
```
---
### 4. Test
```
docker exec -it kafka-connect bash
cd /tmp/hoodie/hudi-test-topic
```
### 5. Test Trino
```
docker exec -it trino bash
trino
```
- List catalogs
```
show catalogs;
```
- Use minio
```
use minio.default;
```
- List tables
```
show tables;
```
- Select 
```
select * from huditesttopic;
```
