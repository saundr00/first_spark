$!/bin/bash

config_dir=$DATA_DIR/config
incoming=$DATA_DIR/incoming
archive=$DATA_DIR/incoming/archive
logs=$DATA_DIR/logs

if [ ! -d $config_dir ]
then
    mkdir $config_dir
fi

if [ ! -d $incoming ]
then
    mkdir $incoming
fi

if [ -d $archive ]
then
    mkdir $archive
fi

if [ ! -d $logs ]
then
    mkdir $logs
fi

