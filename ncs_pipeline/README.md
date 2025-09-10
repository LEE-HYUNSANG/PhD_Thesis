# NCS Data Pipeline

Prototype project scaffolding for building a data pipeline around the HRDK NCS OpenAPI.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U requests pydantic pandas sqlalchemy psycopg2-binary tenacity python-dotenv pyyaml click
```

Create a `.env` based on `.env.example` and export your credentials:

```bash
cp ncs_pipeline/.env.example .env
export $(grep -v '^#' .env | xargs)
```

## Usage

Initialise the database tables:

```bash
python -m ncs_pipeline.core.db
```

Synchronise datasets:

```bash
python -m ncs_pipeline.cli sync all
```

## Notes

This repository contains placeholder implementations. Endpoint URLs in `config/datasets.yaml` require verification from the official HRDK API documentation before production use.
