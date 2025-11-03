# Installation Guide

This guide covers everything you need to install and set up the RAIL Score Python SDK.

---

## Requirements

- **Python**: 3.8 or higher
- **pip**: Latest version recommended
- **Dependencies**: `requests >= 2.28.0` (automatically installed)

---

## Installation Methods

### Method 1: Install from PyPI (Recommended)

The simplest way to install the RAIL Score SDK:

```bash
pip install rail-score
```

### Method 2: Install with Optional Dependencies

For development or additional features:

```bash
# Install with development tools
pip install rail-score[dev]

# Install with documentation tools
pip install rail-score[docs]

# Install everything
pip install rail-score[all]
```

### Method 3: Install from Source

For the latest development version:

```bash
# Clone the repository
git clone https://github.com/Responsible-AI-Labs/rail-score.git
cd rail-score

# Install in editable mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### Method 4: Install Specific Version

To install a specific version:

```bash
# Install specific version
pip install rail-score==1.0.0

# Install minimum version
pip install "rail-score>=1.0.0"
```

---

## Virtual Environment Setup (Recommended)

We strongly recommend using a virtual environment to avoid dependency conflicts.

### Using venv (Python 3.3+)

```bash
# Create virtual environment
python -m venv rail-env

# Activate (Linux/Mac)
source rail-env/bin/activate

# Activate (Windows)
rail-env\Scripts\activate

# Install rail-score
pip install rail-score
```

### Using conda

```bash
# Create conda environment
conda create -n rail-env python=3.10

# Activate environment
conda activate rail-env

# Install rail-score
pip install rail-score
```

### Using virtualenv

```bash
# Install virtualenv if needed
pip install virtualenv

# Create virtual environment
virtualenv rail-env

# Activate (Linux/Mac)
source rail-env/bin/activate

# Activate (Windows)
rail-env\Scripts\activate

# Install rail-score
pip install rail-score
```

---

## Verify Installation

After installation, verify everything works:

```python
import rail_score

# Check version
print(rail_score.__version__)

# Import main class
from rail_score import RailScore

# Verify it can be instantiated
client = RailScore(api_key="test-key")
print("Installation successful!")
```

Or from the command line:

```bash
python -c "import rail_score; print(rail_score.__version__)"
```

---

## Getting an API Key

To use the RAIL Score SDK, you need an API key:

1. **Visit**: [https://responsibleailabs.ai](https://responsibleailabs.ai)
2. **Sign up**: Create a free account
3. **Get API Key**: Navigate to your dashboard and copy your API key
4. **Set Environment Variable** (optional but recommended):

```bash
# Linux/Mac
export RAIL_API_KEY="your-api-key-here"

# Windows (Command Prompt)
set RAIL_API_KEY=your-api-key-here

# Windows (PowerShell)
$env:RAIL_API_KEY="your-api-key-here"
```

Then use in Python:

```python
import os
from rail_score import RailScore

client = RailScore(api_key=os.getenv("RAIL_API_KEY"))
```

---

## Configuration File (Optional)

You can create a configuration file for convenience:

**~/.rail_score/config.json**:
```json
{
  "api_key": "your-api-key-here",
  "base_url": "https://api.responsibleailabs.ai",
  "timeout": 60
}
```

Then load it in your code:

```python
import json
from pathlib import Path
from rail_score import RailScore

config_path = Path.home() / ".rail_score" / "config.json"
config = json.loads(config_path.read_text())

client = RailScore(**config)
```

---

## Upgrading

### Upgrade to Latest Version

```bash
pip install --upgrade rail-score
```

### Upgrade to Specific Version

```bash
pip install --upgrade rail-score==1.2.0
```

### Check Current Version

```bash
pip show rail-score
```

---

## Uninstalling

If you need to uninstall:

```bash
pip uninstall rail-score
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'rail_score'`

**Solution**: Make sure you've activated your virtual environment and installed the package:

```bash
pip install rail-score
```

### Issue: `ImportError: cannot import name 'RailScore'`

**Solution**: You might have an older or corrupted installation:

```bash
pip uninstall rail-score
pip install rail-score
```

### Issue: Version conflicts with other packages

**Solution**: Use a virtual environment or upgrade dependencies:

```bash
pip install --upgrade rail-score requests
```

### Issue: SSL Certificate errors

**Solution**: Update your SSL certificates or use a specific version:

```bash
# Update certifi
pip install --upgrade certifi

# Or ignore SSL (not recommended for production)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org rail-score
```

### Issue: Permission denied during installation

**Solution**: Use `--user` flag or run with elevated privileges:

```bash
# Install for current user only
pip install --user rail-score

# Or use sudo (Linux/Mac)
sudo pip install rail-score
```

### Issue: Slow installation or timeouts

**Solution**: Use a different PyPI mirror:

```bash
# Use a different index
pip install -i https://pypi.org/simple rail-score

# Increase timeout
pip install --timeout 120 rail-score
```

---

## Platform-Specific Notes

### Windows

If you encounter issues with long paths, enable long path support:

```bash
# Run as Administrator in PowerShell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

### macOS

If you have multiple Python versions, specify Python 3:

```bash
python3 -m pip install rail-score
```

### Linux

Some distributions may need additional packages:

```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install python3-pip python3-venv

# RHEL/CentOS/Fedora
sudo yum install python3-pip

# Then install rail-score
pip3 install rail-score
```

---

## Docker Installation

Use RAIL Score in Docker:

**Dockerfile**:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install rail-score
RUN pip install rail-score

# Copy your application code
COPY . .

CMD ["python", "your_app.py"]
```

Build and run:

```bash
docker build -t my-rail-app .
docker run -e RAIL_API_KEY="your-key" my-rail-app
```

---

## CI/CD Integration

### GitHub Actions

```yaml
name: Test with RAIL Score

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install rail-score
      - name: Run tests
        env:
          RAIL_API_KEY: ${{ secrets.RAIL_API_KEY }}
        run: |
          python test_script.py
```

### GitLab CI

```yaml
test:
  image: python:3.10
  script:
    - pip install rail-score
    - python test_script.py
  variables:
    RAIL_API_KEY: $RAIL_API_KEY
```

---

## Next Steps

Now that you have RAIL Score installed:

1. **[Quick Start Guide](quickstart.md)** - Learn the basics
2. **[Configuration](configuration.md)** - Set up the client
3. **[Examples](examples.md)** - See real-world usage

---

## Getting Help

If you encounter installation issues:

- Check the [Troubleshooting Guide](troubleshooting.md)
- Search [GitHub Issues](https://github.com/Responsible-AI-Labs/rail-score/issues)
- Contact [support@responsibleailabs.ai](mailto:support@responsibleailabs.ai)
