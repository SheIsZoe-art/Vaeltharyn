import json, os
from pathlib import Path

def root_path(explicit=None):
    selected = explicit or os.environ.get('VAELTHARYN_ROOT')
    if selected:
        root = Path(selected).resolve()
        if not (root / 'corpus.json').is_file():
            raise ValueError(f'No corpus.json in selected corpus: {root}')
        return root
    for start in (Path(__file__).resolve().parent, Path.cwd()):
        for parent in (start, *start.parents):
            for candidate in (parent, parent / 'references/corpus'):
                if (candidate / 'corpus.json').is_file():
                    return candidate
    raise ValueError('Corpus not found; supply --root or VAELTHARYN_ROOT.')

def manifest(root):
    data = json.loads((root / 'corpus.json').read_text(encoding='utf-8'))
    if data['schema_version'] != 1:
        raise ValueError('Unsupported corpus schema')
    return data

def legacy_path(root, old):
    aliases = json.loads((root / 'archives/legacy-paths.json').read_text(encoding='utf-8'))
    if old in aliases['files']:
        return root / aliases['files'][old]
    for prefix, replacement in aliases['prefixes'].items():
        if old.startswith(prefix):
            return root / (replacement + old[len(prefix):])
        if old.rstrip('/') == prefix.rstrip('/'):
            return root / replacement.rstrip('/')
    return root / old
