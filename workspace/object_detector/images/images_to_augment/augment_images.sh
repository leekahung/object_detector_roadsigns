#!/bin/bash

for d in */; do (cd "$d" && python img_augmentation.py); done
