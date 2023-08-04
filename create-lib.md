## Enviroment
- Sử dụng confluent-hub để install connector

```
curl -O https://packages.confluent.io/archive/7.3/confluent-7.3.0.tar.gz
```
```
tar xzf confluent-7.3.0.tar.gz
```

```
export CONFLUENT_DIR=/path/to/confluent_install_dir
$CONFLUENT_DIR/bin/confluent-hub install confluentinc/kafka-connect-hdfs:10.1.0
cp -r $CONFLUENT_DIR/share/confluent-hub-components/confluentinc-kafka-connect-hdfs/lib /path/to/foler/plugins/lib
```
---
- Download hudi-kafka-connect-bundle-0.11.0.jar
```
cd /path/to/foler/plugins/lib
wget https://repo1.maven.org/maven2/org/apache/hudi/hudi-kafka-connect-bundle/0.11.0/hudi-kafka-connect-bundle-0.11.0.jar
```
- Nếu save hudi table trên Minio s3 cần download thêm 2 file jars
```
cd /path/to/foler/plugins/lib
wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.271/aws-java-sdk-bundle-1.11.271.jar
wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.10.1/hadoop-aws-2.10.1.jar
```
