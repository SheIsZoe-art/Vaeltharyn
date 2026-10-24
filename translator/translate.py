"""Traduction assistée: segments sûrs et glosses, sans prétendre à une traduction libre."""
import re
from .engine import norm, PRONOUNS

SUBJECTS = {"je":0,"j":0,"tu":1,"il":2,"elle":2,"nous":3,"vous":4,"ils":5,"elles":5}
PRON = ("mi","ti","se","min","tin","sen")
def translate_assisted(lex, text, direction="fr-va"):
    if direction not in ("fr-va","va-fr"): raise ValueError("Direction inconnue")
    tokens = re.findall(r"[^\W_]+(?:['’][^\W_]+)?|[^\w]+",text,re.UNICODE)
    out=[]; unresolved=[]
    if direction=="fr-va":
        for token in tokens:
            if not token.strip(): out.append(token);continue
            key=norm(token).replace("’","'")
            rows=lex.lookup(key,direction)
            if rows:
                choices=list(dict.fromkeys(row[lex.va_col] for row in rows))
                out.append(choices[0])
                if len(choices)>1: unresolved.append({"token":token,"reason":"polysémie","candidates":choices[:8]})
            elif key in SUBJECTS: out.append(PRON[SUBJECTS[key]])
            else:
                out.append("⟦"+token+"⟧")
                unresolved.append({"token":token,"reason":"non résolu"})
    else:
        for token in tokens:
            if not token.strip(): out.append(token);continue
            rows=lex.lookup(token,"va-fr")
            if not rows:
                analyses=lex.analyze(token)
                rows=[x["entry"] for x in analyses]
            if rows:
                choices=list(dict.fromkeys(row[lex.fr_col] for row in rows))
                out.append(choices[0])
                if len(choices)>1: unresolved.append({"token":token,"reason":"ambiguïté","candidates":choices[:8]})
            else:
                out.append("⟦"+token+"⟧")
                unresolved.append({"token":token,"reason":"non résolu"})
    return {"output":"".join(out),"unresolved":unresolved,"mode":"glossaire assisté, non traduction syntaxique","direction":direction}
