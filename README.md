# rail-score — DEPRECATED

> **This package has been renamed to [`rail-score-sdk`](https://pypi.org/project/rail-score-sdk/).**
> All future development, bug fixes, and new features are published there.

## Migration

```bash
pip uninstall rail-score
pip install rail-score-sdk
```

Then update your imports:

```python
# Old (deprecated)
from rail_score import RailScore
client = RailScore(api_key="...")

# New
from rail_score_sdk import RailScoreClient
client = RailScoreClient(api_key="...")
```

## What happened?

The `rail-score` package was the original v1 SDK. It has been superseded by
`rail-score-sdk`, which includes:

- **v2 API support** — new endpoints, new auth, new response models
- **Async client** — non-blocking httpx-based client
- **Policy engine** — block / regenerate / log behaviours
- **Multi-turn sessions** — conversation-aware evaluation
- **LLM provider wrappers** — OpenAI, Anthropic, Google GenAI
- **Observability** — Langfuse v3 integration, LiteLLM guardrail

## Compatibility shim

This package (v2.0.0) installs `rail-score-sdk` as a dependency and re-exports
its contents. Existing `from rail_score import ...` imports will continue to work
but will emit a `DeprecationWarning`.

## Links

- **New package**: https://pypi.org/project/rail-score-sdk/
- **Documentation**: https://responsibleailabs.ai/developer/docs
- **GitHub**: https://github.com/RAILethicsHub/rail-score
- **Support**: research@responsibleailabs.ai
