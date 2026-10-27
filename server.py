"""Kleiner Webserver für den Taschenrechner (nur Standardbibliothek).

  GET /                          Eingabeformular
  GET /rechne?a=6&b=7&op=mul     {"ergebnis": 42}
  GET /health                    {"status": "ok"}
"""
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from rechner import formatiere, rechne

SEITE = """<!doctype html>
<html lang="de"><meta charset="utf-8"><title>Taschenrechner</title>
<body style="font-family:sans-serif;max-width:30em;margin:3em auto">
<h1>Taschenrechner</h1>
<form action="/rechne" method="get">
<input name="a" size="6" value="6"> 
<select name="op"><option value="add">+</option><option value="sub">-</option>
<option value="mul" selected>*</option><option value="div">/</option></select>
<input name="b" size="6" value="7"> <button>Rechnen</button>
</form>
<p>Version: {version}</p>
</body></html>"""


class Handler(BaseHTTPRequestHandler):
    def _sende(self, code, inhalt, typ="application/json"):
        daten = inhalt.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", typ + "; charset=utf-8")
        self.send_header("Content-Length", str(len(daten)))
        self.end_headers()
        self.wfile.write(daten)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/":
            seite = SEITE.replace("{version}", os.environ.get("VERSION", "1"))
            self._sende(200, seite, "text/html")
        elif url.path == "/health":
            self._sende(200, json.dumps({"status": "ok"}))
        elif url.path == "/rechne":
            q = parse_qs(url.query)
            try:
                a = float(q["a"][0])
                b = float(q["b"][0])
                ergebnis = formatiere(rechne(a, b, q["op"][0]))
                self._sende(200, json.dumps({"ergebnis": ergebnis}))
            except (KeyError, ValueError) as fehler:
                self._sende(400, json.dumps({"fehler": str(fehler)}))
        else:
            self._sende(404, json.dumps({"fehler": "nicht gefunden"}))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    print(f"Taschenrechner auf Port {port}", flush=True)
    HTTPServer(("", port), Handler).serve_forever()
