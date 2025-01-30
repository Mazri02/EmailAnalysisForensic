import imaplib
import email
import getpass
import pandas as pd
from datetime import datetime
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import time

# Initialize lists
date_list = []
from_list = []
subject_text = []

# Desired Email address is entered as a string
# Then login to the email server
username = input("Enter your email address: ")
password = getpass.getpass("Enter password: ")
mail = imaplib.IMAP4_SSL('imap.gmail.com')

mail.login(username, password)

# Checking the mailboxes and selecting one
print(mail.list())
mail.select("INBOX")

# Searching for emails in the mailbox
result, numbers = mail.uid('search', None, "ALL")
uids = numbers[0].split()
uids = [id.decode("utf-8") for id in uids]
uids = uids[-1:-101:-1]

# Creating a directory to store the emails
output_dir = 'emails'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Fetching and saving the emails
for uid in uids:
    retry = 0
    while retry < 3:  # Retry up to 3 times on failure
        try:
            result, message_data = mail.uid('fetch', uid.encode('utf-8'), '(RFC822)')
            if result != 'OK': 
                raise imaplib.IMAP4.error('Failed to fetch email')
            raw_email = message_data[0][1]
            email_message = email.message_from_bytes(raw_email)
            
            # Save the email as an .eml file
            eml_filename = os.path.join(output_dir, f'email_{uid}.eml')
            with open(eml_filename, 'wb') as eml_file:
                eml_file.write(raw_email)

            # Process the email for analytics
            decode = email.header.decode_header(email_message['Subject'])[0]
            if isinstance(decode[0], bytes):
                decoded = decode[0].decode()
                subject_text.append(decoded)
            else:
                subject_text.append(decode[0])
            date_list.append(email_message.get('date'))
            fromlist = email_message.get('From')
            fromlist = fromlist.split("<")[0].replace('"', '')
            from_list.append(fromlist)
            break  # Exit retry loop on success
        except imaplib.IMAP4.abort:
            retry += 1
            print(f"Connection error, retrying... ({retry})")
            time.sleep(2)  # Wait before retrying
            mail.login(username, password)
            mail.select("INBOX")

print(f"Emails have been successfully extracted to the '{output_dir}' directory.")

# Convert date_list to datetime
date_list = pd.to_datetime(date_list, errors='coerce', utc=True).tz_convert('Asia/Kuala_Lumpur')

# Create DataFrame
df = pd.DataFrame(data={'Date': date_list, 'Sender': from_list, 'Subject': subject_text})
print(df.head())

# DATA VISUALIZATION
# Using Datetime to create new values
# SinceMid is the number of hours after midnight
FMT = '%H:%M:%S'

# Ensure the 'Date' column is in the correct format and ignore NaT values
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Time'] = df['Date'].dropna().apply(lambda x: x.strftime(FMT))

# Filter out NaN values before applying the function
df['SinceMid'] = df['Time'].apply(lambda x: (datetime.strptime(x, FMT) - datetime.strptime("00:00:00", FMT)).seconds / 60 / 60 if pd.notna(x) else None)

print(df.head())

# Using Wordcloud to see the most used words in the email subjects
text = ""
for item in df["Subject"]:
    if isinstance(item, str):
        text += " " + item
text = text.replace("'", "").replace(",", "").replace('"', '')

# Create the wordcloud object
wordcloud = WordCloud(width=800, height=800, background_color="white")

# Display the generated image
wordcloud.generate(text)
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.title("Most Used Subject Words", fontsize=20, ha="center", pad=20)
plt.show()

# Distribution plot for 'SinceMid'
sns.histplot(df["SinceMid"], bins=20)
plt.title("Hours since midnight")
plt.show()
