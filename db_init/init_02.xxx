#!/bin/bash

export HADOOP_HOME=/var/lib/postgres/hadoop-3.3.6
export HIVE_HOME=/var/lib/postgres/apache-hive-3.1.2-bin
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64

cd /var/lib/postgres/apache-hive-3.1.2-bin/bin
./schematool -dbType postgres -driver org.postgresql.Driver \
-url jdbc:postgresql://localhost:5432/metastore_db \
-userName postgres -passWord postgres -initSchema
