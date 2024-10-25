from openpyxl import Workbook

# 1. Neue Excel-Datei erstellen
workbook = Workbook()
sheet = workbook.active

# 2. Einzelne Zelle beschreiben
sheet['A1'] = 'Name'
# oder
sheet.cell(row=1, column=1, value='Name')

# 3. Mehrere Zellen in einer Zeile beschreiben
zeile = ['Name', 'Alter', 'Position']
sheet.append(zeile)

# 4. Speichern der Excel-Datei
workbook.save('neue_datei.xlsx')
