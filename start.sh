#!/bin/bash
gunicorn -w 3 --pid process.pid --bind 0.0.0.0:7319 --daemon run:app --access-logfile logs/access.log --error-logfile logs/error.log
echo "Service Started!"
