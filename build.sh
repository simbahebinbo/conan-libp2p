#!/bin/bash

conan remove p2p/1.0.0 -c
conan create . --version=1.0.0 --name=p2p --build=missing --update
