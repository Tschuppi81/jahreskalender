# Jahreskalender / Year Plan

You can either generate your calendar with the provided commands below or print the included PDF file
in `year_plans` folder. The year plan also shows the calendar week number.

Example for 2033:
<img width="974" height="690" alt="image" src="https://github.com/user-attachments/assets/9cd10f1d-e579-490c-8b3b-600227a82ecf" />

## Installation

Install Python 3.12 or higher. Then create a virtual environment and install the required packages
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Argparse will help you to run the script from the command line. Use the `-h` or `--help` flag to see all 
available options
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
- French (`fr`)
- Italian (`it`)
- Spanish (`es`)

You might need to install your language/locale before running the script to ensure proper month and day names.
```
sudo locale-gen en_US.UTF-8  # English (US)
sudo locale-gen de_DE.UTF-8  # German
sudo locale-gen fr_FR.UTF-8  # French
sudo locale-gen it_IT.UTF-8  # Italian
sudo locale-gen es_ES.UTF-8  # Spanish
```

