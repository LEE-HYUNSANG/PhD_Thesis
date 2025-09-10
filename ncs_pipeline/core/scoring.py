"""Scoring utilities for PE-fit and RDI calculations."""
from __future__ import annotations

from typing import List, Dict
import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Return cosine similarity between two vectors."""
    if not a.any() or not b.any():
        return 0.0
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def score_student_vs_job(student_vec: Dict[str, List[float]], job_vec: Dict[str, List[float]]) -> float:
    """Compute overall fit score between student and job vectors.

    Parameters
    ----------
    student_vec: dict
        Contains vector components for the student.
    job_vec: dict
        Contains vector components for the job.
    """
    riasec_fit = cosine_similarity(
        np.array(student_vec.get("riasec", [])),
        np.array(job_vec.get("riasec", [])),
    )
    value_fit = cosine_similarity(
        np.array(student_vec.get("values", [])),
        np.array(job_vec.get("values", [])),
    )
    skill_fit = cosine_similarity(
        np.array(student_vec.get("skills", [])),
        np.array(job_vec.get("skills", [])),
    )
    return float(0.4 * riasec_fit + 0.3 * value_fit + 0.3 * skill_fit)
