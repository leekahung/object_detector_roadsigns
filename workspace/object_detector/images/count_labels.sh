#!/bin/bash

grep 'trafficlight<' *.xml | wc -l
grep 'stop<' *.xml | wc -l
grep 'speedlimit<' *.xml | wc -l
grep 'crosswalk<' *.xml | wc -l
grep 'nostop<' *.xml | wc -l
grep 'yield<' *.xml | wc -l
