# SEO Agent Demo

## Description
A Python-based AI agent that audits websites for SEO issues, recommends improvements, and safely applies changes with guardrails.

## Features
- Crawl websites and extract page data (title, meta description, headings, links)
- Analyze pages for SEO issues (missing/duplicate titles, broken links, H1 issues, thin content, etc.)
- Generate prioritized recommendations (impact, effort, confidence)
- Implement safe changes automatically (titles/meta, internal links, JSON-LD)
- Guardrails to prevent risky actions (redirects, robots.txt, large rewrites, page deletion)
- Logging of all changes

## Requirements
- Python 3.12+
- Virtual environment with required packages:
  ```bash
  pip install -r requirements.txt