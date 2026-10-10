with open('docs/Chapter-01.md', 'r', encoding='utf-8') as f:
    t1 = f.read()
with open('docs/Chapter-02.md', 'r', encoding='utf-8') as f:
    t2 = f.read()

import re

for name, t in [('Chapter-01', t1), ('Chapter-02', t2)]:
    print(f"=== {name} ===")
    for word in ['java', 'spring', 'node', 'nest', 'express', 'python', 'c#', 'dotnet', 'typescript', 'javascript', 'kotlin', 'room', 'retrofit', 'jpa', 'flyway', 'liquibase', 'docker', 'fargate', 'ecs', 'rds', 'elasti', 'redis', 'ses', 's3', 'cloudfront', 'mq', 'niubiz', 'ml kit']:
        matches = re.findall(rf'.{{0,30}}{word}.{{0,30}}', t, re.IGNORECASE)
        if matches:
            print(f"[{word}] found {len(matches)} times:")
            for m in matches[:3]:
                print(f"   ...{m.strip()}...")
