# entrata_web_automation
- web_ui_pytest.py contains python and pytest based web automation script
- requirements.txt contains all the required libraries for automation script
- After 'git clone' action install all the required libraries from requirements.txt using
  'pip install -r requirements.txt' command
- You can use "chromedriver-win64\chromedriver.exe" file in automation script as a chromedriver
- In web_ui_pytest.py, below test case are defined:
    - test_home_page_title : Test to check the title of the home page
    - test_sign_in_button_text : Test to validate the 'Sign In' button text
    - test_linkedin_redirect : Test to validate LinkedIn redirection page
- Run the web_ui_pytest.py using 'python -m pytest -s web_ui_pytest.py' command

