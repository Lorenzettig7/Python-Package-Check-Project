Python Package Compliance Checker

This project verifies Python applications for compliance with an approved package list.

Given:
-A list of approved packages- ApprovedList.txt
-Multiple application folders each containing a requirements.txt

Code:
-Parses each application's required packages
-Compares them against the approved list 
-Classifies each package as Approved or  Unapproved
-Outputs the results into a consolidated report output.txt

Setup Instructions
This project checks for unauthorized or unexpected Python packages in a given environment. It can be used for basic integrity checks or lightweight security audits.
* Clone the repository
 git clone https://github.com/Lorenzettig7/Python-Package-Check-Project.git
 cd Python-Package-Check-Project 
* Install dependencies (if a requirements.txt file is included)
   pip install -r requirements.txt 
* Run the script
    python package_check.py 
* What it does
    * Lists all currently installed Python packages
    * Optionally compares them against a known-good list
    * Flags unexpected or unauthorized packages



