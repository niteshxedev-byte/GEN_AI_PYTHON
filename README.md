# GEN_AI_PYTHON
# FastAPI & Generative AI Production Roadmap
### From Zero to Production (Expanded Edition)

> A comprehensive, highly detailed step-by-step guide covering everything you need: Python, FastAPI, and production-grade G  enerative AI systems with LangChain, AutoGen, CrewAI, MCP, RAG, prompt engineering, and harness engineering.

---

## Phase 0 — Python Foundations (Everything You Need)

**Goal:** Master Python syntax, tooling, and modern development practices to build a rock‑solid foundation for FastAPI and AI.

### Python Basics

- Variables, data types: int, float, str, bool, None; mutable vs immutable; list, tuple, dict, set, frozenset; indexing, slicing, unpacking; type conversion functions.
- Strings: f-strings, format(), join/split, strip, replace, regular expressions basics (re module).
- Control flow: if/elif/else, ternary operator; for loops, while loops, break/continue, else clause on loops; match/case (structural pattern matching, Python 3.10+).
- Comprehensions: list, dict, set, generator comprehensions; performance and readability trade-offs.
- Functions: defining, arguments (positional, keyword, default), *args and **kwargs, keyword‑only arguments (after *), function annotations, lambda expressions, map/filter/reduce as functional alternatives.
- Error handling: try/except/else/finally, exception hierarchy, raising exceptions, exception chaining (raise from), custom exception classes, assert statements.
- File I/O: open() with modes ('r', 'w', 'a', 'b', '+'), context manager (with) for auto‑close, reading lines, writing, pathlib.Path for modern file path handling.

### Object-Oriented Programming

- Classes and objects: __init__, instance attributes vs class attributes, methods (instance, class, static), @classmethod, @staticmethod.
- Inheritance: single, multiple, MRO (Method Resolution Order), super(), isinstance/issubclass.
- Magic (dunder) methods: __str__ vs __repr__, __eq__, __hash__, __bool__, __len__, __getitem__, __setitem__, __iter__, __call__, context manager protocol (__enter__/__exit__).
- Properties: @property, @setter, @deleter, read‑only attributes.
- Abstract Base Classes (abc module): @abstractmethod, @abstractclassmethod, creating interfaces.
- Dataclasses: @dataclass for automatic __init__, __repr__, __eq__; field options, default_factory, frozen=True for immutability.
- Slots: __slots__ for memory optimization.

### Intermediate / Advanced Python

- Decorators: function decorators, decorators with arguments, class decorators, functools.wraps to preserve metadata, built‑in decorators (@staticmethod, @classmethod, @property).
- Closures: inner functions capturing enclosing state, nonlocal keyword.
- Generators: yield, generator expressions, generator delegation (yield from), lazy evaluation, memory efficiency.
- Iterators: __iter__ and __next__, iter() and next(), itertools module (count, cycle, chain, groupby, etc.), creating custom iterables.
- functools module: partial, lru_cache, cached_property, reduce.
- Type hints (typing module): Optional, Union, List, Dict, Tuple, Callable, Any, TypeVar, Generic, Protocol, Literal, TypedDict; static checking with mypy, pyright; integration with Pydantic.
- Context managers: contextlib.contextmanager, contextlib.ExitStack for dynamic context management.
- Metaclasses (just basics): type as metaclass, __new__ vs __init__, when to use (rarely).

### Tooling & Environment

- Virtual environments: venv, poetry for dependency resolution & locking, pipenv alternative.
- Package management: pip install, requirements.txt vs pyproject.toml; semantic versioning.
- Code formatting: black (opinionated), isort (import sorting), ruff (fast linter + formatter).
- Linting: flake8 with plugins, ruff rules; pre‑commit hooks to automate checks.
- Type checking: mypy in strict mode, gradual typing.
- Testing with pytest: writing test functions, fixtures (with scope), parametrize, mocking with pytest‑mock/unittest.mock, code coverage with pytest‑cov.
- Logging: logging levels, handlers (StreamHandler, FileHandler), formatters, loggers hierarchy, structlog for structured logging.

