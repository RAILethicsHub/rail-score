# Quick Start Guide

Get started with RAIL Score in less than 5 minutes! This guide will walk you through your first evaluation.

---

## Step 1: Installation

First, install the RAIL Score SDK:

```bash
pip install rail-score
```

**Need more details?** See the [Installation Guide](installation.md).

---

## Step 2: Get Your API Key

1. Visit [responsibleailabs.ai](https://responsibleailabs.ai)
2. Sign up for a free account
3. Copy your API key from the dashboard

---

## Step 3: Your First Evaluation

Create a new Python file (`my_first_eval.py`) and add:

```python
from rail_score import RailScore

# Initialize the client
client = RailScore(api_key="your-api-key-here")

# Evaluate some content
result = client.evaluation.basic(
    "Our AI system prioritizes user privacy and data security."
)

# Print the results
print(f"Overall RAIL Score: {result.rail_score.score}/10")
print(f"Confidence: {result.rail_score.confidence}")
print(f"\nDimension Scores:")
for dim_name, dim_score in result.scores.items():
    print(f"  {dim_name}: {dim_score.score}/10")
```

Run it:

```bash
python my_first_eval.py
```

**Expected Output:**
```
Overall RAIL Score: 8.5/10
Confidence: 0.92

Dimension Scores:
  safety: 8.7/10
  privacy: 9.2/10
  fairness: 8.1/10
  transparency: 8.3/10
  accountability: 8.4/10
  reliability: 8.6/10
  legal_compliance: 8.8/10
  user_impact: 8.5/10
```

🎉 **Congratulations!** You've just performed your first RAIL Score evaluation!

---

## Step 4: Explore Different Evaluation Types

### Evaluate a Specific Dimension

Focus on one aspect, like safety:

```python
result = client.evaluation.dimension(
    content="This AI chatbot helps users with medical questions.",
    dimension="safety"
)

print(f"Safety Score: {result['result']['score']}/10")
print(f"Explanation: {result['result']['explanation']}")
if result['result']['issues']:
    print(f"Issues: {', '.join(result['result']['issues'])}")
```

### Batch Evaluation

Evaluate multiple items at once:

```python
items = [
    {"content": "AI helps doctors diagnose diseases faster."},
    {"content": "We collect user data for personalization."},
    {"content": "Our model is trained on diverse datasets."}
]

result = client.evaluation.batch(
    items=items,
    dimensions=["safety", "privacy", "fairness"]
)

print(f"Processed: {result.successful}/{result.total_items}")
for i, item_result in enumerate(result.results):
    print(f"\nItem {i+1}: {item_result.rail_score.score}/10")
```

### Check Compliance

Verify GDPR compliance:

```python
result = client.compliance.gdpr(
    content="We collect user emails for marketing purposes.",
    context={"data_type": "personal", "region": "EU"}
)

print(f"Compliance Score: {result.compliance_score}/10")
print(f"Status: {'✅ PASSED' if result.passed == result.requirements_checked else '❌ FAILED'}")

for req in result.requirements:
    status = "✅" if req.status == "PASS" else "❌"
    print(f"{status} {req.requirement}")
```

---

## Step 5: Understand the Response

Every evaluation returns structured data:

```python
result = client.evaluation.basic("AI content here")

# Overall score
print(result.rail_score.score)        # 0-10
print(result.rail_score.confidence)   # 0-1

# Individual dimension scores
for dim_name, dim_score in result.scores.items():
    print(f"{dim_name}:")
    print(f"  Score: {dim_score.score}")
    print(f"  Confidence: {dim_score.confidence}")
    print(f"  Explanation: {dim_score.explanation}")
    if dim_score.issues:
        print(f"  Issues: {dim_score.issues}")

# Metadata
print(f"Request ID: {result.metadata.req_id}")
print(f"Credits Used: {result.metadata.credits_consumed}")
print(f"Processing Time: {result.metadata.processing_time_ms}ms")
```

---

## Step 6: Handle Errors

Add proper error handling:

```python
from rail_score import (
    RailScore,
    AuthenticationError,
    InsufficientCreditsError,
    ValidationError,
    RateLimitError
)

client = RailScore(api_key="your-api-key")

try:
    result = client.evaluation.basic("Content to evaluate")
    print(f"Score: {result.rail_score.score}")
    
except AuthenticationError:
    print("❌ Invalid API key. Check your credentials.")
    
except InsufficientCreditsError as e:
    print(f"❌ Not enough credits. Balance: {e.balance}, Required: {e.required}")
    
except ValidationError as e:
    print(f"❌ Invalid input: {e}")
    
except RateLimitError as e:
    print(f"❌ Rate limit exceeded. Retry after {e.retry_after}s")
    
except Exception as e:
    print(f"❌ Unexpected error: {e}")
```

---

## Common Use Cases

### Use Case 1: Content Moderation

```python
def moderate_content(user_content):
    """Check if user content is safe to publish."""
    result = client.evaluation.dimension(
        content=user_content,
        dimension="safety"
    )
    
    score = result['result']['score']
    
    if score >= 8.0:
        return "APPROVED"
    elif score >= 6.0:
        return "REVIEW"
    else:
        return "REJECTED"

# Example usage
status = moderate_content("This is a user comment.")
print(f"Moderation Status: {status}")
```

### Use Case 2: RAG Quality Check

```python
def check_rag_response(query, response, context_chunks):
    """Verify RAG response is grounded and not hallucinating."""
    result = client.evaluation.rag_evaluate(
        query=query,
        response=response,
        context_chunks=context_chunks
    )
    
    metrics = result['result']['rag_metrics']
    hallucination = metrics['hallucination_score']
    grounding = result['result']['grounding_score']
    
    return {
        "is_grounded": grounding >= 7.0,
        "has_hallucination": hallucination >= 3.0,
        "quality": metrics['overall_quality']
    }

# Example usage
quality = check_rag_response(
    query="What is the capital of France?",
    response="The capital of France is Paris.",
    context_chunks=[{"content": "Paris is the capital of France."}]
)
print(quality)
```

### Use Case 3: Filter by Quality

```python
def filter_high_quality_content(content_list, min_score=8.0):
    """Keep only high-quality AI-generated content."""
    items = [{"content": text} for text in content_list]
    
    result = client.evaluation.batch(
        items=items[:100],  # Max 100 items
        dimensions=["safety", "reliability", "user_impact"]
    )
    
    high_quality = []
    for i, item_result in enumerate(result.results):
        if item_result.rail_score.score >= min_score:
            high_quality.append(content_list[i])
    
    return high_quality

# Example usage
content = [
    "AI is transforming healthcare.",
    "Buy now! Limited offer!!!",
    "Machine learning improves efficiency."
]

filtered = filter_high_quality_content(content, min_score=7.5)
print(f"Kept {len(filtered)}/{len(content)} items")
```

---

## Best Practices

### 1. Use Environment Variables for API Keys

```python
import os
from rail_score import RailScore

# Good: Use environment variable
client = RailScore(api_key=os.getenv("RAIL_API_KEY"))

# Bad: Hardcode API key
# client = RailScore(api_key="sk-123...")  # Don't do this!
```

### 2. Cache Results When Possible

```python
import functools

@functools.lru_cache(maxsize=100)
def get_content_score(content):
    """Cache evaluation results."""
    result = client.evaluation.basic(content)
    return result.rail_score.score

# This will only call the API once for the same content
score1 = get_content_score("Same content")
score2 = get_content_score("Same content")  # Uses cached result
```

### 3. Use Batch Evaluation for Multiple Items

```python
# Good: Batch evaluation
items = [{"content": text} for text in content_list]
result = client.evaluation.batch(items=items)

# Bad: Individual evaluations
# for text in content_list:
#     result = client.evaluation.basic(text)  # Don't do this!
```

### 4. Check Credits Regularly

```python
def check_available_credits():
    """Monitor credit usage."""
    credits = client.get_credits()
    remaining = credits['credits']['remaining']
    
    if remaining < 10:
        print(f"⚠️  Low credits: {remaining} remaining")
    
    return remaining

# Check before large batch operations
if check_available_credits() > 50:
    # Process batch
    pass
```

---

## What's Next?

Now that you know the basics, explore more advanced features:

- **[API Reference](api-reference.md)** - Complete API documentation
- **[Examples](examples.md)** - More real-world examples
- **[Content Moderation Guide](guides/content-moderation.md)** - Deep dive into moderation
- **[RAG Evaluation Guide](guides/rag-evaluation.md)** - Detect hallucinations
- **[Compliance Guide](guides/compliance.md)** - Automate compliance checks

---

## Need Help?

- 📖 [Full Documentation](index.md)
- 🐛 [Report Issues](https://github.com/Responsible-AI-Labs/rail-score/issues)
- 📧 [Email Support](mailto:support@responsibleailabs.ai)
- 💬 [Community Discussions](https://github.com/Responsible-AI-Labs/rail-score/discussions)

---

**Happy evaluating! 🚀**
