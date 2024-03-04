#!/bin/bash

# Navigating to the subwaysign directory
cd /home/viraj/subwaysign

# Activating the virtual environment
source /home/viraj/.bashrc
source /home/viraj/subwaysign/venvss/bin/activate

# Starting the main.py script
python /home/viraj/subwaysign/main.py | tee /home/viraj/log.txt
