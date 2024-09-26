# WAP Automation Example

A test project using Python, Selenium WebDriver and the Page Object Model design pattern.

# Scenarios:
1. Go to [Twitch.com](<https://www.twitch.com>) in <b>mobile view</b>, perform a search, scroll a couple of times, and take a screenshot once the page loads.

# Requirements

* Python 3.10.12
* pip 23.2.1
* selenium 4.25.0
* pytest 8.3.3
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)
* Full list of dependencies in `requirements.txt`

# Installation

1. Go to this project's root directory.
2. Install dependencies `pip install -r requirements.txt`
3. Activate the virtual environment `source ./.venv/bin/activate` (UNIX systems).
4. Optional: You might need to change executable permissions `sudo chmod 777 ./.venv/bin/activate` and try step 3 again.
5. Run `deactivate` to exit the virtual environment.

# Test Execution

1. Open a terminal
2. From the project root directory run `pytest -v --html=results/report.html`

# Screenshots

Screenshots will be saved as `screenshots/<test_name>.png`.

# Results

To check the report, open the `results/report.html` file once the execution has finished.

# Configuration

Tests are configured to run with <b>Chrome</b>.<br> 
Preferences can be changed in `conf/config.yaml`.
