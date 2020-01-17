import os
import subprocess

def wget_dl(url):
        try:
            print("Downloading Started")
            # i was facing some problem in filename That's Why i did this ,
            #  i will fix it later :(

            filename = os.path.basename(url)
            output = subprocess.check_output("wget '--output-document' '{}' '{}' ".format(filename , url), stderr=subprocess.STDOUT, shell=True)
#

def bar_custom(current, total, width=80):
    print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
#wget.download('http://download.geonames.org/export/zip/US.zip', bar=bar_custom)

#          
            print("Downloading Complete",filename)
            return filename
        except Exception as e:
            print("DOWNLAOD ERROR :",e)
           
            return "error",filename
        
# wget_dl(url)
