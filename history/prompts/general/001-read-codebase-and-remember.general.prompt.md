---
id: 001
title: Read Codebase and Remember
stage: general
date: 2026-03-12
surface: agent
model: claude-sonnet-4-6
feature: none
branch: master
user: zunorain
command: none
labels: ["codebase-exploration","onboarding","memory"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - history/prompts/general/001-read-codebase-and-remember.general.prompt.md
tests:
  - none
---

## Prompt

read the code base just nd remember

## Response snapshot

Explored full project structure: CLAUDE.md, .specify/ templates, .claude/commands/, and extracted all content from the hackathon PDF (47 pages). Saved comprehensive memory to MEMORY.md covering all 5 phases, tech stacks, SDD workflow, PHR requirements, and submission details.

## Outcome

- ✅ Impact: Full project context loaded and persisted to memory for future sessions
- 🧪 Tests: none
- 📁 Files: MEMORY.md created at /home/zunorain/.claude/projects/-mnt-c-Users-MY-PC-Desktop-II/memory/MEMORY.md; history/prompts/general/ directory created
- 🔁 Next prompts: /sp.constitution to define project principles; then /sp.specify for Phase I
- 🧠 Reflection: Project is a clean slate — only CLAUDE.md and the PDF exist. All 5 phases need to be built from scratch using SDD workflow.

## Evaluation notes (flywheel)

- Failure modes observed: pdfplumber not installed initially; needed --break-system-packages flag
- Graders run and results (PASS/FAIL): none
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): Start with /sp.constitution to establish project principles
