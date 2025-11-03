# RAIL Score Python SDK Documentation

Welcome to the official documentation for the RAIL Score Python SDK!

## 🎯 What is RAIL Score?

RAIL Score is a comprehensive framework for evaluating AI systems across **8 critical dimensions** of Responsible AI:

| Dimension | Description |
|-----------|-------------|
| **Safety** | Content safety and harm prevention |
| **Privacy** | Data protection and privacy preservation |
| **Fairness** | Bias detection and equitable outcomes |
| **Transparency** | Explainability and clarity |
| **Accountability** | Responsibility and auditability |
| **Reliability** | Consistency and accuracy |
| **Legal Compliance** | Regulatory adherence (GDPR, HIPAA, CCPA, EU AI Act) |
| **User Impact** | Positive user experience |

This Python SDK provides easy-to-use bindings for the RAIL Score API, enabling you to integrate responsible AI evaluation directly into your applications.

---

## 🚀 Quick Start

Get started in less than 5 minutes:

```bash
pip install rail-score
```

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

**[→ Full Quick Start Guide](quickstart.md)**

---

## 📖 Documentation Sections

### Getting Started
- **[Installation Guide](installation.md)** - Detailed installation instructions
- **[Quick Start](quickstart.md)** - Get up and running in minutes
- **[Configuration](configuration.md)** - API client setup and options

### Core Features
- **[Evaluation API](api/evaluation.md)** - Evaluate content across RAIL dimensions
- **[Generation API](api/generation.md)** - Generate responsible AI content
- **[Compliance API](api/compliance.md)** - Check regulatory compliance
- **[Utilities](api/utilities.md)** - Credits, usage tracking, and health checks

### Guides & Tutorials
- **[Examples & Use Cases](examples.md)** - Real-world examples
- **[Content Moderation](guides/content-moderation.md)** - Moderate user-generated content
- **[RAG Evaluation](guides/rag-evaluation.md)** - Detect hallucinations in RAG systems
- **[Compliance Checking](guides/compliance.md)** - Automate compliance validation
- **[Batch Processing](guides/batch-processing.md)** - Process multiple items efficiently

### Reference
- **[API Reference](api-reference.md)** - Complete API documentation
- **[Error Handling](error-handling.md)** - Exception types and handling
- **[Response Structure](response-structure.md)** - Understanding API responses
- **[Best Practices](best-practices.md)** - Tips for optimal usage

### Additional Resources
- **[FAQ](faq.md)** - Frequently asked questions
- **[Changelog](changelog.md)** - Version history
- **[Migration Guide](migration.md)** - Upgrading between versions
- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions

---

## 🎓 Common Use Cases

### Content Moderation
Evaluate user-generated content for safety and appropriateness:

```python
result = client.evaluation.dimension(
    content="User comment here",
    dimension="safety"
)

if result['result']['score'] < 7.0:
    print("Content flagged for review")
```

**[→ Full Content Moderation Guide](guides/content-moderation.md)**

### GDPR Compliance
Check if your AI system complies with GDPR requirements:

```python
result = client.compliance.gdpr(
    content="We collect user data for analytics",
    context={"data_type": "personal", "region": "EU"}
)

print(f"Compliance Score: {result.compliance_score}")
```

**[→ Full Compliance Guide](guides/compliance.md)**

### RAG Hallucination Detection
Detect hallucinations in retrieval-augmented generation:

```python
result = client.evaluation.rag_evaluate(
    query="What is the capital of France?",
    response="The capital of France is Paris.",
    context_chunks=[{"content": "Paris is the capital of France."}]
)

print(f"Hallucination Score: {result['result']['rag_metrics']['hallucination_score']}")
```

**[→ Full RAG Evaluation Guide](guides/rag-evaluation.md)**

---

## 🔧 Key Features

- ✅ **8 RAIL Dimensions**: Comprehensive evaluation framework
- ✅ **Multiple Evaluation Modes**: Basic, dimension-specific, custom, weighted, detailed, advanced, batch
- ✅ **AI Generation**: RAG chat, reprompting, protected generation
- ✅ **Compliance Checks**: GDPR, HIPAA, CCPA, EU AI Act
- ✅ **Batch Processing**: Evaluate up to 100 items per request
- ✅ **Type-Safe**: Full typing support for better IDE experience
- ✅ **Auto-Retry**: Built-in error handling and retries
- ✅ **Rich Metadata**: Request IDs, credits consumed, processing times

---

## 🆘 Getting Help

- **Documentation**: You're reading it! 📖
- **GitHub Issues**: [Report bugs or request features](https://github.com/Responsible-AI-Labs/rail-score/issues)
- **Email Support**: [support@responsibleailabs.ai](mailto:support@responsibleailabs.ai)
- **API Status**: Check [status.responsibleailabs.ai](https://status.responsibleailabs.ai)

---

## 🤝 Contributing

We welcome contributions! See our [Contributing Guide](https://github.com/Responsible-AI-Labs/rail-score/blob/main/CONTRIBUTING.md) for details.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Responsible-AI-Labs/rail-score/blob/main/LICENSE) file for details.

---

## 🔗 Quick Links

- [PyPI Package](https://pypi.org/project/rail-score/)
- [GitHub Repository](https://github.com/Responsible-AI-Labs/rail-score)
- [RAIL Score Website](https://responsibleailabs.ai)
- [Research Paper](https://arxiv.org/abs/2505.00204)
- [API Dashboard](https://responsibleailabs.ai/dashboard)

---

**Ready to get started? [→ Install the SDK](installation.md)**
