"""Command line interface for the NCS pipeline."""
from __future__ import annotations

import click
from pathlib import Path
import pandas as pd

from .core import etl, scoring

DATASET_FUNCS = {
    "ncs_info": etl.load_ncs_info,
    "job_basic": etl.load_job_basic,
    "unit_licenses": etl.load_unit_licenses,
    "training": etl.load_training,
    "curriculum": etl.load_curriculum,
    "ksa_standard": etl.load_ksa_standard,
    "utilization": etl.load_utilization,
}


@click.group()
def cli() -> None:
    """NCS data pipeline commands."""


@cli.group()
def sync() -> None:
    """Synchronize datasets from the HRDK OpenAPI."""


@sync.command("all")
def sync_all() -> None:
    for name, func in DATASET_FUNCS.items():
        click.echo(f"Syncing {name}...")
        func()


@sync.command()
@click.argument("dataset")
def dataset(dataset: str) -> None:
    func = DATASET_FUNCS.get(dataset)
    if not func:
        raise click.BadParameter(f"Unknown dataset {dataset}")
    click.echo(f"Syncing {dataset}...")
    func()


@cli.command()
@click.option("--student-csv", type=click.Path(exists=True), required=True)
@click.option("--topk", type=int, default=10)
def score(student_csv: str, topk: int) -> None:
    """Compute top-k job recommendations for students."""
    df = pd.read_csv(student_csv)
    click.echo(f"Loaded {len(df)} students. Top-k={topk}")
    # TODO: implement scoring pipeline


@cli.command("export-report")
@click.option("--respondent-id", required=True)
def export_report(respondent_id: str) -> None:
    """Export individual report for a respondent."""
    # TODO: implement report export
    click.echo(f"Exporting report for {respondent_id}")


if __name__ == "__main__":  # pragma: no cover
    cli()
