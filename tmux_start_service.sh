#!/bin/bash
# -*- coding: utf-8 -*-

tmux new-session -d
tmux rename "fastapi_lowjs_auth"

# ------------------------------------------- #
tmux renamew "fastapi_lowjs_auth"

# Split the window horizontally first:
tmux split-window -h -t "fastapi_lowjs_auth:0"

# Send commands to the respective panes:
tmux send-keys -t "fastapi_lowjs_auth:0.0" "cd src && docker-compose -p fastapi_lowjs_auth up -d && cd ../.. && uv run main_api.py" Enter

# ------------------------------------------- #
tmux attach -t "fastapi_lowjs_auth"
