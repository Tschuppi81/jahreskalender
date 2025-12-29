import argparse
import calendar
import locale

from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas


supported_languages = ['en', 'de', 'fr', 'it', 'es']


def safe_set_locale(language: str):
    variants = []

    if language == 'en':
        variants = ['en_US.UTF-8', 'en_US.utf8', 'en_US', 'C']
    elif language == 'de':
        variants = ['de_DE.UTF-8', 'de_DE.utf8', 'de_DE', 'deu_DEU', 'C']
    elif language == 'fr':
        variants = ['fr_FR.UTF-8', 'fr_FR.utf8', 'fr_FR', 'fr_FR@euro', 'fr_FR.ISO8859-1', 'fr']
    elif language == 'it':
        variants = ['it_IT.UTF-8', 'it_IT.utf8', 'it_IT', 'ita_ITA', 'it']
    elif language == 'es':
        variants = ['es_ES.UTF-8', 'es_ES.utf8', 'es_ES', 'es_ES@euro', 'es_ES.ISO8859-1', 'es']
    else:
        # Unknown language: try system default only
        variants = []

    for variant in variants:
        try:
            locale.setlocale(locale.LC_TIME, variant)
            return variant
        except locale.Error:
            continue

    return None


def create_year_plan(year=None, language='en', filename=None):
    # Default: next year
    if year is None:
        year = datetime.now().year + 1

    if language not in supported_languages:
        language = 'en'

    used_locale = safe_set_locale(language)
    if not used_locale:
        print(f'Warning: Could not set locale for language "{language}". Using default locale.')

    if filename is None:
        filename = f"year_plan_{year}_{language}.pdf"

    # PDF setup
    c = canvas.Canvas(filename, pagesize=landscape(A4))
    width, height = landscape(A4)

    margin = 40
    cell_width = (width - 2 * margin) / 12   # 12 months
    cell_height = (height - 2 * margin) / 33 # 31 days + header rows

    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2, height - margin, f"{year}")

    # Month names
    months = [calendar.month_name[m] for m in range(1, 13)]

    c.setFont("Helvetica-Bold", 10)
    for i, month in enumerate(months):
        x = margin + i * cell_width
        c.drawCentredString(x + cell_width / 2, height - (1.5 * margin), month)

    # Calendar logic
    cal = calendar.Calendar(firstweekday=0)  # Monday = 0

    y_start = height - margin - (2 * cell_height)

    for month in range(1, 13):
        month_days = cal.itermonthdates(year, month)

        for day in month_days:
            if day.month != month:
                continue

            week = day.isocalendar()[1]
            weekday = day.weekday()  # 0=Mon ... 6=Sun
            day_of_month = day.day

            row = day_of_month

            x = margin + (month - 1) * cell_width
            y = y_start - row * cell_height

            # Weekend background
            if weekday >= 5:
                c.setFillColor(colors.lightgrey)
                c.rect(x, y, cell_width, cell_height, fill=1, stroke=0)
                c.setFillColor(colors.black)

            # Border around each day
            c.rect(x, y, cell_width, cell_height, fill=0, stroke=1)

            # Weekend bold text
            if weekday >= 5:
                c.setFont("Helvetica-Bold", 8)
            else:
                c.setFont("Helvetica", 8)

            day_label = f"{day.strftime('%a').capitalize().rstrip('.')} {day_of_month}"
            c.drawString(x + 4, y + 4, day_label)
            if weekday == 0:
                c.setFont("Helvetica-Bold", 9)
                c.drawRightString(x + 60, y + 4, f'{week}')

    c.save()
    print(f"PDF created: {filename}")



def parse_args():
    parser = argparse.ArgumentParser(description="Create a year plan PDF")
    parser.add_argument(
        "-y", "--year",
        type=int,
        default=None,
        help="Year to generate (default: next year)"
    )
    parser.add_argument(
        "-l", "--language",
        choices=set(supported_languages),
        default="en",
        help="Language for month names (choices: en, de)"
    )
    parser.add_argument(
        "-o", "--output",
        metavar="FILE",
        default=None,
        help="Output PDF filename (default: year_plan_{year}_{lang}.pdf)"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    create_year_plan(year=args.year, language=args.language, filename=args.output)
