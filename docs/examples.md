# Examples & Use Cases

Practical examples demonstrating how to use RAIL Score for various scenarios.

---

## Table of Contents

- [Content Moderation](#content-moderation)
- [Batch Processing](#batch-processing)
- [Compliance Checking](#compliance-checking)
- [RAG Evaluation](#rag-evaluation)
- [Quality Filtering](#quality-filtering)
- [Monitoring & Alerts](#monitoring--alerts)
- [A/B Testing](#ab-testing)
- [Report Generation](#report-generation)

---

## Content Moderation

### Basic Content Moderation

```python
from rail_score import RailScore

client = RailScore(api_key="your-key")

def moderate_content(user_content, threshold=7.0):
    """
    Moderate user-generated content.
    
    Returns: "APPROVED", "REVIEW", or "REJECTED"
    """
    result = client.evaluation.dimension(
        content=user_content,
        dimension="safety"
    )
    
    score = result['result']['score']
    
    if score >= threshold + 1:
        return "APPROVED"
    elif score >= threshold:
        return "REVIEW"
    else:
        return "REJECTED"

# Example usage
comments = [
    "This is a helpful product review.",
    "I'm not sure about this feature.",
    "This is completely inappropriate content!"
]

for comment in comments:
    status = moderate_content(comment)
    print(f"{status}: {comment[:50]}")
```

### Multi-Dimension Moderation

```python
def advanced_moderation(content, dimensions=None):
    """
    Check multiple dimensions for comprehensive moderation.
    """
    if dimensions is None:
        dimensions = ["safety", "fairness", "user_impact"]
    
    result = client.evaluation.custom(
        content=content,
        dimensions=dimensions
    )
    
    # Check if all dimensions pass threshold
    all_pass = all(
        score.score >= 7.0 
        for score in result.scores.values()
    )
    
    return {
        "approved": all_pass,
        "overall_score": result.rail_score.score,
        "dimension_scores": {
            name: score.score 
            for name, score in result.scores.items()
        },
        "issues": [
            f"{name}: {score.issues}"
            for name, score in result.scores.items()
            if score.issues
        ]
    }

# Example
result = advanced_moderation("User comment here")
print(f"Approved: {result['approved']}")
print(f"Score: {result['overall_score']:.2f}")
```

---

## Batch Processing

### Process Multiple Items

```python
def batch_evaluate_content(content_list, batch_size=100):
    """
    Evaluate multiple pieces of content efficiently.
    """
    results = []
    
    # Process in batches of 100 (API limit)
    for i in range(0, len(content_list), batch_size):
        batch = content_list[i:i + batch_size]
        items = [{"content": text} for text in batch]
        
        batch_result = client.evaluation.batch(
            items=items,
            dimensions=["safety", "privacy", "fairness"],
            tier="balanced"
        )
        
        results.extend(batch_result.results)
    
    return results

# Example with 250 items
content_list = ["Content " + str(i) for i in range(250)]
results = batch_evaluate_content(content_list)

print(f"Processed: {len(results)} items")
print(f"Average score: {sum(r.rail_score.score for r in results) / len(results):.2f}")
```

### Parallel Batch Processing

```python
from concurrent.futures import ThreadPoolExecutor
import time

def process_batch_parallel(content_list, max_workers=5):
    """
    Process multiple batches in parallel.
    """
    def process_single_batch(batch):
        items = [{"content": text} for text in batch]
        return client.evaluation.batch(
            items=items,
            tier="fast"
        )
    
    # Split into batches of 100
    batches = [
        content_list[i:i + 100] 
        for i in range(0, len(content_list), 100)
    ]
    
    # Process in parallel
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        batch_results = executor.map(process_single_batch, batches)
        
        for batch_result in batch_results:
            results.extend(batch_result.results)
    
    return results

# Example
start = time.time()
results = process_batch_parallel(content_list, max_workers=3)
print(f"Processed {len(results)} items in {time.time() - start:.2f}s")
```

---

## Compliance Checking

### GDPR Compliance Pipeline

```python
def check_gdpr_compliance(content, data_type="personal", region="EU"):
    """
    Comprehensive GDPR compliance check.
    """
    result = client.compliance.gdpr(
        content=content,
        context={
            "data_type": data_type,
            "region": region,
            "purpose": "service_provision"
        },
        strict_mode=True
    )
    
    # Generate compliance report
    report = {
        "compliant": result.failed == 0,
        "score": result.compliance_score,
        "summary": f"{result.passed}/{result.requirements_checked} checks passed",
        "violations": []
    }
    
    # Extract violations
    for req in result.requirements:
        if req.status == "FAIL":
            report["violations"].append({
                "requirement": req.requirement,
                "article": req.article,
                "issue": req.issue,
                "severity": "HIGH" if result.compliance_score < 5 else "MEDIUM"
            })
    
    return report

# Example
report = check_gdpr_compliance(
    "We collect user emails and share them with partners."
)

print(f"Compliant: {report['compliant']}")
print(f"Score: {report['score']:.2f}")
if report['violations']:
    print("\nViolations:")
    for v in report['violations']:
        print(f"  - {v['requirement']}: {v['issue']}")
```

### Multi-Regulation Compliance

```python
def check_all_compliance(content):
    """
    Check against multiple compliance frameworks.
    """
    frameworks = {
        "GDPR": client.compliance.gdpr,
        "CCPA": client.compliance.ccpa,
        "HIPAA": client.compliance.hipaa,
        "EU AI Act": client.compliance.ai_act
    }
    
    results = {}
    for name, check_func in frameworks.items():
        try:
            result = check_func(content)
            results[name] = {
                "score": result.compliance_score,
                "passed": result.failed == 0,
                "details": f"{result.passed}/{result.requirements_checked}"
            }
        except Exception as e:
            results[name] = {"error": str(e)}
    
    return results

# Example
results = check_all_compliance(
    "Healthcare AI system that processes patient data."
)

for framework, result in results.items():
    if "error" not in result:
        status = "✅" if result["passed"] else "❌"
        print(f"{status} {framework}: {result['score']:.2f}/10")
```

---

## RAG Evaluation

### Hallucination Detection

```python
def detect_hallucination(query, response, context_chunks, threshold=3.0):
    """
    Check if RAG response contains hallucinations.
    """
    result = client.evaluation.rag_evaluate(
        query=query,
        response=response,
        context_chunks=context_chunks
    )
    
    metrics = result['result']['rag_metrics']
    hallucination_score = metrics['hallucination_score']
    grounding_score = result['result']['grounding_score']
    
    return {
        "has_hallucination": hallucination_score >= threshold,
        "hallucination_score": hallucination_score,
        "grounding_score": grounding_score,
        "quality": metrics['overall_quality'],
        "recommendation": "REJECT" if hallucination_score >= threshold else "ACCEPT"
    }

# Example
result = detect_hallucination(
    query="What is the capital of France?",
    response="The capital of France is Paris, founded in 1789.",
    context_chunks=[
        {"content": "Paris is the capital and largest city of France."}
    ]
)

print(f"Hallucination: {result['has_hallucination']}")
print(f"Recommendation: {result['recommendation']}")
```

### RAG Quality Pipeline

```python
def rag_quality_pipeline(query, generated_response, context_chunks):
    """
    Complete RAG quality assurance pipeline.
    """
    # Step 1: Check for hallucinations
    hallucination_check = detect_hallucination(
        query, generated_response, context_chunks
    )
    
    # Step 2: Evaluate response quality
    quality_check = client.evaluation.dimension(
        content=generated_response,
        dimension="reliability"
    )
    
    # Step 3: Generate report
    report = {
        "query": query,
        "response": generated_response,
        "hallucination": hallucination_check,
        "reliability_score": quality_check['result']['score'],
        "overall_pass": (
            not hallucination_check['has_hallucination'] and
            quality_check['result']['score'] >= 7.0
        )
    }
    
    return report

# Example
report = rag_quality_pipeline(
    query="How does photosynthesis work?",
    generated_response="Photosynthesis is the process plants use to convert sunlight into energy.",
    context_chunks=[
        {"content": "Photosynthesis converts light energy into chemical energy."},
        {"content": "Plants use chlorophyll to capture sunlight."}
    ]
)

print(f"Quality Check: {'PASS' if report['overall_pass'] else 'FAIL'}")
```

---

## Quality Filtering

### Filter High-Quality Content

```python
def filter_by_quality(content_list, min_score=8.0, max_items=None):
    """
    Filter content by minimum quality score.
    """
    items = [{"content": text} for text in content_list]
    
    # Evaluate in batches
    result = client.evaluation.batch(
        items=items[:100],
        dimensions=["reliability", "user_impact", "safety"]
    )
    
    # Filter by score
    high_quality = []
    for i, item_result in enumerate(result.results):
        if item_result.rail_score.score >= min_score:
            high_quality.append({
                "content": content_list[i],
                "score": item_result.rail_score.score,
                "confidence": item_result.rail_score.confidence
            })
    
    # Sort by score
    high_quality.sort(key=lambda x: x['score'], reverse=True)
    
    if max_items:
        high_quality = high_quality[:max_items]
    
    return high_quality

# Example
content = [
    "AI is transforming healthcare through improved diagnostics.",
    "Click here now! Limited time offer!!!",
    "Machine learning improves efficiency in manufacturing."
]

filtered = filter_by_quality(content, min_score=7.5, max_items=10)
print(f"Found {len(filtered)} high-quality items")
for item in filtered:
    print(f"  {item['score']:.2f}: {item['content'][:50]}")
```

---

## Monitoring & Alerts

### Monitor Content Quality Over Time

```python
import time
from datetime import datetime

class QualityMonitor:
    def __init__(self, client, alert_threshold=7.0):
        self.client = client
        self.alert_threshold = alert_threshold
        self.history = []
    
    def evaluate_and_log(self, content):
        """Evaluate content and log results."""
        result = self.client.evaluation.basic(content)
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "score": result.rail_score.score,
            "confidence": result.rail_score.confidence,
            "content_preview": content[:100]
        }
        
        self.history.append(log_entry)
        
        # Check for alerts
        if result.rail_score.score < self.alert_threshold:
            self.trigger_alert(log_entry)
        
        return result
    
    def trigger_alert(self, log_entry):
        """Trigger alert for low-quality content."""
        print(f"⚠️  ALERT: Low quality detected!")
        print(f"   Score: {log_entry['score']:.2f}")
        print(f"   Time: {log_entry['timestamp']}")
        print(f"   Content: {log_entry['content_preview']}")
    
    def get_statistics(self):
        """Get quality statistics."""
        if not self.history:
            return None
        
        scores = [entry['score'] for entry in self.history]
        return {
            "count": len(scores),
            "average": sum(scores) / len(scores),
            "min": min(scores),
            "max": max(scores),
            "below_threshold": sum(1 for s in scores if s < self.alert_threshold)
        }

# Example usage
monitor = QualityMonitor(client, alert_threshold=7.0)

# Monitor content
contents = [
    "High quality AI content",
    "Spam content!!!",
    "Another good piece of content"
]

for content in contents:
    monitor.evaluate_and_log(content)
    time.sleep(1)

# Get statistics
stats = monitor.get_statistics()
print(f"\nStatistics:")
print(f"  Evaluated: {stats['count']} items")
print(f"  Average Score: {stats['average']:.2f}")
print(f"  Alerts: {stats['below_threshold']}")
```

---

## A/B Testing

### Compare Content Variants

```python
def ab_test_content(variant_a, variant_b, dimensions=None):
    """
    A/B test two content variants.
    """
    if dimensions is None:
        dimensions = ["safety", "user_impact", "reliability"]
    
    # Evaluate both variants
    result_a = client.evaluation.custom(
        content=variant_a,
        dimensions=dimensions
    )
    
    result_b = client.evaluation.custom(
        content=variant_b,
        dimensions=dimensions
    )
    
    # Compare scores
    comparison = {
        "variant_a": {
            "overall": result_a.rail_score.score,
            "dimensions": {
                name: score.score 
                for name, score in result_a.scores.items()
            }
        },
        "variant_b": {
            "overall": result_b.rail_score.score,
            "dimensions": {
                name: score.score 
                for name, score in result_b.scores.items()
            }
        },
        "winner": "A" if result_a.rail_score.score > result_b.rail_score.score else "B",
        "difference": abs(result_a.rail_score.score - result_b.rail_score.score)
    }
    
    return comparison

# Example
variant_a = "Our AI system is designed with your privacy in mind."
variant_b = "We use AI to personalize your experience while protecting your data."

result = ab_test_content(variant_a, variant_b)
print(f"Winner: Variant {result['winner']}")
print(f"Score difference: {result['difference']:.2f}")
```

---

## Report Generation

### Generate Quality Report

```python
def generate_quality_report(content_list):
    """
    Generate comprehensive quality report.
    """
    # Evaluate all content
    items = [{"content": text} for text in content_list]
    batch_result = client.evaluation.batch(items=items, tier="balanced")
    
    # Calculate statistics
    scores = [r.rail_score.score for r in batch_result.results]
    
    report = {
        "summary": {
            "total_items": len(scores),
            "average_score": sum(scores) / len(scores),
            "min_score": min(scores),
            "max_score": max(scores),
            "passing_rate": sum(1 for s in scores if s >= 7.0) / len(scores) * 100
        },
        "dimension_breakdown": {},
        "recommendations": []
    }
    
    # Dimension breakdown
    for dim in ["safety", "privacy", "fairness"]:
        dim_scores = [
            r.scores[dim].score 
            for r in batch_result.results 
            if dim in r.scores
        ]
        if dim_scores:
            report["dimension_breakdown"][dim] = {
                "average": sum(dim_scores) / len(dim_scores),
                "issues_count": sum(
                    1 for r in batch_result.results 
                    if r.scores.get(dim) and r.scores[dim].issues
                )
            }
    
    # Generate recommendations
    if report["summary"]["average_score"] < 7.0:
        report["recommendations"].append(
            "Overall quality is below threshold. Review content generation process."
        )
    
    return report

# Example
content_list = [
    "AI content piece 1",
    "AI content piece 2",
    "AI content piece 3"
]

report = generate_quality_report(content_list)
print(f"Average Score: {report['summary']['average_score']:.2f}")
print(f"Passing Rate: {report['summary']['passing_rate']:.1f}%")
```

---

## Next Steps

- Explore [Jupyter Notebooks](../examples/) for interactive examples
- Read the [API Reference](api-reference.md) for detailed documentation
- Check out the [Best Practices](best-practices.md) guide

## Need More Examples?

- [GitHub Issues](https://github.com/Responsible-AI-Labs/rail-score/issues) - Request specific examples
- [Email Support](mailto:support@responsibleailabs.ai) - Get help with your use case
