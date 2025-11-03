# API Reference

Complete API documentation for the RAIL Score Python SDK.

---

## Table of Contents

- [Client Initialization](#client-initialization)
- [Evaluation API](#evaluation-api)
- [Generation API](#generation-api)
- [Compliance API](#compliance-api)
- [Utilities](#utilities)
- [Data Models](#data-models)
- [Exceptions](#exceptions)

---

## Client Initialization

### `RailScore`

Main client class for interacting with the RAIL Score API.

```python
from rail_score import RailScore

client = RailScore(
    api_key: str,
    base_url: str = "https://api.responsibleailabs.ai",
    timeout: int = 60
)
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api_key` | `str` | Required | Your RAIL Score API key |
| `base_url` | `str` | `"https://api.responsibleailabs.ai"` | API base URL |
| `timeout` | `int` | `60` | Request timeout in seconds |

**Returns:** `RailScore` client instance

**Example:**

```python
import os
from rail_score import RailScore

# Using environment variable (recommended)
client = RailScore(api_key=os.getenv("RAIL_API_KEY"))

# With custom configuration
client = RailScore(
    api_key="your-api-key",
    base_url="https://api.responsibleailabs.ai",
    timeout=120
)
```

---

## Evaluation API

### `client.evaluation.basic()`

Evaluate content across all 8 RAIL dimensions.

```python
result = client.evaluation.basic(
    content: str,
    weights: Optional[Dict[str, float]] = None
) -> EvaluationResult
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | `str` | Required | Content to evaluate |
| `weights` | `Optional[Dict[str, float]]` | `None` | Custom dimension weights (must sum to 100) |

**Returns:** `EvaluationResult` object with:
- `rail_score`: Overall RAIL score (0-10) and confidence
- `scores`: Dictionary of dimension scores
- `metadata`: Request metadata

**Example:**

```python
# Basic evaluation
result = client.evaluation.basic(
    "Our AI system ensures user privacy and data security."
)

print(f"Score: {result.rail_score.score}")
print(f"Confidence: {result.rail_score.confidence}")

# With custom weights
weights = {
    "safety": 30,
    "privacy": 30,
    "reliability": 20,
    "accountability": 10,
    "transparency": 5,
    "fairness": 3,
    "inclusivity": 1,
    "user_impact": 1
}

result = client.evaluation.basic(
    "Content here",
    weights=weights
)
```

---

### `client.evaluation.dimension()`

Evaluate content on a single specific dimension.

```python
result = client.evaluation.dimension(
    content: str,
    dimension: str
) -> Dict[str, Any]
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `content` | `str` | Content to evaluate |
| `dimension` | `str` | One of: `"safety"`, `"privacy"`, `"fairness"`, `"transparency"`, `"accountability"`, `"reliability"`, `"legal_compliance"`, `"user_impact"` |

**Returns:** Dictionary with:
- `result['score']`: Dimension score (0-10)
- `result['confidence']`: Confidence level (0-1)
- `result['explanation']`: Detailed explanation
- `result['issues']`: List of identified issues

**Example:**

```python
result = client.evaluation.dimension(
    content="We collect user data with consent.",
    dimension="privacy"
)

print(f"Privacy Score: {result['result']['score']}")
print(f"Explanation: {result['result']['explanation']}")
```

---

### `client.evaluation.custom()`

Evaluate specific dimensions with optional custom weights.

```python
result = client.evaluation.custom(
    content: str,
    dimensions: List[str],
    weights: Optional[Dict[str, float]] = None
) -> EvaluationResult
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | `str` | Required | Content to evaluate |
| `dimensions` | `List[str]` | Required | List of dimensions to evaluate |
| `weights` | `Optional[Dict[str, float]]` | `None` | Weights for specified dimensions |

**Returns:** `EvaluationResult` object

**Example:**

```python
result = client.evaluation.custom(
    content="Healthcare AI system",
    dimensions=["safety", "privacy", "reliability"],
    weights={"safety": 50, "privacy": 30, "reliability": 20}
)
```

---

### `client.evaluation.weighted()`

Evaluate with custom dimension weights.

```python
result = client.evaluation.weighted(
    content: str,
    weights: Dict[str, float]
) -> EvaluationResult
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `content` | `str` | Content to evaluate |
| `weights` | `Dict[str, float]` | Dimension weights (must sum to 100) |

**Returns:** `EvaluationResult` object

**Example:**

```python
weights = {
    "safety": 40,
    "privacy": 30,
    "fairness": 15,
    "transparency": 10,
    "accountability": 5
}

result = client.evaluation.weighted("Content here", weights=weights)
```

---

### `client.evaluation.detailed()`

Get detailed evaluation with strengths, weaknesses, and improvements.

```python
result = client.evaluation.detailed(
    content: str
) -> Dict[str, Any]
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `content` | `str` | Content to evaluate |

**Returns:** Dictionary with detailed breakdown including:
- `result['summary']['strengths']`: List of strengths
- `result['summary']['weaknesses']`: List of weaknesses
- `result['summary']['improvements_needed']`: Suggested improvements

**Example:**

```python
result = client.evaluation.detailed("AI model description")

summary = result['result']['summary']
print(f"Strengths: {summary['strengths']}")
print(f"Weaknesses: {summary['weaknesses']}")
print(f"Improvements: {summary['improvements_needed']}")
```

---

### `client.evaluation.advanced()`

Ensemble evaluation with higher confidence.

```python
result = client.evaluation.advanced(
    content: str,
    context: Optional[str] = None
) -> EvaluationResult
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | `str` | Required | Content to evaluate |
| `context` | `Optional[str]` | `None` | Additional context for evaluation |

**Returns:** `EvaluationResult` object with typically 0.90+ confidence

**Example:**

```python
result = client.evaluation.advanced(
    content="Critical AI system",
    context="Healthcare decision support system"
)

print(f"Confidence: {result.rail_score.confidence}")  # Typically 0.90+
```

---

### `client.evaluation.batch()`

Evaluate multiple items in a single request (up to 100 items).

```python
result = client.evaluation.batch(
    items: List[Dict[str, str]],
    dimensions: Optional[List[str]] = None,
    tier: str = "balanced"
) -> BatchEvaluationResult
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `items` | `List[Dict[str, str]]` | Required | List of items with `"content"` key (max 100) |
| `dimensions` | `Optional[List[str]]` | `None` | Dimensions to evaluate (defaults to all) |
| `tier` | `str` | `"balanced"` | One of: `"fast"`, `"balanced"`, `"advanced"` |

**Returns:** `BatchEvaluationResult` with:
- `results`: List of evaluation results
- `total_items`: Total number of items
- `successful`: Number of successful evaluations
- `failed`: Number of failed evaluations

**Example:**

```python
items = [
    {"content": "First AI text"},
    {"content": "Second AI text"},
    {"content": "Third AI text"}
]

result = client.evaluation.batch(
    items=items,
    dimensions=["safety", "privacy"],
    tier="balanced"
)

print(f"Processed: {result.successful}/{result.total_items}")

for i, item_result in enumerate(result.results):
    print(f"Item {i+1}: {item_result.rail_score.score}")
```

---

### `client.evaluation.rag_evaluate()`

Evaluate RAG (Retrieval-Augmented Generation) responses for hallucinations.

```python
result = client.evaluation.rag_evaluate(
    query: str,
    response: str,
    context_chunks: List[Dict[str, str]]
) -> Dict[str, Any]
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `query` | `str` | Original query |
| `response` | `str` | Generated response |
| `context_chunks` | `List[Dict[str, str]]` | Context chunks with `"content"` key |

**Returns:** Dictionary with:
- `result['rag_metrics']['hallucination_score']`: Hallucination score (lower is better)
- `result['grounding_score']`: How well grounded in context (higher is better)
- `result['rag_metrics']['overall_quality']`: Overall response quality

**Example:**

```python
result = client.evaluation.rag_evaluate(
    query="What is the capital of France?",
    response="The capital of France is Paris.",
    context_chunks=[
        {"content": "Paris is the capital city of France."},
        {"content": "France is a country in Western Europe."}
    ]
)

metrics = result['result']['rag_metrics']
print(f"Hallucination: {metrics['hallucination_score']}")
print(f"Grounding: {result['result']['grounding_score']}")
```

---

## Generation API

### `client.generation.rag_chat()`

Generate context-grounded responses.

```python
result = client.generation.rag_chat(
    query: str,
    context: str,
    max_tokens: int = 300,
    model: str = "gpt-4o-mini"
) -> GenerationResult
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | `str` | Required | User query |
| `context` | `str` | Required | Context for grounding |
| `max_tokens` | `int` | `300` | Maximum tokens to generate |
| `model` | `str` | `"gpt-4o-mini"` | Model to use |

**Returns:** `GenerationResult` with:
- `generated_text`: Generated response
- `usage`: Token usage statistics
- `metadata`: Request metadata

**Example:**

```python
result = client.generation.rag_chat(
    query="What are the benefits of GDPR?",
    context="GDPR provides data protection and privacy rights...",
    max_tokens=300,
    model="gpt-4o-mini"
)

print(result.generated_text)
print(f"Tokens: {result.usage['total_tokens']}")
```

---

### `client.generation.reprompt()`

Get suggestions to improve content scores.

```python
result = client.generation.reprompt(
    content: str,
    current_scores: Dict[str, Dict[str, float]],
    target_score: float = 8.0,
    focus_dimensions: Optional[List[str]] = None
) -> Dict[str, Any]
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | `str` | Required | Current content |
| `current_scores` | `Dict` | Required | Current dimension scores |
| `target_score` | `float` | `8.0` | Target score to achieve |
| `focus_dimensions` | `Optional[List[str]]` | `None` | Dimensions to focus on |

**Returns:** Dictionary with improvement suggestions

**Example:**

```python
current_scores = {
    "transparency": {"score": 4.5},
    "accountability": {"score": 5.0}
}

result = client.generation.reprompt(
    content="AI makes decisions automatically",
    current_scores=current_scores,
    target_score=8.0,
    focus_dimensions=["transparency", "accountability"]
)

suggestions = result['result']['improvement_suggestions']
print(suggestions['text_replacements'])
```

---

### `client.generation.protected_generate()`

Generate content with safety filters and minimum RAIL score.

```python
result = client.generation.protected_generate(
    prompt: str,
    max_tokens: int = 200,
    min_rail_score: float = 8.0
) -> ProtectedGenerationResult
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `prompt` | `str` | Required | Generation prompt |
| `max_tokens` | `int` | `200` | Maximum tokens |
| `min_rail_score` | `float` | `8.0` | Minimum acceptable RAIL score |

**Returns:** `ProtectedGenerationResult` with:
- `generated_text`: Generated content
- `rail_score`: RAIL score of generated content
- `safety_passed`: Whether content passed safety checks

**Example:**

```python
result = client.generation.protected_generate(
    prompt="Write a description for an AI hiring tool",
    max_tokens=200,
    min_rail_score=8.0
)

print(result.generated_text)
print(f"Score: {result.rail_score}")
print(f"Safe: {result.safety_passed}")
```

---

## Compliance API

### `client.compliance.gdpr()`

Check GDPR compliance.

```python
result = client.compliance.gdpr(
    content: str,
    context: Optional[Dict[str, Any]] = None,
    strict_mode: bool = False
) -> ComplianceResult
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | `str` | Required | Content to check |
| `context` | `Optional[Dict]` | `None` | Additional context (data_type, region, purpose) |
| `strict_mode` | `bool` | `False` | Use 7.5 threshold instead of 7.0 |

**Returns:** `ComplianceResult` with:
- `compliance_score`: Overall compliance score
- `requirements_checked`: Total requirements checked
- `passed`: Number of requirements passed
- `failed`: Number of requirements failed
- `requirements`: List of requirement details

**Example:**

```python
result = client.compliance.gdpr(
    content="We collect user emails for marketing.",
    context={"data_type": "personal", "region": "EU"},
    strict_mode=True
)

print(f"Score: {result.compliance_score}")
print(f"Passed: {result.passed}/{result.requirements_checked}")

for req in result.requirements:
    print(f"{req.requirement} ({req.article}): {req.status}")
    if req.status == "FAIL":
        print(f"  Issue: {req.issue}")
```

---

### `client.compliance.ccpa()`

Check CCPA (California Consumer Privacy Act) compliance.

```python
result = client.compliance.ccpa(
    content: str,
    context: Optional[Dict[str, Any]] = None
) -> ComplianceResult
```

**Example:**

```python
result = client.compliance.ccpa(
    "We share user data with third parties."
)

print(f"CCPA Score: {result.compliance_score}")
```

---

### `client.compliance.hipaa()`

Check HIPAA (Health Insurance Portability and Accountability Act) compliance.

```python
result = client.compliance.hipaa(
    content: str,
    context: Optional[Dict[str, Any]] = None
) -> ComplianceResult
```

**Example:**

```python
result = client.compliance.hipaa(
    "Healthcare AI system processes patient records."
)

print(f"HIPAA Score: {result.compliance_score}")
```

---

### `client.compliance.ai_act()`

Check EU AI Act compliance.

```python
result = client.compliance.ai_act(
    content: str,
    context: Optional[Dict[str, Any]] = None
) -> ComplianceResult
```

**Example:**

```python
result = client.compliance.ai_act(
    "AI system for credit scoring."
)

print(f"EU AI Act Score: {result.compliance_score}")
```

---

## Utilities

### `client.get_credits()`

Get current credit balance and usage.

```python
credits = client.get_credits() -> Dict[str, Any]
```

**Returns:** Dictionary with:
- `plan`: Current plan name
- `credits['monthly_limit']`: Monthly credit limit
- `credits['used_this_month']`: Credits used this month
- `credits['remaining']`: Remaining credits

**Example:**

```python
credits = client.get_credits()

print(f"Plan: {credits['plan']}")
print(f"Remaining: {credits['credits']['remaining']}")
```

---

### `client.get_usage()`

Get usage history.

```python
usage = client.get_usage(
    limit: int = 50,
    from_date: Optional[str] = None
) -> Dict[str, Any]
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `limit` | `int` | `50` | Number of records to retrieve |
| `from_date` | `Optional[str]` | `None` | Start date (ISO format) |

**Returns:** Dictionary with usage history

**Example:**

```python
usage = client.get_usage(
    limit=50,
    from_date="2025-01-01T00:00:00Z"
)

print(f"Total: {usage['total_records']}")
print(f"Credits: {usage['total_credits_used']}")

for entry in usage['history']:
    print(f"{entry['timestamp']}: {entry['endpoint']} - {entry['credits_used']}")
```

---

### `client.health_check()`

Check API health and status.

```python
health = client.health_check() -> Dict[str, Any]
```

**Returns:** Dictionary with:
- `ok`: Boolean status
- `version`: API version

**Example:**

```python
health = client.health_check()

if health['ok']:
    print(f"✅ API is healthy (v{health['version']})")
else:
    print("❌ API is down")
```

---

## Data Models

### `EvaluationResult`

```python
class EvaluationResult:
    rail_score: RailScore
    scores: Dict[str, DimensionScore]
    metadata: Metadata
```

### `RailScore`

```python
class RailScore:
    score: float  # 0-10
    confidence: float  # 0-1
```

### `DimensionScore`

```python
class DimensionScore:
    score: float
    confidence: float
    explanation: str
    issues: Optional[List[str]]
```

### `Metadata`

```python
class Metadata:
    req_id: str
    tier: str
    queue_wait_time_ms: float
    processing_time_ms: float
    credits_consumed: float
    timestamp: str
```

---

## Exceptions

### `AuthenticationError`

Raised when API key is invalid or missing.

```python
from rail_score import AuthenticationError

try:
    result = client.evaluation.basic("content")
except AuthenticationError:
    print("Invalid API key")
```

---

### `InsufficientCreditsError`

Raised when account has insufficient credits.

```python
from rail_score import InsufficientCreditsError

try:
    result = client.evaluation.basic("content")
except InsufficientCreditsError as e:
    print(f"Balance: {e.balance}, Required: {e.required}")
```

---

### `ValidationError`

Raised when request parameters are invalid.

```python
from rail_score import ValidationError

try:
    result = client.evaluation.dimension("content", dimension="invalid")
except ValidationError as e:
    print(f"Invalid input: {e}")
```

---

### `RateLimitError`

Raised when rate limit is exceeded.

```python
from rail_score import RateLimitError

try:
    result = client.evaluation.basic("content")
except RateLimitError as e:
    print(f"Retry after {e.retry_after} seconds")
```

---

### `PlanUpgradeRequired`

Raised when endpoint requires a higher plan tier.

```python
from rail_score import PlanUpgradeRequired

try:
    result = client.evaluation.advanced("content")
except PlanUpgradeRequired:
    print("Upgrade to Pro plan required")
```

---

## See Also

- [Quick Start Guide](quickstart.md)
- [Examples](examples.md)
- [Error Handling Guide](error-handling.md)
