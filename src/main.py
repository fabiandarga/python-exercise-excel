def lese_mitarbeiter():
    pass  # Bitte entfernen


def erstelle_gehaltstabelle():
    pass  # Bitte entfernen


def aktualisiere_gehalt(name, neues_gehalt):
    pass  # Bitte entfernen


def main():
    try:
        mitarbeiter = lese_mitarbeiter()
        print(mitarbeiter)
        erstelle_gehaltstabelle()
        print("Gehaltstabelle erstellt!")

        aktualisiere_gehalt("Max", 3000)
    except Exception as e:
        print(f"Fehler: {e}")


if __name__ == "__main__":
    main()
