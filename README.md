# Dynamic Content Handling ⏳

Automate dynamic/AJAX content using **explicit waits** in Selenium. Tested on [The Internet - Dynamic Loading](https://the-internet.herokuapp.com/dynamic_loading).

## Technologies Used
- Python 3
- Selenium WebDriver
- pytest
- Explicit Waits (`WebDriverWait`)

## Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/dynamic-content.git
   cd dynamic-content
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Update ChromeDriver** (if needed) in `conftest.py`.

## Run Tests
```bash
pytest tests/test_dynamic.py -v
```

## Project Structure
```
dynamic-content/
├── tests/
│   └── test_dynamic.py      # Test cases for dynamic content
├── pages/
│   └── dynamic_page.py      # Page class for dynamic interactions
├── utils/
│   └── config.py            # URL configurations
└── conftest.py              # Pytest fixtures
```

## Example Test Run
```bash
========================= test session starts =========================
collected 2 items

tests/test_dynamic.py::test_dynamic_loading PASSED               [100%]
========================== 2 passed in 12.34s =========================
```

## Key Features
- Handles dynamic content loading (hidden/rendered elements).
- Uses `WebDriverWait` for synchronization.
- Tests multiple dynamic loading scenarios.