### Concurrency & Async

- Threading: threading.Thread, locks (Lock, RLock), queues (queue.Queue), GIL limitations, when threading is useful (I/O‑bound).
- Multiprocessing: multiprocessing.Process, Pool, shared memory, Manager, overcoming GIL for CPU‑bound tasks.
- asyncio: event loop, coroutines (async def), await, tasks (asyncio.create_task), gathering, asyncio.gather vs asyncio.as_completed.
- Async iterators and async generators: async for, async with, async context managers.
- Async libraries: aiohttp for HTTP client, aiomysql/asyncpg for databases.
- Concurrency patterns: producer‑consumer, semaphores, timeouts, cancellation with asyncio.CancelledError.
- Debugging async code: asyncio debug mode, caio for tracing.

### Data & Communication

- JSON: json module (loads, dumps, custom encoders/decoders), working with complex types.
- YAML: PyYAML, safe_load vs load, configuration files.
- .env handling: python‑dotenv, os.getenv, pydantic‑settings.
- HTTP basics: HTTP methods (GET, POST, PUT, DELETE, PATCH), status codes (1xx‑5xx), headers, request/response body, REST principles, idempotency.
- Requests library: get, post, sessions, timeout, retries, streaming responses.
- Environment variables: 12‑factor app, secret management.

---

## Phase 1 — FastAPI Core: Build Your First APIs

**Goal:** Create performant, production‑ready REST APIs with automatic interactive documentation, data validation, and modern async support.

### FastAPI Basics

- Install FastAPI and Uvicorn: `pip install fastapi uvicorn`, first app, `uvicorn main:app --reload`.
- Path operations: @app.get, @app.post, etc., path parameters (with type hints), query parameters (default values, Optional, validation), request body using Pydantic models (BaseModel).
- Response models: response_model parameter, response_model_exclude, response_model_include, using multiple models for input/output separation.
- Status codes: status.HTTP_201_CREATED, etc., returning different statuses.
- Headers and cookies: Request parameter, Response parameter, setting cookies, reading headers.
- Nested models: Pydantic models within models, lists, dicts, optional fields.
- Field validation: Pydantic Field (min_length, max_length, gt, lt, regex), custom validators (@validator, @root_validator).
- Path operation configuration: summary, description, tags, response_description, deprecated.

### Advanced Routing & Structure

- APIRouter: creating modular routers, prefix, tags, dependencies, including routers in main app.
- Mounting sub‑applications: `app.mount()` for static files or separate ASGI apps.
- Handling forms and file uploads: Form(...) fields, UploadFile, saving files, validating file size/type.
- Path operation function parameters: Body(...), Header(...), Cookie(...), Path(...) for extra validation and metadata.
- Structuring a larger application: routers per feature, separate models, schemas, services, dependencies.

### Dependency Injection

- Function dependencies: yield for cleanup (DB session, file handles), dependencies that return values.
- Classes as dependencies: using callable classes with __call__, sharing state.
- Global dependencies: `app = FastAPI(dependencies=[Depends(verify_api_key)])`.
- Route‑specific dependencies: using deps list in path decorator.
- Dependencies for common tasks: get_current_user (JWT), get_db session, pagination parameters.
- Sub‑dependencies: a dependency that uses another dependency, caching dependency results per request (use_cache=False).

### Middleware & CORS

- Custom middleware: @app.middleware("http"), request/response manipulation, timing, logging request ID.
- CORS: CORSMiddleware, allow_origins, allow_methods, allow_headers, allow_credentials.
- TrustedHostMiddleware: preventing host header attacks.
- HTTPSRedirectMiddleware: redirect HTTP to HTTPS.
- Other built‑in: GZipMiddleware, SessionMiddleware (needs external backend).

### Background Tasks & WebSockets

