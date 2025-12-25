import calendar
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime
import sys

def create_year_plan(year=None, filename=None):
    # Default: next year
    if year is None:
        year = datetime.now().year + 1

    if filename is None:
        filename = f"year_plan_{year}.pdf"

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

    # German weekday abbreviations
    weekday_abbr = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

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

            # Day label: "Mo 1", "Di 2", ...
            day_label = f"{weekday_abbr[weekday]}"
            c.drawString(x + 2, y + 2, day_label)
            if weekday == 0:
                c.setFont("Helvetica-Bold", 9)
                c.drawString(x + 48, y + 2, f'{week}')

    c.save()
    print(f"PDF created: {filename}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            year = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid year, e.g. 2026")
            sys.exit(1)
        create_year_plan(year)
    else:
        create_year_plan()
