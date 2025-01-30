from google.oauth2 import service_account
from googleapiclient.discovery import build
import requests

# Google Drive API setup
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
creds = service_account.Credentials.from_service_account_file("JSON FILE PATH",
                                                              scopes=SCOPES)
service = build('drive', 'v3', credentials=creds)

# Name of the file you want to download
file_name = 'FILE NAME'

bot_token = '7745321944:AAEkMDhDVJfWnY_4f3P31zaRrpcLQ3lCqPs'

input("Start the bot @DtoTel_Bot on Telegram. Press any key after starting the bot. ")

def get_chat_id():
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url).json()

    if response.get("ok"):
        messages = response.get("result", [])
        if messages:
            latest_message = messages[-1]["message"]["chat"]
            chat_id = latest_message["id"]
            username = latest_message.get("username", "No username")

            print(f"User: {username} | Chat ID: {chat_id}")
            return chat_id
    print("No messages found. Make sure someone has started the bot.")
    return None

chat_id = get_chat_id()
if not chat_id:
    exit("Error: Could not retrieve chat ID. Ensure the bot has received at least one message.")


# Search for the file by name
results = service.files().list(q=f"name='{file_name}' and trashed=false", fields='files(id, name, mimeType)').execute()
items = results.get('files', [])

if not items:
    print(f'File "{file_name}" not found in your Google Drive.')
else:
    file = items[0]
    file_id = file['id']

    # Get the file's download URL
    download_url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media"
    headers = {'Authorization': f'Bearer {creds.token}'}

    response = requests.get(download_url, headers=headers, stream=True)

    if response.status_code == 200:
        file_size = int(response.headers.get('content-length', 0))
        print(f"Downloading {file['name']} ({file_size} bytes) from Google Drive...")

        # Save to temporary file
        temp_file_path = f"./{file_name}"
        with open(temp_file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"Download complete: {temp_file_path}")

        # Upload to Telegram
        with open(temp_file_path, 'rb') as f:
            url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
            data = {'chat_id': chat_id}
            files = {'document': f}

            upload_response = requests.post(url, data=data, files=files)

            if upload_response.status_code == 200:
                print(f"File '{file_name}' uploaded successfully to Telegram.")
            else:
                print(f"Failed to upload file '{file_name}' to Telegram. Status code: {upload_response.status_code}")
                print("Response:", upload_response.json())  # Print detailed error message from Telegram

    else:
        print(f'Failed to download file "{file_name}" from Google Drive. Status code:', response.status_code)