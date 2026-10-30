"""
PYTHON API HANDLING AND FILE HANDLING NOTES
===========================================

Beginner-friendly reference notes with comments and examples.

Requirements:
    pip install requests

Topics:
    1. Text file handling
    2. CSV file handling
    3. JSON file handling
    4. API handling with requests
    5. Saving API data into JSON and CSV files

Run:
    python api_and_file_handling.py

IMPORTANT:
    - The file-handling examples create sample files in the same folder.
    - The API examples use JSONPlaceholder (https://jsonplaceholder.typicode.com).
    - JSONPlaceholder is a testing API. POST, PUT, PATCH, and DELETE responses
      are simulated; changes are not permanently saved on its server.
    - API examples need an internet connection.
"""

import csv
import json
import requests


# ============================================================
# 1. TEXT FILE HANDLING
# ============================================================

# "w" means write. It creates a file or replaces its old content.
with open("notes.txt", mode="w") as file:
    file.write("Learning Python file handling.\n")
    file.write("This is the second line.\n")

# "r" means read. It reads the content of an existing file.
with open("notes.txt", mode="r") as file:
    content = file.read()  # read() reads the complete file as one string.
    print("\nTEXT FILE CONTENT")
    print(content)

# readline() reads one line at a time.
with open("notes.txt", mode="r") as file:
    first_line = file.readline()
    print("FIRST LINE:", first_line)

# readlines() reads all lines and returns a list of strings.
with open("notes.txt", mode="r") as file:
    all_lines = file.readlines()
    print("ALL LINES:", all_lines)

# "a" means append. It adds new content at the end of the file.
# It does not erase the content already present.
with open("notes.txt", mode="a") as file:
    file.write("This line was added later.\n")

# Loop through a file one line at a time.
with open("notes.txt", mode="r") as file:
    print("\nREADING LINE BY LINE")
    for line in file:
        print(line.strip())  # strip() removes surrounding whitespace/newline.

# "x" creates a new file, but gives an error if the file already exists.
# Uncomment to try it with a filename that does not exist.
# with open("new_file.txt", mode="x") as file:
#     file.write("This is a new file.")

# Common file modes:
# "r" = read
# "w" = write (creates or overwrites)
# "a" = append (adds to the end)
# "x" = create a new file; error if it already exists
# "r+" = read and write an existing file


# ============================================================
# 2. CSV FILE HANDLING
# ============================================================

# CSV means Comma-Separated Values.
# Each row contains values separated by commas.

# Create a sample CSV file using DictWriter.
products = [
    {"Name": "Laptop", "Price": 100000, "Stock": 5},
    {"Name": "Mouse", "Price": 2000, "Stock": 10},
    {"Name": "Keyboard", "Price": 5000, "Stock": 4}
]

with open("products.csv", mode="w", newline="") as file:
    fields = ["Name", "Price", "Stock"]

    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()  # Writes the column headings.
    writer.writerows(products)  # Writes all dictionaries as rows.

# DictReader reads each CSV row as a dictionary.
with open("products.csv", mode="r", newline="") as file:
    reader = csv.DictReader(file)

    print("\nREADING CSV WITH DictReader")
    for row in reader:
        print(row)
        # Example row:
        # {'Name': 'Laptop', 'Price': '100000', 'Stock': '5'}
        # CSV values are read as strings, so convert numbers with int()/float().

# Calculate the total value of each product and store dictionaries in a list.
productDetails = []

with open("products.csv", mode="r", newline="") as file:
    for row in csv.DictReader(file):
        productDetails.append({
            "Name": row["Name"],
            "Total Value": int(row["Price"]) * int(row["Stock"])
        })

print("\nPRODUCT DETAILS")
print(productDetails)

# DictWriter uses dictionaries.
# writerow() writes one dictionary as one CSV row.
# writerows() writes multiple dictionaries.
# writeheader() writes the column names.

# csv.reader reads each row as a list instead of a dictionary.
with open("products.csv", mode="r", newline="") as file:
    reader = csv.reader(file)

    print("\nREADING CSV WITH reader")
    for row in reader:
        print(row)

# csv.writer writes rows using lists.
with open("marks.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Marks"])  # Writes one row.
    writer.writerow(["Ali", 85])
    writer.writerow(["Sara", 92])

