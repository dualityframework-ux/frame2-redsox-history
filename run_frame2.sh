#!/bin/bash

echo "⚾ starting frame² red sox intelligence..."

cd ~/Downloads/frame2-redsox-history-v1

source venv/bin/activate

export PYTHONPATH=.

streamlit run app/app.py --server.port 8510

