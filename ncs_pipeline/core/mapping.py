"""Logic for mapping KSIC -> Job group -> NCS unit."""
from __future__ import annotations

from typing import Optional
import pandas as pd


class OntologyMapping:
    """Placeholder class for ontology mapping operations."""

    def __init__(self, mapping_path: Optional[str] = None) -> None:
        self.mapping_path = mapping_path

    def load(self) -> pd.DataFrame:
        """Load mapping file into a DataFrame."""
        if not self.mapping_path:
            raise ValueError("mapping_path not provided")
        return pd.read_csv(self.mapping_path)

    def resolve_job_profile(self, unit_code: str) -> dict:
        """Return a job profile vector for the given NCS unit."""
        # TODO: implement actual resolution logic
        return {"unit_code": unit_code, "vector": []}
