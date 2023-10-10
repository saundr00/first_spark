#!/bin/bash

cd /var/lib/postgres/var/lib/postgres/apache-hive-3.1.2-bin/bin
./schematool -dbType postgres -driver org.postgresql.Driver \
-url jdbc:postgresql://localhost:5432/metastore_db \
-userName postgres -passWord postgres -initSchema
