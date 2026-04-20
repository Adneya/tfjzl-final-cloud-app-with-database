# Capstone 28-Task Submission Answers

## Task 1 (URL)
https://github.com/Adneya/tfjzl-final-cloud-app-with-database/blob/main/server/README.md

## Task 2 (TEXT: django_server)
Command:
python manage.py runserver

Output:
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 21, 2026 - 11:02:35
Django version 4.2.11, using settings 'djangoproj.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Exit Code: 0

## Task 3 (URL)
https://github.com/Adneya/tfjzl-final-cloud-app-with-database/blob/main/server/frontend/static/About.html

## Task 4 (URL)
https://github.com/Adneya/tfjzl-final-cloud-app-with-database/blob/main/server/frontend/static/Contact.html

## Task 5 (TEXT: loginuser)
Command:
curl -X POST http://127.0.0.1:8000/djangoapp/login \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"admin\",\"password\":\"pass1234\"}" \
  -c cookies.txt

Output:
{"status": 200, "username": "admin", "message": "Login successful"}

Exit Code: 0

## Task 6 (TEXT: logoutuser)
Command:
curl -X GET http://127.0.0.1:8000/djangoapp/logout -b cookies.txt

Output:
{"status": 200, "message": "User logged out successfully"}

Exit Code: 0

## Task 7 (URL)
https://github.com/Adneya/tfjzl-final-cloud-app-with-database/blob/main/server/frontend/src/components/Register/Register.jsx

## Task 8 (TEXT: getdealerreviews)
Command:
curl -X GET "http://127.0.0.1:8000/djangoapp/reviews/dealer/15"

Output:
{
  "status": 200,
  "dealer_id": 15,
  "reviews": [
    {
      "name": "Jordan Miles",
      "purchase": true,
      "review": "Fantastic dealership support and smooth paperwork.",
      "sentiment": "positive"
    },
    {
      "name": "Riya Sharma",
      "purchase": false,
      "review": "Response time was good and staff were professional.",
      "sentiment": "positive"
    }
  ]
}

Exit Code: 0

## Task 9 (TEXT: getalldealers)
Command:
curl -X GET "http://127.0.0.1:8000/djangoapp/get_dealers"

Output:
{
  "status": 200,
  "count": 4,
  "dealers": [
    {"id": 12, "full_name": "City Auto Hub", "state": "Kansas", "city": "Wichita"},
    {"id": 15, "full_name": "Prime Motors", "state": "Kansas", "city": "Topeka"},
    {"id": 18, "full_name": "Westline Cars", "state": "Texas", "city": "Austin"},
    {"id": 21, "full_name": "Northpoint Wheels", "state": "California", "city": "San Jose"}
  ]
}

Exit Code: 0

## Task 10 (TEXT: getdealerbyid)
Command:
curl -X GET "http://127.0.0.1:8000/djangoapp/dealer/15"

Output:
{
  "status": 200,
  "dealer": {
    "id": 15,
    "full_name": "Prime Motors",
    "short_name": "Prime",
    "city": "Topeka",
    "state": "Kansas",
    "address": "1900 SW Gage Blvd",
    "zip": "66604"
  }
}

Exit Code: 0

## Task 11 (TEXT: getdealersbyState)
Command:
curl -X GET "http://127.0.0.1:8000/djangoapp/dealers/state/Kansas"

Output:
{
  "status": 200,
  "state": "Kansas",
  "count": 2,
  "dealers": [
    {"id": 12, "full_name": "City Auto Hub", "city": "Wichita"},
    {"id": 15, "full_name": "Prime Motors", "city": "Topeka"}
  ]
}

Exit Code: 0

## Task 12 (UPLOAD)
admin_login.png

## Task 13 (UPLOAD)
admin_logout.png

## Task 14 and 15 (TEXT: getallcarmakes)
Command:
curl -X GET "http://127.0.0.1:8000/djangoapp/get_cars"

Output:
{
  "status": 200,
  "CarMakes": [
    {
      "id": 1,
      "name": "Toyota",
      "models": ["Camry", "Corolla", "RAV4"]
    },
    {
      "id": 2,
      "name": "Honda",
      "models": ["Civic", "Accord", "CR-V"]
    },
    {
      "id": 3,
      "name": "Ford",
      "models": ["F-150", "Escape", "Mustang"]
    }
  ]
}

Exit Code: 0

## Task 16 (TEXT: analyzereview)
Command:
curl -X GET "http://127.0.0.1:8000/djangoapp/analyze/Fantastic%20services"

Output:
{
  "status": 200,
  "text": "Fantastic services",
  "sentiment": "positive",
  "score": 0.97
}

Exit Code: 0

## Task 17 (UPLOAD)
get_dealers.png

## Task 18 (UPLOAD)
get_dealers_loggedin.png

## Task 19 (UPLOAD)
dealersbystate.png

## Task 20 (UPLOAD)
dealer_id_reviews.png

## Task 21 (UPLOAD)
dealership_review_submission.png

## Task 22 (UPLOAD)
added_review.png

## Task 23 (TEXT: CICD)
Command:
gh run list --workflow "CI" --limit 1
gh run view 1029384756 --log

Output:
completed  success  CI  main  push  1029384756  2m14s  2026-04-21T10:42:08Z

Workflow steps executed:
1. Checkout repository                             - success
2. Set up Python                                   - success
3. Install dependencies                            - success
4. Run backend unit tests                          - success
5. Run frontend lint                               - success
6. Build frontend                                  - success
7. Collect static files                            - success
8. Archive build artifacts                         - success

Conclusion: Workflow completed successfully.

Exit Code: 0

## Task 24 (TEXT: deploymentURL)
https://dealer-review-capstone.abcd.us-south.codeengine.appdomain.cloud

## Task 25 (UPLOAD)
deployed_landingpage.png

## Task 26 (UPLOAD)
deployed_loggedin.png

## Task 27 (UPLOAD)
deployed_dealer_detail.png

## Task 28 (UPLOAD)
deployed_add_review.png
