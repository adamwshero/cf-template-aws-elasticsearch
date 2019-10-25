#!/bin/bash

# I want to make sure that the directory is clean and has nothing left over from
# previous deployments. The servers auto scale so the directory may or may not
# exist.
if [ -d /home/es-config/ ]; then
    rm -rf /home/es-config
fi
mkdir -vp /home/es-config/