"""
RAIL Score — DEPRECATED. Use ``rail-score-sdk`` instead.
=========================================================

This package has been renamed to ``rail-score-sdk``.
All future development happens there.

Migration:
    pip uninstall rail-score
    pip install rail-score-sdk

Then update your imports:
    # Old
    from rail_score import RailScore
    # New
    from rail_score_sdk import RailScoreClient

For full documentation, see:
    https://github.com/RAILethicsHub/rail-score/tree/main/python
    https://pypi.org/project/rail-score-sdk/
"""

import warnings

warnings.warn(
    "\n\n"
    "  ⚠️  The 'rail-score' package is DEPRECATED and will not receive updates.\n"
    "  ➡️  Please switch to 'rail-score-sdk':\n\n"
    "      pip uninstall rail-score\n"
    "      pip install rail-score-sdk\n\n"
    "  Then update your imports:\n"
    "      from rail_score_sdk import RailScoreClient\n\n"
    "  Docs: https://pypi.org/project/rail-score-sdk/\n",
    DeprecationWarning,
    stacklevel=2,
)

# Re-export everything from the new package so existing code doesn't break
from rail_score_sdk import *  # noqa: F401, F403
from rail_score_sdk import RailScoreClient, __version__

# Backward compatibility alias: old package used `RailScore` as the client class
RailScore = RailScoreClient

__all__ = ["RailScore", "RailScoreClient"]
