import os
import re

files_to_check = ['README.md', 'docs/Chapter-01.md', 'docs/Chapter-02.md', 'Chapter-02-backup-becker.md']

langs = [
    'c#', 'csharp', 'dotnet', '.net', 'asp.net', 'golang', 'rust', 'ruby', 'php',
    'python', 'javascript', 'typescript', 'node', 'express', 'nest', 'fastapi',
    'spring', 'java', 'kotlin', 'swift', 'dart', 'flutter', 'react', 'angular', 'vue'
]

for fp in files_to_check:
    if not os.path.exists(fp): continue
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"*** {fp} ***")
    for l in langs:
        found = re.findall(rf'(\b[^\n.]{{0,30}}{re.escape(l)}[^\n.]{{0,30}}\b)', content, re.IGNORECASE)
        # filter out inmonode
        found_filtered = [x for x in found if not re.match(r'^.*inmonode.*$', x, re.IGNORECASE) or l.lower() != 'node']
        if found_filtered:
            print(f"  [{l}]: {len(found_filtered)} occurrences")
            for sample in found_filtered[:3]:
                print(f"     -> {sample.strip()}")
