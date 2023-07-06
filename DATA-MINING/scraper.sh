#!/bin/bash
python3 ./PY-SCRIPTS/fontanka_scraper.py $1 $2 $3 $4 $5 $6 &
python3 ./PY-SCRIPTS/gazeta_spb_scraper.py $1 $2 $3 $4 $5 $6 &
python3 ./PY-SCRIPTS/lenta_scraper.py $1 $2 $3 $4 $5 $6 &
python3 ./PY-SCRIPTS/rbc_scraper.py $1 $2 $3 $4 $5 $6 &
python3 ./PY-SCRIPTS/spb_mk_scraper.py $1 $2 $3 $4 $5 $6 &
wait
python3 ./PY-SCRIPTS/merger.py $1 $2 $3 $4 $5 $6 ;
