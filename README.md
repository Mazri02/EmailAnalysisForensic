![Python](https://img.shields.io/badge/python-3.10-blue.svg)

References : https://github.com/keraattin/EmailAnalyzer

# Email Analyzer Tutorial

## Steps to Use the Email Analyzer

### 1. Clone this Repository

### 2. Add VirusTotal API Key in Email_Scanner.py
- You can obtain this for free on their official website by registering (if you don't have an account).
- Free version accounts may have limited access, so be sure to calculate your API usage to avoid going beyond its limit.

### 3. Extract Emails from inbox into .eml format
- Run Command: `python Email_Visualize.py`
- It will prompt you to give your email address and password. For the password, you need to obtain a key from the app password generator in your Google account. Refer to this [link](https://support.google.com/accounts/answer/185833?hl=en) for guidance on how to obtain such a password.
- By running this command, it will generate a folder named 'emails', where it will extract all the emails from your inbox into .eml files.

### 4. Scan Your Selected Emails
- Find your desired email in the 'emails' folder and remember its name.
- Run this command: `python Email_Scanner.py -f ./emails/<selected email files name>`
  - This will upload your selected .eml files to the VirusTotal API Database. Ensure that you don't send any emails that might contain your personal information to avoid data leaks.
  - It will also create an Excel file named 'Email Analysis'. From here, you can view the scores evaluated by famous security vendors and verify the authenticity of the content of your emails.

