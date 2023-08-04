FROM confluentinc/cp-kafka-connect-base:7.0.1

COPY ./docker-config/kafka-plugins/plugins /data/plugins