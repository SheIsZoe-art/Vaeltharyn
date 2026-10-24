"""API locale du traducteur Vaeltharyn."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from pathlib import Path
from .engine import open_default, noun, verb
from .translate import translate_assisted

lex = open_default()
PAGE = (Path(__file__).parent / "web" / "index.html").read_bytes()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        q = parse_qs(parsed.query)
        def arg(name, default=""): return q.get(name, [default])[0]
        try:
            if parsed.path == "/":
                body=PAGE; mime="text/html; charset=utf-8"
            else:
                if parsed.path == "/api/lookup": result=lex.lookup(arg("q"),arg("direction","fr-va"))[:100]
                elif parsed.path == "/api/analyze": result=lex.analyze(arg("q"))[:100]
                elif parsed.path == "/api/gloss": result=lex.gloss(arg("q"),arg("direction","fr-va"))[:300]
                elif parsed.path == "/api/translate": result=translate_assisted(lex,arg("q"),arg("direction","fr-va"))
                elif parsed.path == "/api/conjugate":
                    result={t:{m:[verb(arg("verb"),p,t,m) for p in range(6)] for m in ("indicatif","subjonctif","conditionnel")} for t in ("present","passe","futur")}
                elif parsed.path == "/api/decline":
                    result={n:{c:noun(arg("noun"),n=="pluriel",c) for c in ("direct","genitif","datif","locatif","instrumental")} for n in ("singulier","pluriel")}
                elif parsed.path == "/api/health": result={"ok":True,"entries":len(lex.entries)}
                else: self.send_error(404);return
                body=json.dumps(result,ensure_ascii=False).encode();mime="application/json; charset=utf-8"
            status=200
        except (ValueError,KeyError) as exc:
            body=json.dumps({"error":str(exc)}).encode();mime="application/json";status=400
        self.send_response(status)
        self.send_header("Content-Type",mime)
        self.send_header("Content-Length",str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__=="__main__":
    print("Vaeltharyn: http://127.0.0.1:8000")
    ThreadingHTTPServer(("127.0.0.1",8000),Handler).serve_forever()
