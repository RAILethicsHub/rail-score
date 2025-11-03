# RAIL Score Python SDK

**Evaluate and generate responsible AI content with the official Python client for RAIL Score API**

[![PyPI version](https://badge.fury.io/py/rail-score.svg)](https://badge.fury.io/py/rail-score)
[![Python Versions](https://img.shields.io/pypi/pyversions/rail-score.svg)](https://pypi.org/project/rail-score/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## What is RAIL Score?

RAIL Score is a comprehensive framework for evaluating AI systems across **8 critical dimensions**:

- 🛡️ **Safety**: Content safety and harm prevention
- 🔒 **Privacy**: Data protection and privacy preservation
- ⚖️ **Fairness**: Bias detection and equitable outcomes
- 📊 **Transparency**: Explainability and clarity
- ✅ **Accountability**: Responsibility and auditability
- 🎯 **Reliability**: Consistency and accuracy
- 📜 **Legal Compliance**: Regulatory adherence
- 👥 **User Impact**: Positive user experience

This SDK provides easy-to-use Python bindings for the RAIL Score API, enabling you to integrate responsible AI evaluation directly into your applications.

---

## ⚡ Quick Install

```bash
pip install rail-score
```

---

## 🚀 Quick Start

```python
from rail_score import RailScore

# Initialize client
client = RailScore(api_key="your-rail-api-key")

# Evaluate content
result = client.evaluation.basic("Our AI system ensures user privacy and data security.")

# Access scores
print(f"Overall RAIL Score: {result.rail_score.score}")
print(f"Privacy Score: {result.scores['privacy'].score}")
```

Get your API key at [responsibleailabs.ai](https://responsibleailabs.ai)

---

## ✨ Key Features

### 🎯 Multiple Evaluation Modes
- **Basic**: Quick evaluation across all 8 dimensions
- **Dimension-Specific**: Focus on individual aspects (safety, privacy, fairness, etc.)
- **Custom**: Choose specific dimensions to evaluate
- **Weighted**: Apply custom importance weights
- **Detailed**: Get comprehensive breakdown with improvement suggestions
- **Advanced**: Ensemble evaluation with higher confidence (0.90+)
- **Batch**: Process up to 100 items efficiently
- **RAG**: Evaluate RAG responses for hallucinations

### 🤖 AI Generation
- Generate context-grounded responses (RAG Chat)
- Get AI-powered improvement suggestions (Reprompting)
- Create safe content with minimum quality thresholds (Protected Generation)

### ✅ Compliance Checks
Built-in support for major compliance frameworks:
- 🇪🇺 **GDPR** (EU General Data Protection Regulation)
- 🇺🇸 **CCPA** (California Consumer Privacy Act)
- 🏥 **HIPAA** (Healthcare data protection)
- 🤖 **EU AI Act** (Artificial Intelligence regulation)

### 🔧 Developer-Friendly
- ✅ **Type-safe**: Full typing support with IDE autocomplete
- 🔄 **Auto-retry**: Built-in error handling and retries
- 📊 **Detailed metadata**: Request IDs, credits, processing times
- ⚠️ **Rich errors**: Comprehensive exception handling
- 📈 **Usage tracking**: Monitor credits and API usage

---

## 📖 Example: Batch Content Moderation

```python
from rail_score import RailScore

client = RailScore(api_key="your-key")

# Evaluate multiple items
items = [
    {"content": "First piece of content"},
    {"content": "Second piece of content"},
    {"content": "Third piece of content"}
]

result = client.evaluation.batch(
    items=items,
    dimensions=["safety", "privacy", "fairness"],
    tier="balanced"
)

# Filter safe content
safe_items = [
    item for i, item in enumerate(items)
    if result.results[i].rail_score.score >= 7.5
]

print(f"Safe content: {len(safe_items)}/{len(items)}")
```

---

## 📖 Example: GDPR Compliance Check

```python
result = client.compliance.gdpr(
    content="We collect user data for personalized recommendations",
    context={"data_type": "personal", "region": "EU"},
    strict_mode=True
)

print(f"Compliance Score: {result.compliance_score}")
print(f"Passed: {result.passed}/{result.requirements_checked}")

for req in result.requirements:
    if req.status == "FAIL":
        print(f"❌ {req.requirement}: {req.issue}")
```

---

## 📖 Example: RAG Hallucination Detection

```python
result = client.evaluation.rag_evaluate(
    query="What is the capital of France?",
    response="The capital of France is Paris, located in the Île-de-France region.",
    context_chunks=[
        {"content": "Paris is the capital and largest city of France."},
        {"content": "The Île-de-France region surrounds Paris."}
    ]
)

metrics = result['result']['rag_metrics']
print(f"Hallucination Score: {metrics['hallucination_score']}")  # Lower is better
print(f"Grounding Score: {result['result']['grounding_score']}")  # Higher is better
```

---

## 🎓 Use Cases

- **Content Moderation**: Evaluate user-generated content for safety and compliance
- **AI Model Evaluation**: Assess LLM outputs across responsible AI dimensions
- **Compliance Automation**: Automated GDPR, HIPAA, CCPA checks
- **RAG Quality Assurance**: Detect hallucinations in retrieval-augmented generation
- **Policy Enforcement**: Ensure AI-generated content meets organizational standards
- **Research & Development**: Benchmark responsible AI metrics

---

## 📚 Documentation & Resources

- **Full Documentation**: [responsibleailabs.ai/docs](https://responsibleailabs.ai/docs)
- **API Reference**: [responsibleailabs.ai/docs/api](https://responsibleailabs.ai/docs/api)
- **GitHub Repository**: [github.com/Responsible-AI-Labs/rail-score](https://github.com/Responsible-AI-Labs/rail-score)
- **Research Paper**: [RAIL in the Wild (arXiv)](https://arxiv.org/abs/2505.00204)
- **Issue Tracker**: [GitHub Issues](https://github.com/Responsible-AI-Labs/rail-score/issues)

---

## 🔧 Requirements

- Python 3.8 or higher
- `requests >= 2.28.0`

---

## 📄 License

MIT License - see [LICENSE](https://github.com/Responsible-AI-Labs/rail-score/blob/main/LICENSE) for details.

---

## 🤝 Support

- **Email**: [support@responsibleailabs.ai](mailto:support@responsibleailabs.ai)
- **Website**: [responsibleailabs.ai](https://responsibleailabs.ai)
- **GitHub Issues**: [Report a bug or request a feature](https://github.com/Responsible-AI-Labs/rail-score/issues)

---

**Made with ❤️ by [Responsible AI Labs](https://responsibleailabs.ai)**
