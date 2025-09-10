"""Common API client with pagination and retry logic."""
from __future__ import annotations

import os
import time
from typing import Dict, Iterator, Any, Optional

import requests
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type


class APIError(Exception):
    """Custom exception for API errors."""


class APIClient:
    """Client for HRDK OpenAPI with basic retry and pagination support."""

    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or os.getenv("HRDK_API_KEY")
        if not self.api_key:
            raise RuntimeError("HRDK_API_KEY not set in environment")

    @retry(
        reraise=True,
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        retry=retry_if_exception_type((requests.HTTPError, APIError)),
    )
    def _request(self, url: str, params: Dict[str, Any]) -> Dict[str, Any]:
        params = {**params, "serviceKey": self.api_key}
        resp = requests.get(url, params=params, timeout=30)
        if resp.status_code >= 400:
            raise requests.HTTPError(f"HTTP {resp.status_code}: {resp.text}")
        try:
            return resp.json()
        except ValueError as exc:  # pragma: no cover - network issues
            raise APIError("Invalid JSON response") from exc

    def fetch_all(self, dataset_cfg: Dict[str, Any]) -> Iterator[Dict[str, Any]]:
        """Yield all records for a dataset configuration."""
        params = dict(dataset_cfg.get("params", {}))
        paging = dataset_cfg.get("paging", {})
        page_param = paging.get("page_param")
        size_param = paging.get("size_param")
        per_page = paging.get("per_page")
        page = params.get(page_param, 1) if page_param else None

        while True:
            data = self._request(dataset_cfg["endpoint"], params)
            items = self._extract_items(data, dataset_cfg.get("root_path"))
            if not items:
                break
            for item in items:
                yield item
            if not page_param:
                break
            page += 1
            params[page_param] = page
            if size_param and per_page:
                params[size_param] = per_page
            time.sleep(0.2)  # rate limit ~5 calls/sec

    @staticmethod
    def _extract_items(payload: Dict[str, Any], root_path: Optional[str]) -> list:
        if root_path:
            for key in root_path.split('.'):
                payload = payload.get(key, {})
        # naive extraction: find first list in payload
        if isinstance(payload, list):
            return payload
        for value in payload.values():
            if isinstance(value, list):
                return value
            if isinstance(value, dict):
                sub = APIClient._extract_items(value, None)
                if sub:
                    return sub
        return []
