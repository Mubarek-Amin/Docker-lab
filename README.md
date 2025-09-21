Docker-Lab

A collection of small Docker labs / experiments using Flask, Redis, and related tooling.

Table of Contents

Overview

Structure

Getting Started

Usage

Prerequisites

Contributing

License

Overview

This repository is meant as a learning playground to explore how to containerize applications (especially Python/Flask apps), integrate with caching/databases/services (like Redis), and use Docker (and Docker Compose) to orchestrate them.

Use-cases include:

Running a Flask app inside Docker.

Connecting Flask with Redis.

Experimenting with multiple containers.

Seeing how basic services communicate in a Docker environment.

Structure

Here’s how the repository is organised:

Docker-lab/
├── hello_flask/        # A minimal Flask app example
├── Flask-Redis/        # Flask app + Redis integration example
└── README.md


hello_flask/ — Simple Flask app, “hello world”-style, ideal for first Dockerising steps.

Flask-Redis/ — More advanced: shows how to connect Flask to Redis, often via Docker or Docker Compose.

Prerequisites

Before you begin, make sure you have installed:

Docker

Docker Compose (if using compose setups)

Python 3.x

(Optional) pip / virtualenv if running Flask locally

Getting Started

Here are common steps to run the examples.

Clone the repo

git clone https://github.com/Mubarek-Amin/Docker-lab.git
cd Docker-lab


Choose a lab to run, e.g.:

hello_flask/

Flask-Redis/

Build / run with Docker:

If the lab has a Dockerfile only:

cd hello_flask
docker build -t hello-flask .
docker run -p 5000:5000 hello-flask


If using Docker Compose (for multi-service, e.g. Flask + Redis):

cd Flask-Redis
docker-compose up --build


Access the app in your web browser:

Usually at http://localhost:5000/ (or another port if configured).

Usage and Features

Each lab demonstrates a concept:

Basic Flask server inside container.

Flask + Redis caching or usage.

Multi-container setups (app + data/cache services).

You can modify code, rebuild containers, and see how changes propagate.

Use for learning how networking works in Docker, how environment variables can be passed, how persistent data (if configured) behaves, etc.

Contributing

Suggestions welcome! If you want to:

Add another lab (e.g. Flask + PostgreSQL, or Flask + Celery + Redis)

Improve existing labs (better Dockerfile, more configurations)

Fix issues / documentation

Please open a pull request or an issue.
