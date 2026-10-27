"""Die Rechenlogik des Taschenrechners. Kein Webserver, keine Abhängigkeiten."""


def rechne(a, b, op):
    """Wendet die Operation op (add, sub, mul, div) auf a und b an."""
    if op == "add":
        return a + b
    if op == "sub":
        return a - b
    if op == "mul":
        return a * b
    if op == "div":
        if b == 0:
            raise ValueError("Division durch null")
        return a / b
    raise ValueError(f"Unbekannte Operation: {op}")


def formatiere(zahl):
    """Ganze Zahlen ohne Nachkommastelle: 42.0 wird zu 42."""
    if float(zahl).is_integer():
        return int(zahl)
    return round(zahl, 10)
