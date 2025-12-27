# Jahreskalender / Year Plan

A simple yearly calendar template designed for planning and organizing your year. This template provides a clear overview of all twelve months, allowing you to jot down important dates, events, and goals for each month.


## Usage

Argparse will help you to run the script from the command line. Use the `-h` or `--help` flag to see all available options
```
python3 jahreskalender.py -h
```

Basic usage to generate a yearly calendar for a specific year and language
```
python3 jahreskalender.py --year 2033 --language en
python3 jahreskalender.py -y 2033 -l en
```

If you don't provide a year, the coming year will be used by default
```
python3 jahreskalender.py --language de
python3 jahreskalender.py -l de
```

### Supported Languages
Currently supported languages are:
- English US (`en`)
- German (`de`)

