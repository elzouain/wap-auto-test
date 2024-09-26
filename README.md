# WAP Automation Example

A test project using Python, Selenium WebDriver and the Page Object Model design pattern.

# Scenarios:
1. Go to [Twitch.com](<https://www.twitch.com>) in <b>mobile view</b>, perform a search, scroll down a couple of times, 
click on one result, wait for the page to load, dismiss popup, and take a screenshot.

# Requirements

* Python 3.10.12
* pip 23.2.1
* selenium 4.25.0
* pytest 8.3.3
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)
* Full list of dependencies in `requirements.txt`

# Installation

1. Clone the repository `git clone https://github.com/elzouain/wap-auto-test.git`
2. Change to this project's root directory `cd wap-auto-test`
3. Run `python3 -m venv .venv` to create the `./.venv/` directory. 
If you get an error, use `sudo apt install python3.10-venv` and try again.
4. Change the executable permissions of the virtual environment activation script `sudo chmod 777 ./.venv/bin/activate`
5. Activate the virtual environment `source ./.venv/bin/activate` (UNIX systems). 
You should see `(.venv)` next to the terminal prompt.
6. Within the virtual environment, install the necessary dependencies `pip install -r requirements.txt`
7. To exit the virtual environment run `deactivate`.

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
