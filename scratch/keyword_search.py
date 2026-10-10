import re

with open('docs/Chapter-02.md', 'r', encoding='utf-8') as f:
    c2 = f.read()

with open('docs/Chapter-01.md', 'r', encoding='utf-8') as f:
    c1 = f.read()

text = c1 + "\n" + c2

keywords = [
    'Spring Boot', 'Spring', 'Java', 'NestJS', 'Nest', 'Node.js', 'Node', 'Express',
    'Kotlin', 'Python', 'FastAPI', 'Django', 'TypeScript', 'C#', '.NET',
    'Flyway', 'Liquibase', 'JPA', 'Hibernate', 'Room', 'Retrofit', 'Axios',
    'PostgreSQL', 'SQLite', 'Redis', 'RabbitMQ', 'Amazon MQ', 'AWS', 'Docker',
    'Kubernetes', 'ECS', 'Fargate', 'RDS', 'S3', 'CloudFront', 'SES', 'ElastiCache',
    'Niubiz', 'Stripe', 'DocuSign', 'Signio', 'ML Kit', 'Swagger', 'OpenAPI',
    'GitHub Actions', 'GitLab CI', 'Puppeteer', 'Gotenberg'
]

for kw in keywords:
    matches = len(re.findall(r'\b' + re.escape(kw) + r'\b', text, re.IGNORECASE))
    print(f"{kw}: {matches} matches")