- BackgroundTasks: adding tasks that run after response is sent, sending emails, writing logs.
- WebSocket basics: @app.websocket, accepting, sending/receiving text/JSON/binary, using WebSocketDisconnect.
- Broadcasting: managing multiple connections in a set, sending messages to all (simple chat example).
- Limitations: no concurrency inside a WebSocket route (use asyncio queues/background tasks for heavy lifting).

### Testing

- TestClient (from starlette.testclient): synchronous and async tests (pytest‑asyncio).
- Writing tests for endpoints: checking status codes, response JSON, headers.
- Overriding dependencies: app.dependency_overrides to mock DB, auth, external services.
- Testing background tasks and WebSockets.

### Automatic Documentation

- Swagger UI (/docs) and ReDoc (/redoc) customisation: title, description, version, terms_of_service, contact, license_info, openapi_tags.
- Adding examples to Pydantic models (schema_extra, Field(examples=...)), path operations (examples in decorator).
- Extending OpenAPI schema: app.openapi() customisation, adding security schemes.
- Hiding endpoints from docs: include_in_schema=False.

---

## Phase 2 — Databases, Auth & Full‑Stack Backend

**Goal:** Integrate persistent storage, user management, and industry‑standard project architecture.

### SQL Databases with SQLAlchemy (async)

- SQLAlchemy 2.0 setup: async engine with asyncpg, async sessionmaker, Base declarative model.
- Models: defining tables (__tablename__, Column, Integer, String, Boolean, DateTime, ForeignKey, relationship), server_default, unique constraints.
- CRUD operations: async session add/commit/refresh, select/where/filter, update, delete.
- Relationships: one‑to‑many, many‑to‑many (association table), lazy loading (selectin, joined, subquery).
- Alembic: initialisation, generating autogenerate migrations, upgrade/downgrade, handling complex changes.
- Repository pattern: abstracting data access, unit‑of‑work (optional), dependency injection of session.
- Performance: connection pooling, eager loading (selectinload, joinedload) to avoid N+1 queries, indexing.

### NoSQL

- MongoDB with Motor: async client, collection operations, CRUD, aggregation pipeline.
- Redis: using redis‑py async, caching (cache‑aside, read‑through), session storage, fastapi‑cache for decorators.
- Elasticsearch (optional): async client for full‑text search.

### Authentication & Authorization

- JWT: creating access tokens with python‑jose, setting expiration, refresh tokens, token invalidation (blacklist).
- OAuth2 password flow: FastAPI's OAuth2PasswordBearer, OAuth2PasswordRequestForm, hashing passwords with passlib[bcrypt].
- Security utilities: get_current_user dependency extracting user from token, handling token errors.
- Role‑based access control: user roles, permission checking decorator/dependency, scoped access.
- API keys: for machine‑to‑machine communication, header‑based validation.

### Project Structure & Configuration

- Clean architecture: separate directories for api (routers), models (DB models), schemas (Pydantic), services (business logic), core (config, security, dependencies).
- Settings management with pydantic‑settings: BaseSettings, reading from .env, secrets, field validation.
- Async database session: creating session dependency using async generator (yield db), closing session on request end.
- Environment‑specific config: dev, staging, production via env variables.

---

## Phase 3 — Productionising FastAPI

**Goal:** Deploy a secure, scalable, observable, and maintainable service ready for real traffic.

### Performance & Reliability

- Async all the things: ensure DB calls, HTTP requests, file I/O are non‑blocking; use async libraries.
- Connection pooling: SQLAlchemy pool_size, max_overflow, pool_recycle; Redis connection pool.
- Lazy loading avoidance: use joined/selectin loading, avoid N+1.
- Rate limiting: slowapi for IP/user‑based limits, in‑memory or Redis backend.
- Pagination: limit/offset, cursor‑based pagination for large datasets, consistent ordering.
- Compression: GZip middleware for responses.
- Caching strategies: ETag, Cache‑Control headers, server‑side caching with Redis.

