"""Picking the columns that model going to use"""

from src.config import FEATURE_COLS


def make_features(raw):
    return raw[FEATURE_COLS].copy()