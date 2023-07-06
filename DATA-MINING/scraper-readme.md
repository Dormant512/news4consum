# Scraper usage

N.B.: this scraper's file manipulations are tuned for the GNU/Linux kernel. Modifications to `.py` scripts are needed in order to work on Windows OS.

Example usage:

```bash
chmod +x ./scraper.sh
./scraper.sh 2020 1 10 2021 6 14
```

for scraping five news websites for news headlines from 10.01.2020 to 14.06.2021. The scraper `bash`script takes in 6 args:

- Year, month, day of starting date
- Year, month, day of end date

The scraper utilizes 5 `python` scripts in `./PY-SCRIPTS` subdirectory in parallel, produces 5 temporary `.csv` files in the `./SCRAPED-DATA` subdirectory, then merges them to one `.csv` file with an appropriate name while deleting the temporary files.
