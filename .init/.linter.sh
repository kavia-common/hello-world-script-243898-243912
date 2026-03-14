#!/bin/bash
cd /home/kavia/workspace/code-generation/hello-world-script-243898-243912/hello_world_python_app
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

