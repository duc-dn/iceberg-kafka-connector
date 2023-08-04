#!/bin/bash
schemaFile=${PWD}/schema/user.avsc
kafkaTopicName=user_topic
# Setup the schema registry
export SCHEMA=$(sed 's|/\*|\n&|g;s|*/|&\n|g' ${schemaFile} | sed '/\/\*/,/*\//d' | jq tostring)
docker exec schema-registry curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" --data "{\"schema\": $SCHEMA}" http://localhost:8081/subjects/${kafkaTopicName}/versions
docker exec schema-registry curl -X GET http://localhost:8081/subjects/${kafkaTopicName}/versions/latest

