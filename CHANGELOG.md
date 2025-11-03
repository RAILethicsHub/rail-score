# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Additional compliance frameworks (SOC 2, ISO 27001)
- Async/await support for concurrent evaluations
- Webhook support for batch processing notifications
- CLI tool for command-line evaluations

---

## [1.0.1] - 2025-11-04

### Changed
- Enhanced README with badges and better structure
- Improved PyPI package metadata and keywords
- Updated documentation with comprehensive guides

### Added
- Complete installation guide with platform-specific instructions
- Quick start tutorial with step-by-step examples
- Comprehensive API reference documentation
- Real-world examples and use cases
- Interactive Jupyter notebooks

### Fixed
- Minor documentation formatting improvements

---

## [1.0.0] - 2025-11-04

### Initial Stable Release

This is the first stable release of the RAIL Score Python SDK, providing production-ready tools for evaluating and generating responsible AI content.

#### Evaluation API
- **Basic Evaluation**: Comprehensive evaluation across all 8 RAIL dimensions
- **Dimension-Specific Evaluation**: Focus on individual dimensions (privacy, safety, fairness, etc.)
- **Custom Evaluation**: Evaluate specific dimensions with custom weights
- **Weighted Evaluation**: Apply custom importance weights to dimensions
- **Detailed Evaluation**: Get in-depth breakdown with strengths, weaknesses, and improvement suggestions
- **Advanced Evaluation**: Ensemble-based evaluation with higher confidence scores (0.90+)
- **Batch Evaluation**: Process up to 100 items per request efficiently
- **RAG Evaluation**: Evaluate RAG responses for hallucinations and grounding quality

#### Generation API
- **RAG Chat**: Generate context-grounded responses with configurable models
- **Reprompting**: Get AI-powered suggestions to improve content scores
- **Protected Generation**: Generate content with safety filters and minimum RAIL score thresholds

#### Compliance API
- **GDPR Compliance**: Check compliance with EU General Data Protection Regulation
- **CCPA Compliance**: Validate against California Consumer Privacy Act requirements
- **HIPAA Compliance**: Assess healthcare data handling compliance
- **EU AI Act Compliance**: Evaluate against EU Artificial Intelligence Act standards

#### Utility Methods
- **Credit Management**: Check remaining credits and monthly limits
- **Usage Tracking**: View detailed usage history with filtering options
- **Health Check**: Verify API status and version information

#### Core Features
- Full typing support with structured dataclasses
- Comprehensive error handling with custom exceptions:
  - `AuthenticationError`
  - `InsufficientCreditsError`
  - `ValidationError`
  - `RateLimitError`
  - `PlanUpgradeRequired`
- Automatic retry logic with exponential backoff
- Detailed metadata in all responses (request ID, credits consumed, processing time)
- Support for Python 3.8, 3.9, 3.10, 3.11, 3.12

#### Documentation
- Complete README with usage examples
- Comprehensive API reference documentation
- Installation guide with platform-specific instructions
- Quick start guide
- Real-world examples and use cases
- Jupyter notebooks for interactive learning
- Type hints for IDE autocomplete support

### Technical Details
- **Dependencies**: requests >= 2.28.0
- **Python Support**: 3.8, 3.9, 3.10, 3.11, 3.12
- **License**: MIT

---

## How to Update This Changelog

When releasing a new version, move items from `[Unreleased]` to a new version section with the release date.

### Categories
- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` in case of vulnerabilities

### Example Entry

```markdown
## [1.1.0] - 2025-XX-XX

### Added
- New feature X
- Support for Y

### Fixed
- Bug in Z component
- Performance issue in batch processing

### Changed
- Improved error messages
- Updated dependencies
```

---

[Unreleased]: https://github.com/Responsible-AI-Labs/rail-score/compare/v1.0.1...HEAD
[1.0.1]: https://github.com/Responsible-AI-Labs/rail-score/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/Responsible-AI-Labs/rail-score/releases/tag/v1.0.0