### Security

- HTTPS: HSTS headers, secure cookies (secure, httponly, samesite).
- CORS properly configured: not just *; validate sudo systemctl restart bluetooth
referer/origin.
- CSRF protection: for cookie‑based auth, same‑site lax/strict, double submit cookie.
- Input validation: Pydantic strict mode, sanitising against XSS (bleach for HTML output), SQL injection prevention (parameterised queries).
- Secrets: never hardcode; environment variables, vault (HashiCorp Vault), cloud secrets manager.
- Dependency vulnerability scanning: pip‑audit, safety.

### Logging & Monitoring

- Structured logging: JSON‑formatted logs (python‑json‑logger, structlog), correlation IDs across requests.
- Health checks: /healthz (liveness), /readyz (readiness) that check DB, Redis connectivity.
- Metrics: Prometheus client (prometheus‑fastapi‑instrumentator) to expose request duration, error rate, DB pool stats; Grafana dashboards.
- Error tracking: Sentry SDK (sentry‑sdk[fastapi]) for automatic exception capture, release tracking.
- Distributed tracing: OpenTelemetry (opentelemetry‑instrumentation‑fastapi) with Jaeger/Zipkin.
- Alerting: set up alerts on error rate, latency, resource usage.

### Containerization & CI/CD

- Dockerfile: multi‑stage build (builder stage with poetry install, runtime stage with only necessary dependencies), non‑root user, healthcheck.
- docker‑compose: define services (FastAPI, Postgres, Redis, Nginx), volumes, networks, environment.
- CI pipeline: GitHub Actions / GitLab CI to run tests, lint, type‑check, build Docker image, push to registry.
- Continuous Deployment: deploy to staging, run integration tests, promote to production; canary/blue‑green deployments.
- Deployment targets: AWS ECS/Fargate + ALB, GCP Cloud Run, Azure Container Apps, Kubernetes (kind/minikube for local).
- Production server: Uvicorn workers managed by Gunicorn (`gunicorn -k uvicorn.workers.UvicornWorker`), behind Nginx reverse proxy (with SSL termination, buffering).
- Serverless: FastAPI on AWS Lambda via Mangum adapter (cold start considerations).

### Infrastructure as Code (IaC)

- Terraform: define cloud resources (database, cache, compute), state management.
- Pulumi (optional): using Python to define infrastructure.
- Environment configuration management.

---

## Phase 4 — Generative AI Landscape & Prompt Engineering

**Goal:** Understand LLMs, craft effective prompts, and integrate basic GenAI features into FastAPI.

### LLM Fundamentals

- Transformer architecture overview: attention mechanism, tokenisation, embedding, decoding strategies (greedy, beam search, top‑k, top‑p, temperature).
- Model providers: OpenAI (GPT‑4, GPT‑3.5), Anthropic (Claude), Google (Gemini), open‑source (LLaMA 2/3, Mistral, Mixtral) via HuggingFace TGI/vLLM/Ollama.
- APIs: chat completions (system, user, assistant roles), streaming via Server‑Sent Events (SSE), function/tool calling.
- Token economy: understanding token limits, pricing, tokenisers (tiktoken for OpenAI).
- Model selection: balancing capability, latency, cost.

### Prompt Engineering

- Prompt structure: system message (personality, rules), user message, assistant pre‑fill; delimiters for clarity.
- Techniques: zero‑shot, few‑shot (providing examples), Chain‑of‑Thought (step‑by‑step reasoning), ReAct (Reason + Act), self‑consistency (multiple samples then majority vote).
- Prompt templates: using langchain PromptTemplate, dynamic variables, partial templates, saving and versioning prompts (YAML, JSON).
- Evaluating outputs: accuracy, hallucination detection, factual consistency (using NLI models), relevancy, toxicity scoring.
- Iterative prompt development: A/B testing, systematic evaluation, prompt version control.
- Safety: prompt injection prevention, output filtering, using moderation APIs.

