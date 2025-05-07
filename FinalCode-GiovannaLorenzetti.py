import os
import fnmatch
import sys
import pandas
from fuzzywuzzy import process

approved_packages_file_path = r"/Users/giovannalorenzetti/Desktop/FinalCodeFolder/ApprovedList.txt"
applications_folder_path = "/Users/giovannalorenzetti/Desktop/FinalCodeFolder/applications/"
output_file_path = "/Users/giovannalorenzetti/Desktop/FinalCodeFolder/output.txt"

def GetApprovedPackages(file_paths):
    all_lines = []
    with open(file_paths, 'r') as file:
        while True:
            lines = file.readlines()
            if not lines:
                break
            lines = [line.strip() for line in lines]
            all_lines.extend(lines)
    df = pandas.DataFrame(all_lines)
    list_data = df.values.tolist()
    NewListData = [val for row in list_data for val in row]
    return NewListData

def ReadRequirements(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def CheckPackages(package_list, requirements):
    approved = []
    unapproved = []
    for requirement in requirements:
        similar_matches = process.extractBests(requirement.lower(), package_list, score_cutoff=100)
        exact_matches = [match for match in similar_matches if match[0].lower() == requirement.lower()]
        if exact_matches:
            approved.append(requirement)
        else:
            unapproved.append(requirement)
    return approved, unapproved

def RetrieveReqFile(folder, app_names):
    result = {}
    for app_name in app_names:
        app_folder = os.path.join(folder, app_name)
        for foldername, subfolders, filenames in os.walk(app_folder):
            for filename in filenames:
                if filename == 'requirements.txt':
                    result[app_name] = os.path.join(foldername, filename)
    return result

if __name__ == "__main__":
    arguments = sys.argv[1:]
    apps = [arg for arg in arguments]
    package_list = GetApprovedPackages(approved_packages_file_path)
    requirements_paths = RetrieveReqFile(applications_folder_path, apps)
    req_apps = []
    with open(output_file_path, "w") as output_file:
        for app, req_file_path in requirements_paths.items():
            if os.path.exists(req_file_path):
                requirements = ReadRequirements(req_file_path)
                approved, unapproved = CheckPackages(package_list, requirements)
                req_apps.append(app)
                output_file.write(f"***** Application Name: {app} *****\n\n")
                output_file.write("Approved Packages:\n")
                for package in approved:
                    output_file.write(package + "\n")

                output_file.write("\nUnapproved Packages:\n")
                for package in unapproved:
                    output_file.write(package + "\n")
                output_file.write("\n\n")
    
    with open(output_file_path, "a") as output_file:
        apps_list = [s_app for s_app in apps if s_app not in req_apps]
        if apps_list:
            output_file.write(f"\nNo requirements.txt file Apps: {','.join(apps_list)}\n")

    print(f"Output written to {output_file_path}")

