<!--
  Sync Impact Report
  ==================
  Version change: 0.0.0 → 1.0.0
  Modified principles: N/A (initial creation)
  Added sections:
    - Core Principles (6 principles)
    - Additional Constraints
    - Development Workflow
    - Governance
  Removed sections: None
  Templates requiring updates:
    - .specify/templates/plan-template.md ✅ (Constitution Check section compatible)
    - .specify/templates/spec-template.md ✅ (User stories + acceptance criteria compatible)
    - .specify/templates/tasks-template.md ✅ (Phase structure + test-first compatible)
  Follow-up TODOs: None
-->

# Hackathon II — Todo Evolution Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)

All features MUST follow the SDD lifecycle before any code is written:
- Constitution → Specify → Plan → Tasks → Implement
- No manual coding is permitted; all code MUST be generated via Claude Code
  from validated specifications
- Every implementation task MUST reference a Task ID from tasks.md
- Every code file MUST trace back to a spec requirement
- If a spec is incomplete, the agent MUST stop and request clarification
  rather than improvise

### II. Incremental Evolution

Each hackathon phase builds on the previous one; code carries forward:
- Phase I (CLI) → Phase II (Web) → Phase III (AI Chatbot) →
  Phase IV (K8s) → Phase V (Cloud)
- Breaking changes between phases MUST include migration steps
- Shared abstractions (models, services) MUST be designed for reuse
  across phases
- New phases extend existing code rather than rewrite it

### III. Test-First Development

TDD is mandatory for all implementation work:
- Tests MUST be written before implementation code
- Red-Green-Refactor cycle MUST be strictly followed
- Python backend: pytest with >80% coverage target
- Frontend (Phase II+): vitest or jest for component and integration tests
- Each user story MUST have independently runnable acceptance tests
- Tests MUST fail before implementation (Red) and pass after (Green)

### IV. Clean Architecture

Separation of concerns is enforced at every layer:
- Models: Data structures and validation only
- Services: Business logic, no I/O awareness
- Interfaces: CLI commands, API routes, or UI components
- Each layer MUST be independently testable without mocking other layers
- Dependencies flow inward: interfaces → services → models
- No circular dependencies between modules

### V. Cloud-Native Ready

All components MUST be designed for containerized deployment from Day 1:
- Stateless application design; no in-process session state
- Configuration via environment variables (.env files locally,
  K8s secrets in production)
- 12-factor app principles: strict separation of config from code
- Health check endpoints for liveness and readiness (Phase II+)
- Structured logging to stdout/stderr
- Graceful shutdown handling

### VI. Security by Default

Security is a first-class concern, not an afterthought:
- No hardcoded secrets, tokens, or credentials in source code
- All secrets MUST use .env files (local) or secret stores (production)
- .env files MUST be in .gitignore; only .env.example is committed
- JWT authentication for all protected API endpoints (Phase II+)
- Input validation at all system boundaries (user input, API requests)
- SQL injection prevention via parameterized queries (SQLModel/ORM)
- CORS configuration MUST be explicit, not wildcard in production

## Additional Constraints

- **Language**: Python 3.13+ managed by UV package manager
- **Environment**: WSL 2 (Ubuntu) in VS Code
- **Virtual Environments**: Created in WSL via `uv venv` or `uv init`
- **Frontend** (Phase II+): Next.js 16+ with TypeScript and Tailwind CSS
- **Database** (Phase II+): Neon serverless PostgreSQL via SQLModel ORM
- **Authentication** (Phase II+): Better Auth (frontend) + JWT shared
  secret (backend)
- **AI Framework** (Phase III+): OpenAI Agents SDK + Official MCP SDK
- **Containerization** (Phase IV+): Docker with multi-stage builds
- **Orchestration** (Phase IV+): Kubernetes via Minikube (local) or
  cloud provider (production)
- **No manual coding**: All code MUST be generated through the SDD
  pipeline via Claude Code

## Development Workflow

The following workflow MUST be followed for every feature:

1. **Constitution Check** — Verify the feature aligns with all 6 principles
2. **Specify** (`/sp.specify`) — Create feature spec with user stories,
   acceptance criteria, and functional requirements
3. **Clarify** (`/sp.clarify`) — Resolve any ambiguities (optional but
   recommended)
4. **Plan** (`/sp.plan`) — Generate implementation plan with technical
   context, data models, and API contracts
5. **Tasks** (`/sp.tasks`) — Break plan into ordered, testable tasks
   grouped by user story
6. **Analyze** (`/sp.analyze`) — Cross-artifact consistency check
   (optional)
7. **Implement** (`/sp.implement`) — Execute tasks in phase order;
   mark each complete
8. **Commit** (`/sp.git.commit_pr`) — Commit changes with clear
   messages and create PR

PHR (Prompt History Record) MUST be created after every user interaction.
ADR (Architecture Decision Record) MUST be suggested when significant
architectural decisions are detected.

## Governance

This constitution is the highest authority in the project. All agents,
tools, and workflows MUST comply with these principles.

- **Amendments**: Any change to this constitution MUST be documented
  with rationale, approved by the user, and versioned appropriately
- **Versioning**: Semantic versioning (MAJOR.MINOR.PATCH)
  - MAJOR: Principle removal or incompatible redefinition
  - MINOR: New principle or materially expanded guidance
  - PATCH: Clarifications, wording, non-semantic refinements
- **Compliance**: All PRs, code reviews, and spec artifacts MUST verify
  alignment with these principles
- **Conflict Resolution**: Constitution > Specify > Plan > Tasks
  (hierarchy of authority)
- **Runtime Guidance**: See CLAUDE.md for agent-specific behavioral rules

**Version**: 1.0.0 | **Ratified**: 2026-03-13 | **Last Amended**: 2026-03-13