### FastAPI Integration

- Streaming LLM responses: async generator that yields tokens, StreamingResponse with `media_type='text/event-stream'` for SSE.
- Asynchronous LLM calls: using httpx or aiohttp for non‑blocking calls to provider APIs.
- Caching LLM responses: Redis cache keyed by prompt hash and temperature; store for a short period to save costs.
- Rate limiting and queuing: protect LLM endpoints from abuse, implement token bucket algorithm.
- Error handling: retries with exponential backoff, fallback models (e.g., if OpenAI fails, try Anthropic).

---

## Phase 5 — RAG & LangChain: Build Intelligent Retrieval Systems

**Goal:** Create retrieval‑augmented generation pipelines and integrate them via FastAPI.

### RAG Core Components

- Document loaders: load from PDFs (PyPDF, Unstructured), web pages (WebBaseLoader), Markdown, Notion, CSV, databases; directory loader.
- Text splitting: RecursiveCharacterTextSplitter (by characters, then recursively), SemanticChunker (using embeddings to detect topic breaks), chunk size and overlap trade‑offs.
- Embeddings: OpenAI embeddings, sentence‑transformers (all‑MiniLM‑L6‑v2), Voyage AI; caching embeddings to avoid recomputation.
- Vector stores: ChromaDB (local/cloud), Pinecone (production), Weaviate, Qdrant, FAISS (in‑memory), pgvector (Postgres extension). Storing metadata alongside vectors for filtering.
- Retrieval: similarity search, maximum marginal relevance (MMR) for diversity, metadata filtering, self‑query retrievers.
- Indexing: incremental indexing, handling document updates/deletions.

### LangChain

- Chains: LLMChain (basic prompt), SequentialChain, RouterChain, ConversationalRetrievalChain (combining memory and retriever).
- Memory: ConversationBufferMemory (full history), ConversationSummaryMemory, ConversationBufferWindowMemory, creating custom memory backends (Redis).
- Agents: AgentExecutor, Zero‑Shot ReAct Agent, OpenAI Functions agent; custom tools (function wrapping with @tool) for web search, calculator, database queries.
- Callbacks: for logging, streaming tokens (AsyncCallbackHandler), cost tracking.
- RAG pipeline with FastAPI: endpoint that accepts query, retrieves documents, constructs prompt, calls LLM, streams answer.
- Advanced RAG: query transformations (multi‑query, step‑back), reranking (Cohere reranker, cross‑encoder), multi‑hop retrieval.

### Streaming & FastAPI

- Streaming chain: using LangChain's astream_events or async callback to capture tokens, pushing to an asyncio Queue, consuming by StreamingResponse.
- Proper backpressure handling: if client disconnects, cancel LLM call.
- Building a simple chat interface with SSE on frontend.

---

## Phase 6 — Multi‑Agent Frameworks: AutoGen & CrewAI

**Goal:** Orchestrate multiple AI agents through FastAPI for complex task automation.

### AutoGen (Microsoft)

- Core concepts: ConversableAgent (LLM‑based), UserProxyAgent (human or code executor), configurable with OAI_CONFIG_LIST.
- Conversations: two‑agent chat, group chat with GroupChat manager, allowing sequential or dynamic selection.
- Tool use: registering Python functions as tools, integrating with external APIs, code execution sandbox (Docker).
- Human‑in‑the‑loop: `human_input_mode` "ALWAYS"/"TERMINATE"/"NEVER".
- FastAPI integration: triggering a conversation via endpoint, streaming messages back using WebSocket (agent messages are forwarded to queue).
- Managing state: saving and resuming conversations.
- Deploying AutoGen with FastAPI: wrapping agent initiation in async task, publishing status.

### CrewAI