# Read the CSV created above.
with open("marks.csv", mode="r", newline="") as file:
    reader = csv.reader(file)
    print("\nMARKS CSV")
    for row in reader:
        print(row)


# ============================================================
# 3. JSON FILE HANDLING
# ============================================================

# JSON stores data in a format similar to Python dictionaries and lists.

student = {
    "name": "Ali",
    "age": 20,
    "courses": ["Python", "AI"]
}

# json.dump() writes Python data into a JSON file.
with open("student.json", mode="w") as file:
    json.dump(student, file, indent=4)
    # indent=4 makes the JSON file easier to read.

# json.load() reads JSON from a file and converts it into Python data.
with open("student.json", mode="r") as file:
    loaded_student = json.load(file)

print("\nJSON DATA")
print(loaded_student)
print(loaded_student["name"])
print(loaded_student["courses"])

# json.dumps() converts Python data into a JSON-formatted string.
json_string = json.dumps(student, indent=4)
print("\nJSON STRING")
print(json_string)

# json.loads() converts a JSON-formatted string into Python data.
python_data = json.loads(json_string)
print("\nPYTHON DATA FROM JSON STRING")
print(python_data)

# Remember:
# json.dump(data, file)  -> writes Python data into a file.
# json.load(file)        -> reads JSON data from a file.
# json.dumps(data)       -> converts Python data into a JSON string.
# json.loads(string)     -> converts a JSON string into Python data.


# ============================================================
# 4. API HANDLING: BASIC GET REQUEST
# ============================================================

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_all_posts():
    # GET retrieves data from an API.
    url = BASE_URL + "/posts"

    try:
        response = requests.get(url, timeout=10)

        # status_code tells us the HTTP response status.
        print("\nGET ALL POSTS STATUS:", response.status_code)

        # raise_for_status() raises an error for unsuccessful HTTP responses.
        response.raise_for_status()

        # response.json() converts the API's JSON response into Python data.
        posts = response.json()

        print("NUMBER OF POSTS:", len(posts))

        # Each post is a dictionary, so we can access its keys.
        for post in posts[:5]:
            print("ID:", post["id"])
            print("TITLE:", post["title"])
            print()

        return posts

    except requests.exceptions.Timeout:
        print("The request took too long.")

    except requests.exceptions.ConnectionError:
        print("Could not connect to the API.")

    except requests.exceptions.HTTPError as error:
        print("HTTP error:", error)

    except requests.exceptions.RequestException as error:
        print("Request error:", error)

    except ValueError:
        print("The response could not be converted to JSON.")

    return None


# ============================================================
# 5. GET ONE RECORD USING AN ID
# ============================================================

def get_post_by_id(post_id):
    # /posts/1 retrieves the post whose ID is 1.
    url = BASE_URL + "/posts/" + str(post_id)

    try:
        response = requests.get(url, timeout=10)
        print("\nGET ONE POST STATUS:", response.status_code)

        response.raise_for_status()

        post = response.json()

        print("POST DETAILS")
        print("ID:", post["id"])
        print("USER ID:", post["userId"])
        print("TITLE:", post["title"])
        print("BODY:", post["body"])

        return post

    except requests.exceptions.RequestException as error:
        print("Request error:", error)

    except ValueError:
        print("The response could not be converted to JSON.")

    return None


# ============================================================
# 6. GET DATA USING QUERY PARAMETERS
# ============================================================

def get_posts_by_user(user_id):
    url = BASE_URL + "/posts"

    # params adds query parameters to the URL.
    # This request asks for posts belonging to userId 1.
    params = {"userId": user_id}

    try:
        response = requests.get(url, params=params, timeout=10)
        print("\nGET WITH PARAMS STATUS:", response.status_code)

        response.raise_for_status()

        posts = response.json()

        for post in posts:
            print(post["id"], post["title"])

        return posts

    except requests.exceptions.RequestException as error:
        print("Request error:", error)

    except ValueError:
        print("The response could not be converted to JSON.")

    return None


# ============================================================
# 7. POST: SEND / CREATE DATA
# ============================================================

