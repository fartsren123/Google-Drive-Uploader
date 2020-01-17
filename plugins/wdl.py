import os
import subprocess
import wget

#wget.download(url)

def wget_dl(url):
        try:
            print("Downloading Started")

           filename = os.path.basename(url)
           output = subprocess.check_output("wget '--output-document' '{}' '{}' ".format(filename , url), stderr=subprocess.STDOUT, shell=True)
       
            print("Downloading Complete",filename)
            return filename
        except Exception as e:
            print("DOWNLAOD ERROR :",e)
           
            return "error",filename 
        
# wget_dl(url)
