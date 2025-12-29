#!/bin/sh

# generate year plans for years in all supported languages
for year in $(seq 2026 2040); do
  echo ""
  echo "Generating year plan for $year .."
  for lang in en de fr es it; do
    python3 jahreskalender.py -y "$year" -l "$lang"

    mkdir -p ../year_plans
    mv "year_plan_${year}_${lang}.pdf" ./year_plans/
  done
done