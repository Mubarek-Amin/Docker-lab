# Docker‑Lab

A collection of small Docker labs and experiments focused on containerising Python (Flask) apps and wiring them to services like Redis. Use this repo to learn, tinker, and iterate.

<p align="left">
  <a href="https://github.com/Mubarek-Amin/Docker-lab">
    <img alt="last commit" src="https://img.shields.io/github/last-commit/Mubarek-Amin/Docker-lab">
  </a>
  <a href="https://github.com/Mubarek-Amin/Docker-lab">
    <img alt="top language" src="https://img.shields.io/github/languages/top/Mubarek-Amin/Docker-lab">
  </a>
  <img alt="docker" src="https://img.shields.io/badge/docker-ready-blue">
</p>

---

## Contents

- [What you’ll learn](#what-youll-learn)
- [Repo structure](#repo-structure)
- [Prerequisites](#prerequisites)
- [Quick start](#quick-start)
  - [Hello Flask](#hello-flask)
  - [Flask + Redis](#flask--redis)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## What you’ll learn

- How to containerise a simple Flask app with a `Dockerfile`.
- How to run multiple services locally with Docker Compose (e.g., Flask + Redis).
- How to pass environment variables, expose ports, and persist data (basics).

## Repo structure

```
.
├─ Flask-Redis/     # Flask app that talks to Redis (usually via docker compose)
└─ hello_flask/     # Minimal Flask “hello world” in a single container
```

> Tip: each folder is a self‑contained lab with its own files (app code, Dockerfile, and possibly `docker-compose.yml`).

## Prerequisites

- Docker Desktop (or Docker Engine)
- (Optional) Docker Compose v2 (usually included with modern Docker Desktop)
- Python 3.x (optional, only if you want to run apps locally outside of Docker)

## Quick start

First, clone this repository:

```bash
git clone https://github.com/Mubarek-Amin/Docker-lab.git
cd Docker-lab
```

### Hello Flask

Build and run the minimal Flask app:

```bash
# from repo root
docker build -t hello-flask ./hello_flask
docker run --rm -p 5000:5000 hello-flask
```

Open: http://localhost:5000

> If your app uses a different port, update the `-p` mapping accordingly.

### Flask + Redis

Spin up Flask (web) and Redis with Compose:

```bash
cd Flask-Redis
docker compose up --build
```

Then visit: http://localhost:5000

> Common pattern: a `web` service (Flask) depends_on a `redis` service. If your compose file uses a different service name or port (e.g. `8080`), adjust the command and URL as needed.

## Troubleshooting

- **Port already in use**: Stop whatever is bound to the port or change the left side of `-p`, e.g. `-p 8080:5000`.
- **Module not found / requirements not installed**: Rebuild the image after editing `requirements.txt`:
  ```bash
  docker compose build --no-cache
  # or for the single-image lab
  docker build --no-cache -t hello-flask ./hello_flask
  ```
- **Can’t reach Redis from Flask**: In Docker Compose, connect to Redis via its **service name** (e.g. `redis`) rather than `localhost`.
- **Windows line endings**: If entrypoints fail on Windows, ensure shell scripts are LF (`
`) not CRLF.

## Contributing

PRs welcome! Ideas:
- Add new labs (e.g., Flask + Postgres, Celery workers, Nginx as reverse proxy).
- Improve Dockerfiles (multi‑stage builds, slimmer images).
- Expand docs with diagrams or screenshots.

## License

If you add a license file (e.g., `LICENSE` with MIT), mention it here.
