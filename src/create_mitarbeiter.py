from openpyxl import Workbook

def erstelle_mitarbeiter_excel():
    # Neue Excel-Datei erstellen
    wb = Workbook()
    sheet = wb.active
    sheet.title = "Mitarbeiter"

    # Überschriften
    sheet['A1'] = 'Name'
    sheet['B1'] = 'Alter'
    sheet['C1'] = 'Position'

    # Beispieldaten
    mitarbeiter_daten = [
        ['Anna Schmidt', 34, 'Entwicklerin'],
        ['Max Müller', 28, 'Designer'],
        ['Lisa Weber', 45, 'Projektmanagerin'],
        ['Tom Fischer', 31, 'Entwickler'],
        ['Marie Jung', 29, 'Designer'],
        ['Peter Krause', 52, 'Produktmanager'],
        ['Sarah Meyer', 37, 'Entwicklerin'],
        ['Klaus Wagner', 41, 'Architekt'],
        ['Julia Berg', 33, 'Designerin'],
        ['Mark Winter', 39, 'Entwickler']
    ]

    # Daten einfügen
    for row, mitarbeiter in enumerate(mitarbeiter_daten, start=2):
        sheet[f'A{row}'] = mitarbeiter[0]  # Name
        sheet[f'B{row}'] = mitarbeiter[1]  # Alter
        sheet[f'C{row}'] = mitarbeiter[2]  # Position

    # Spaltenbreiten anpassen
    sheet.column_dimensions['A'].width = 15
    sheet.column_dimensions['B'].width = 10
    sheet.column_dimensions['C'].width = 20

    # Datei speichern
    wb.save('mitarbeiter.xlsx')
    print("mitarbeiter.xlsx wurde erfolgreich erstellt!")


if __name__ == "__main__":
    erstelle_mitarbeiter_excel()