- Agent definition: role, goal, backstory, verbose, memory, tools, allow_delegation.
- Task definition: description, expected_output, agent, context (dependencies).
- Processes: sequential (tasks run in order), hierarchical (manager agent delegates).
- Tools: using built‑in tools (SerperDev, WebsiteSearch), custom tools (BaseTool subclass), sharing tools among agents.
- Crew execution: `crew.kickoff()` runs all tasks, returning final output.
- Integration with FastAPI: kickoff in background task (asyncio.to_thread or a job queue), WebSocket updates as tasks complete, returning final result.
- Caching and cost tracking: log token usage per crew run.

### Design Patterns

- Long‑running agent processes: using Celery/Redis Queue to offload work, updating progress in DB/Redis.
- WebSocket updates: agent can emit events to a Redis pub/sub, FastAPI subscriber sends to client.
- Cancellation and timeout: setting time limits, handling asyncio.CancelledError to stop agents.
- Error handling: retrying failed task steps, fallback agents.

---

## Phase 7 — MCP (Model Context Protocol): Tools & Data on Autopilot

**Goal:** Standardise how LLMs connect to tools and data using Anthropic's MCP, and expose servers inside FastAPI.

### Understanding MCP

- Architecture: MCP Host (LLM app), MCP Client (connects to server), MCP Server (exposes tools/resources/prompts).
- Primitives: Resources (context/data like files, DB), Tools (functions LLM can execute), Prompts (pre‑defined templates), Sampling (server requests LLM generation).
- Transport: stdio (local subprocess) and SSE (HTTP long‑lived connection).
- JSON‑RPC 2.0 message format.

### Building an MCP Server with Python

- Using mcp Python SDK: creating server, registering tools with name, description, input schema (Pydantic), handler function.
- Exposing resources: file content, database query results, API data, with URI templates.
- Running server: stdio mode (for local integration with Claude Desktop) or SSE server inside FastAPI (mounting as sub‑app).
- Example tools: get_weather, search_knowledge_base, send_email, query_sql.
- Authentication/authorisation: securing SSE endpoint with API tokens.

### Integrating MCP Clients

- LangChain agent as MCP client: use tool adapter to dynamically load tools from MCP server at runtime.
- AutoGen agent as MCP client: wrapping MCP tools as AutoGen tools.
- FastAPI as MCP client: an endpoint that receives user query, discovers tools from an MCP server, and executes a ReAct loop.
- Dynamic tool discovery: refreshing list of tools when server updates.

---

## Phase 8 — Harness Engineering: AI Reliability & LLMOps

**Goal:** Bring production‑grade testing, evaluation, guardrails, observability, and CI/CD to AI features.

### Prompt & Model Evaluation

- Unit tests for prompts: assert that rendered prompt contains expected text, valid JSON.
- Evaluation frameworks: LangSmith (LangChain tracing and eval), TruLens (feedback functions for relevance, groundedness), DeepEval (metric‑based testing).
- Metrics: Faithfulness, Answer Relevancy, Contextual Precision/Recall, Hallucination, Toxicity, Latency.
- A/B testing: canary deployment of different prompts/models, route a percentage of traffic, compare metrics.
- Regression testing: golden dataset of Q&A pairs to prevent prompt regressions.

### Guardrails

- NeMo Guardrails: define topical, safety, jailbreak rails; integrate with FastAPI via guardrails config.
- Input validation: Pydantic validators for prompt injection (detect 'ignore previous instructions'), length limits.
- Output validation: regex patterns, forbidden words, fact‑checking against retrieved context.
- Moderation APIs: OpenAI moderation endpoint, Perspective API for toxicity.
- Circuit breakers: block LLM call if input fails certain checks.

### Observability

- Tracing: Langfuse (self‑hosted or cloud), MLflow Tracing, Weights & Biases Prompts. Trace every LLM call, retrieval step, tool execution.
- Logging: structured logs with trace ID, user ID, prompt template version, input/output, token count, cost.
- Cost tracking: sum token usage per user/team, alert on budget overruns.
- Dashboard: Grafana panel showing LLM latency, error rate, cost per hour.

