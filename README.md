# Google Drive to Telegram File Uploader

This Python script allows you to download files from Google Drive and upload them to Telegram. It uses the Google Drive API to fetch files and the Telegram Bot API to upload them.

**Note**: This script is still under construction. I am aware that it is not very user-friendly at the moment and am working on improving it.

---

## Table of Contents
1. [Features](#features)
2. [Tools](#tools)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [License](#license)
8. [Acknowledgments](#acknowledgments)

---

## Features
- **Google Drive Integration**: Downloads files from Google Drive using the Google Drive API.
- **Telegram Integration**: Uploads downloaded files to a Telegram chat using the Telegram Bot API.
- **Progress Tracking**: Displays download progress in real-time.

---

## Tools
- **Google Drive API**
- **Telegram Bot API**
- **Requests library**
  
---

## Prerequisites
Before running the script, ensure you have the following:

1. **Google Cloud Project**:
   - Enable the Google Drive API.
   - Create a service account and download the JSON credentials file.
   - Share the file in Google Drive with the service account's email.

2. **Telegram Bot**:
   - Start [@DtoTel_Bot](https://t.me/DtoTel_Bot) Telegram bot.

---

## Installation
1. **Clone this repository or download the script.**
2. **Install the required Python packages.**

   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client requests
   ```

---

## Configuration
1. **Google Drive API**
   * Enable the Google Drive API in your Google Cloud Console.
   * Create a service account and download the JSON credentials file.
   * Replace "JSON FILE PATH" in the script with the path to your JSON credentials file.
   * Share the file you want to download with the service account's email (found in the JSON file).
     
2. **Start the bot on Telegram by sending a message to @DtoTel_Bot.**
3. **Replace 'FILE NAME' in the script with the name of the file you want to download from Google Drive.**

---

## Usage
1. **Start the Telegram bot by sending a message to it.**
2. **Run the script.**
   
   ```bash
   python script.py
   ```
   
4. **The script will**
   * Fetch the chat ID from Telegram.
   * Search for the specified file in Google Drive.
   * Download the file.
   * Upload and send the file to the Telegram chat.
  
![alt text]((https://drive.google.com/file/d/1Nw6vi8H9veWGP_TqCyqXIIyrmYTNofjf/view?usp=sharing) "Preview")

---

## License
This project is open-source and available under the MIT License.

---

## Acknowledgments
* [Google Drive API Documentation](https://developers.google.com/drive/api/guides/about-sdk)
* [Telegram Bot API Documentation](https://core.telegram.org/bots/api)



<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/chethiya-ravindranath-64a1b5329" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="chethiya-ravindranath-64a1b5329" height="30" width="40" /></a>
<a href="https://instagram.com/ch3thiya" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="ch3thiya" height="30" width="40" /></a>
</p>
