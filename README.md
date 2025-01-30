![Python](https://img.shields.io/badge/python-3.10-blue.svg)

References: https://github.com/keraattin/EmailAnalyzer

# Email Analyzer Tutorial

## Steps to Use the Email Analyzer

### 1. Clone this Repository

### 2. Add VirusTotal API Key in Email_Scanner.py

![image](https://github.com/user-attachments/assets/6d5b5aae-55ab-4ca1-b048-cb1d2217e574)

- You can obtain this for free on their official website by registering (if you don't have an account).
- Free version accounts may have limited access, so be sure to calculate your API usage to avoid going beyond its limit.

### 3. Extract Emails from inbox into .eml format

![image](https://github.com/user-attachments/assets/002b5ca1-cb05-4e2a-a76c-98f7515d3fc8)
![image](https://github.com/user-attachments/assets/1cd60c80-380c-4bff-9335-dda6cec29fdf)

- Run Command: `python Email_Visualize.py`
- It will prompt you to give your email address and password. For the password, you need to obtain a key from the app password generator in your Google account. Refer to this [link](https://support.google.com/accounts/answer/185833?hl=en) for guidance on how to obtain such a password.
- By running this command, it will generate a folder named 'emails', where it will extract all the emails from your inbox into .eml files.
- It also highlights the most frequent keywords that are used in email titles, this can be used to quickly determine whether most of the emails are spam based on their title

### 4. Scan Your Selected Emails

![image](https://github.com/user-attachments/assets/8de29161-463e-425b-bbd8-62705f28fc43)
![image](https://github.com/user-attachments/assets/5b3fa6d1-745f-4734-9f9f-bff612a33f8d)

- Find your desired email in the 'emails' folder and remember its name.
- The URL of the result will be written into an excel files, the overall score can be viewed from VirusTotal API site 
- Run this command: `python Email_Scanner.py -f ./emails/<selected email files name>`
  - This will upload your selected .eml files to the VirusTotal API Database. Ensure that you don't send any emails that might contain your personal information to avoid data leaks.
  - It will also create an Excel file named 'Email Analysis'. From here, you can view the scores evaluated by famous security vendors and verify the authenticity of the content of your emails.