def create_post():
    url = BASE_URL + "/posts"

    # This is the data we want to send to the API.
    data = {
        "title": "Learning Python APIs",
        "body": "This is a sample post.",
        "userId": 1
    }

    try:
        # json=data converts the dictionary into JSON for the request body.
        response = requests.post(url, json=data, timeout=10)

        print("\nPOST STATUS:", response.status_code)
        response.raise_for_status()

        result = response.json()
        print("CREATED POST RESPONSE:", result)

        return result

    except requests.exceptions.RequestException as error:
        print("Request error:", error)

    except ValueError:
        print("The response could not be converted to JSON.")

    return None


# ============================================================
# 8. PUT: REPLACE / UPDATE A RECORD
# ============================================================

def replace_post(post_id):
    url = BASE_URL + "/posts/" + str(post_id)

    # PUT sends the replacement data for the record.
    data = {
        "id": post_id,
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1
    }

    try:
        response = requests.put(url, json=data, timeout=10)

        print("\nPUT STATUS:", response.status_code)
        response.raise_for_status()

        result = response.json()
        print("UPDATED POST:", result)

        return result

    except requests.exceptions.RequestException as error:
        print("Request error:", error)

    except ValueError:
        print("The response could not be converted to JSON.")

    return None


# ============================================================
# 9. PATCH: UPDATE SELECTED FIELDS
# ============================================================

def update_post_title(post_id):
    url = BASE_URL + "/posts/" + str(post_id)

    # PATCH changes only the field(s) sent in this dictionary.
    data = {
        "title": "Only the title has been changed"
    }

    try:
        response = requests.patch(url, json=data, timeout=10)

        print("\nPATCH STATUS:", response.status_code)
        response.raise_for_status()

        result = response.json()
        print("PATCH RESPONSE:", result)

        return result

    except requests.exceptions.RequestException as error:
        print("Request error:", error)

    except ValueError:
        print("The response could not be converted to JSON.")

    return None


# ============================================================
# 10. DELETE: DELETE A RECORD
# ============================================================

def delete_post(post_id):
    url = BASE_URL + "/posts/" + str(post_id)

    try:
        response = requests.delete(url, timeout=10)

        print("\nDELETE STATUS:", response.status_code)
        response.raise_for_status()

        print("DELETE REQUEST COMPLETED.")
        return True

    except requests.exceptions.RequestException as error:
        print("Request error:", error)

    return False


# ============================================================
# 11. SAVE API DATA INTO A JSON FILE
# ============================================================

def save_posts_to_json(posts):
    if posts is None:
        print("No posts available to save.")
        return

    # json.dump() saves the list of dictionaries into a JSON file.
    with open("posts.json", mode="w") as file:
        json.dump(posts, file, indent=4)

    print("Posts saved to posts.json")


# ============================================================
# 12. SAVE API DATA INTO A CSV FILE
# ============================================================

def save_posts_to_csv(posts):
    if posts is None:
        print("No posts available to save.")
        return

    # Select only the fields we want in our CSV file.
    selected_posts = []

    for post in posts:
        selected_posts.append({
            "id": post["id"],
            "userId": post["userId"],
            "title": post["title"],
            "body": post["body"]
        })

    fields = ["id", "userId", "title", "body"]

    with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(selected_posts)

    print("Posts saved to posts.csv")


# ============================================================
# 13. RUN API EXAMPLES
# ============================================================

if __name__ == "__main__":
    # The file-handling examples above run when this file is executed.
    # Uncomment the API calls below to try them.

    # all_posts = get_all_posts()
    # save_posts_to_json(all_posts)
    # save_posts_to_csv(all_posts)

    # get_post_by_id(1)
    # get_posts_by_user(1)
    # create_post()
    # replace_post(1)
    # update_post_title(1)
    # delete_post(1)

    pass


# ============================================================
# QUICK REVISION
# ============================================================

"""
FILE HANDLING:
    open()
    read()
    readline()
    readlines()
    write()
    close()             # with open() closes the file automatically
    strip()

CSV:
    csv.reader()
    csv.writer()
    csv.DictReader()
    csv.DictWriter()
    writerow()
    writerows()
    writeheader()

JSON:
    json.dump()
    json.load()
    json.dumps()
    json.loads()

API / REQUESTS:
    requests.get()
    requests.post()
    requests.put()
    requests.patch()
    requests.delete()

RESPONSE:
    response.status_code
    response.json()
    response.raise_for_status()

OTHER:
    params=             # query parameters for a request
    json=               # JSON request body
    timeout=            # maximum time to wait for a response
    try / except        # handle errors
"""
