#!/usr/bin/env bash

set -e
set -x

pytest --cov=app --cov-report=html --cov-report=term-missing app/tests "${@}"