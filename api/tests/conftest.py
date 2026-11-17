"""Shared test setup: make the repo's .env available to tests that need a key."""

from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]

# Loaded at import time so `live` tests can check ANTHROPIC_API_KEY at collection.
load_dotenv(REPO_ROOT / ".env")
