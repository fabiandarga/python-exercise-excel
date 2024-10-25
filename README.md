# Übung: Excel Files mit Openpyxl

## Setup

### 1. Virtuelle Umgebung erstellen und aktivieren:
```bash
python -m venv venv
# Linux
source venv/bin/activate
# Win PowerShell
.\venv\Scripts\activate.ps1
```

### 2. Openpyxl installieren
```bash
python -m pip install openpyxl
```


## Aufgaben
Lese dir die Beispiele in read_excel.py und write_excel.py durch.
Schreibe den Code zu den Aufgaben in die main.py

### Aufgabe 1: Datei lesen
Erstelle eine Funktion lese_mitarbeiter(), die:

- Die Datei "mitarbeiter.xlsx" öffnet
- Alle Mitarbeiterdaten einliest (Name, Alter, Position)
- Die Daten als Liste von Dictionaries zurückgibt

### Aufgabe 2: Datei schreiben
Erstelle eine Funktion erstelle_gehaltstabelle(), die:

- Eine neue Excel-Datei erstellt
- In die erste Zeile die Überschriften "Name", "Position", "Gehalt" schreibt
- Beispieldaten für 5 Mitarbeiter einfügt
- Die Datei als "gehalt.xlsx" speichert

### Aufgabe 3: Datei aktualisieren
Erstelle eine Funktion aktualisiere_gehalt(name, neues_gehalt), die:

- Die "gehalt.xlsx" öffnet
- Das Gehalt für den angegebenen Mitarbeiter aktualisiert
- Die Änderungen speichert
