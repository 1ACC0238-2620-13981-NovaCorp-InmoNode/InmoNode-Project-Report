import re

with open('docs/Chapter-02.md', 'r', encoding='utf-8') as f:
    c2 = f.read()

with open('docs/Chapter-01.md', 'r', encoding='utf-8') as f:
    c1 = f.read()

text = c1 + "\n" + c2

# Search all sentences containing backend, lenguaje, arquitectura, stack, framework, etc.
lines = text.split('\n')
for i, l in enumerate(lines):
    l_lower = l.lower()
    if any(k in l_lower for k in ['lenguaje de programación', 'lenguaje', 'stack', 'framework', 'tecnolog', 'backend', 'jpa', 'java', 'node', 'express', 'nest', 'c#', 'net core', 'asp.net', 'spring']):
        # Filter out "lenguaje ubicuo" if it only has that
        if 'lenguaje ubicuo' in l_lower and not any(k in l_lower for k in ['backend', 'programación', 'stack', 'framework', 'java', 'node', 'nest', 'spring', 'jpa', 'tecnol']):
            continue
        print(f"L{i}: {l[:150]}")
