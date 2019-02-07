#!/bin/bash
#
# Tested on git-bash (for windows)
#
openssl req \
 -x509 \
 -nodes \
 -newkey rsa:4096 \
 -keyout key.pem \
 -out cacert.crt \
 -days 3650 \
 -sha256 \
 -subj '//CN=localhost'