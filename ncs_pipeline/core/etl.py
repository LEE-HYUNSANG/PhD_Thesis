"""ETL functions for each dataset."""
from __future__ import annotations

from pathlib import Path
import yaml

from .client import APIClient

# Load dataset configuration
CONFIG_PATH = Path(__file__).resolve().parents[1] / "config" / "datasets.yaml"
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    DATASETS = yaml.safe_load(f).get("datasets", {})


def load_ncs_info() -> None:
    """Load NCS unit master data into the database."""
    client = APIClient()
    cfg = DATASETS.get("ncs_info", {})
    for _ in client.fetch_all(cfg):
        pass  # TODO: implement upsert logic


def load_job_basic() -> None:
    """Load job basic skills mapping."""
    client = APIClient()
    cfg = DATASETS.get("job_basic", {})
    for _ in client.fetch_all(cfg):
        pass  # TODO


def load_unit_licenses() -> None:
    """Load unit-license mapping."""
    client = APIClient()
    cfg = DATASETS.get("unit_licenses", {})
    for _ in client.fetch_all(cfg):
        pass  # TODO


def load_training() -> None:
    """Load training course information."""
    client = APIClient()
    cfg = DATASETS.get("training", {})
    for _ in client.fetch_all(cfg):
        pass  # TODO


def load_curriculum() -> None:
    """Load academic curriculum data."""
    client = APIClient()
    cfg = DATASETS.get("curriculum", {})
    for _ in client.fetch_all(cfg):
        pass  # TODO


def load_ksa_standard() -> None:
    """Load KSA standard data."""
    client = APIClient()
    cfg = DATASETS.get("ksa_standard", {})
    for _ in client.fetch_all(cfg):
        pass  # TODO


def load_utilization() -> None:
    """Load utilization data."""
    client = APIClient()
    cfg = DATASETS.get("utilization", {})
    for _ in client.fetch_all(cfg):
        pass  # TODO
