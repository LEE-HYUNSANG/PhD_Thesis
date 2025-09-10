"""Pydantic models for NCS datasets."""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class NCSUnit(BaseModel):
    code: str
    name: str
    level: Optional[int] = None
    definition: Optional[str] = Field(None, alias="def")
    large: Optional[str] = None
    medium: Optional[str] = None
    small: Optional[str] = None
    detail: Optional[str] = None


class JobBasicSkill(BaseModel):
    unit_code: str
    unit_name: Optional[str] = None
    basic_name: str
    basic_factor: str


class UnitLicenseMap(BaseModel):
    unit_code: str
    unit_name: Optional[str] = None
    jm_code: str
    jm_name: Optional[str] = None
    total_hours: Optional[int] = None
    basic_hours: Optional[int] = None
    must_hours: Optional[int] = None
    opt_hours: Optional[int] = None
    org: Optional[str] = Field(None, alias="exam_org")
    min_hours: Optional[int] = None


class TrainingCourse(BaseModel):
    unit_code: str
    unit_name: Optional[str] = None
    level: Optional[int] = None
    goal: Optional[str] = None
    hours: Optional[int] = None
    facility: Optional[str] = None
    method: Optional[str] = None


class AcademicCurriculum(BaseModel):
    large_cd: str
    dept: str
    subject: str
    hours: Optional[int] = None
    credit: Optional[float] = None
    theory: Optional[bool] = None
    practice: Optional[bool] = None
    teamproj: Optional[bool] = None


class KSAStandard(BaseModel):
    duty_code: str
    unit_code: str
    element_no: str
    ksa_type: str
    ksa_name: Optional[str] = None
    ksa_text: Optional[str] = None


class Utilization(BaseModel):
    unit_code: str
    unit_name: Optional[str] = None
    career_path_url: Optional[str] = None
    career_period: Optional[str] = None
    related_license: Optional[str] = None