### CI/CD for AI

- Version everything: prompts (in git), model versions, RAG config (chunk size, k), agent definitions.
- Automated testing: run evaluation metrics on each pull request; fail if accuracy drops below threshold.
- Deployment strategies: canary release of new prompt, automatic rollback if error rate spikes.
- Infrastructure: separate staging environment with synthetic data, integration tests that call real LLM (with cost limits).

### Harnessing the Full Stack

- Unified FastAPI service blueprint: auth layer → rate limiter → input guardrails → LLM with fallback → output guardrails → caching → logging/metrics.
- Resilience patterns: retries, circuit breakers, bulkheads (separate thread pools for AI), timeouts.
- Graceful degradation: if vector store down, use keyword search; if primary LLM fails, fallback to simpler model; show user friendly message.
- Security: don't expose raw LLM endpoint directly; always go through API that enforces policies.
- Scale: use message queue (RabbitMQ, Redis Streams) for heavy agent tasks, auto‑scaling based on queue length.

---

## Phase 9 — Capstone Projects: Put It All Together

**Goal:** Build real‑world systems that solidify every concept, from basic backend to a fully‑managed AI platform.

### Project 1 — Production RESTful Backend

Users CRUD, items, authentication, roles, Alembic migrations, Docker Compose, deployed to cloud (GCP Cloud Run), CI/CD with GitHub Actions, monitoring.

### Project 2 — Streaming AI Chatbot

FastAPI backend with LangChain conversation chain, memory in Redis, SSE streaming, modern frontend (React/Next.js or simple HTML/JS), token‑by‑token display.

### Project 3 — Document Q&A RAG System

Allow upload of PDF/Word documents, process and index in Pinecone/pgvector, conversational retrieval endpoint, citation of sources, streaming answers.

### Project 4 — Multi‑Agent Research Assistant

CrewAI: researcher, writer, fact‑checker. Trigger via FastAPI, stream agent thoughts and results via WebSocket, final report with references. Use tools for web search and document fetching.

### Project 5 — MCP‑Enabled Tool Platform

Build MCP servers for Jira, Slack, and a knowledge base. Expose SSE endpoint in FastAPI. Build an agent (LangChain or AutoGen) that dynamically uses these tools to handle user tasks like "Create a ticket and notify #general".

### Project 6 — Production‑Hardened GenAI Gateway

Combine everything: auth, rate limiting, LLM fallback (OpenAI/Anthropic), guardrails, vector search, agent orchestration, full observability (Langfuse, Prometheus, Sentry), CI/CD for prompts, automated rollback, cost tracking, admin dashboard.

---
//
## Resources & Continuous Learning

- **Python:** Real Python (realpython.com), official Python docs, *Fluent Python* by Luciano Ramalho.
- **FastAPI:** Official tutorial (fastapi.tiangolo.com), *FastAPI Best Practices* GitHub repo by zhanymkanov, *Building Python Microservices with FastAPI* book.
- **GenAI Tools:** LangChain official docs & cookbook, AutoGen official notebooks, CrewAI documentation, MCP specification on modelcontextprotocol.io.
- **Prompt Engineering:** DeepLearning.AI short course "ChatGPT Prompt Engineering for Developers", *Prompt Engineering Guide* on GitHub by DAIR.AI.
- **LLMOps:** *Full Stack Deep Learning* course, MadeWithML (madewithml.com), LangSmith documentation, *Building LLM Apps* by Hamel Husain.
- **Community:** FastAPI Discord, r/FastAPI, r/MachineLearning, LangChain Discord.

---

> **Note:** This roadmap is intended to be followed sequentially, but you can jump to specific phases based on your current knowledge. Expect to spend **6‑12 months** to go from Python basics to production‑grade GenAI systems. The key is to build projects at every phase — theory alone won't suffice. Always keep a **production mindset**: think about error handling, security, observability, and testing from day one. Happy building!
