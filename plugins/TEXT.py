

# Here is Your Drive Folder Name You can Replace it with Your Desire name(Optional)
drive_folder_name = "Mitsuha'sDrive"


# Enter Your Mega email And Pass (Required)
#MEGA_EMAIL = "example@example.com"
#MEGA_PASSWORD = "example@example.com"


START = " Hello,<b> {} </b>.\n \nI'm a Drive Uploader Bot. I can upload files to your Google Drive remotely. \n \nTo get started click on /auth and follow the provided instructions. "

HELP = """   <b>Authorise Bot: </b> \n
       Use <b> /auth </b>Command Generate
       Your Google Drive Token And 
       Send It To Bot  
<b> To change Google Drive Account :</b> \n
        Use /revoke command to get new Token from different Drive Account.          
        """
PROCESSING = "Verifying if Download Link is Valid...!!"
DOWN_TWO = True
DOWNLOAD = "Downloading Started ..."
DOWN_COMPLETE = "Downloading complete !!"
NOT_AUTH = "You Are Not Authorised To Use this Bot \n\n Please Authorise Me Using /auth  \n"
REVOKE_FAIL = "You Are Already UnAuthorised \n. Please Use /auth To Authorise \n"
AUTH_SUCC = "Authorised Successfully  !! \n\n Now Send me A direct Link :)"
ALREADY_AUTH = "You Are Already Authorised ! \n\n Wanna Change Drive Account? \n\n Use /revoke .\n "
AUTH_URL = '<a href ="{}"><b>Get Auth Token</b></a> \n\nClick on the above link to generate Auth Token And send it here.'
UPLOADING = "Download Complete !! \n Uploading to Google Drive"
REVOKE_TOK = " Your Token was Revoked Successfully !! \n\n Use /auth To Re-Authorise Your Drive Account. "
# DOWN_PATH = "Downloads\\" #windows path
DOWN_PATH = "Downloads/"  # Linux path
DOWNLOAD_URL = "Your File was Uploaded Successfully \n\n <b>Filename</b> : {} \n\n <b> Size</b> : {} MB \n\n <b>Drive Link :</b> {}"
AUTH_ERROR = "AUTH Error !! Please  Send Me a  valid Token or Re-Authorise Me  \n"
OPENLOAD = True
DROPBOX = True
MEGA = True
