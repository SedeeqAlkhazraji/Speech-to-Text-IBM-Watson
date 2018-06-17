# Speech-to-Text-IBM-Watson
Speech to Text using IBM Watson API. 

To run this code, you will need a `username`, `password`, and `url`. To get your service credentials, follow these steps:
 1. Log in to IBM Cloud at https://console.bluemix.net.

 1. Create an instance of the service:
     1. In the IBM Cloud **Catalog**, select the Speech to Text service.
     1. Click **Create**.

 1. Copy your credentials:
     1. On the left side of the page, click **Service Credentials** to view your service credentials.
     1. Copy `username`, `password`, and `url` from these service credentials.
     
 **Input**
 Save your audio (Speech) files in the "1_Input_flca_Files" directory.
 
 **Running**
Run the file **Convert.py** using python 2.7 or later

**Output**
The final formatted TEXT will save as ".SRT" files on "2_Output_Files" directory.
NOTE: "2_Output_Files" will contain ".text" files as temporary files during the conversion process. 

