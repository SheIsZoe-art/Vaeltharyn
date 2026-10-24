"""API HTTP standard-library; lancer: python -m translator.api"""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from .engine import open_default, noun, verb, imperative

lex = open_default()
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        q = parse_qs(parsed.query)
        def arg(name, default=""): return q.get(name, [default])[0]
        try:
            if parsed.path == "/api/lookup":
                result = lex.lookup(arg("q"), arg("direction", "fr-va"))[:100]
            elif parsed.path == "/api/analyze":
                result = lex.analyze(arg("q"))[:100]
            elif parsed.path == "/api/gloss":
                result = lex.gloss(arg("q"), arg("direction", "fr-va"))[:300]
            elif parsed.path == "/api/conjugate":
                result = {t: {m: [verb(arg("verb"), p, t, m) for p in range(6)] for m in ("indicatif","subjonctif","conditionnel")} for t in ("present","passe","futur")}
            elif parsed.path == "/api/decline":
                result = {n: {c: noun(arg("noun"), n=="pluriel", c) for c in ("direct","genitif","datif","locatif","instrumental")} for n in ("singulier","pluriel")}
            elif parsed.path == "/api/health":
                result = {"ok": True, "entries": len(lex.entries)}
            else:
                self.send_error(404); return
            body = json.dumps(result, ensure_ascii=False).encode()
            self.send_response(200); self.send_header("Content-Type", "application/json; charset=utf-8")
        except (ValueError, KeyError) as exc:
            body = json.dumps({"error": str(exc)}).encode()
            self.send_response(400); self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "http://localhost:8000")
        self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)
if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
