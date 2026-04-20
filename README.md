# Coursera Final Project Repository

This repository contains completed implementations and submission artifacts for two graded projects:

1. Express Book Reviews API (Node.js + Express)
2. Online Course Web App (Django)

It includes source code, required API evidence files, and rubric screenshots used for final submission.

## Repository Contents

- final_project
	- Node.js Express API for books and reviews
- onlinecourse_django_project
	- Django app with course, exam, and admin workflows
- Evidence files (command/output style)
	- githubrepo
	- getallbooks
	- getbooksbyISBN
	- getbooksbyauthor
	- getbooksbytitle
	- getbookreview
	- register
	- login
	- reviewadded
	- deletereview
- Screenshots
	- 1-getallbooks.png
	- 2-getbooksbyISBN.png
	- 3-getbooksbyauthor.png
	- 4-getbooksbytitle.png
	- 5-getbookreview.png
	- 6-register.png
	- 7-login.png
	- 8-reviewadded.png
	- 9-deletereview.png
	- 12-searchbyauthor.png
	- 13-searchbytitle.png
	- 03-admin-site.png
	- 07-final.png

## Project 1: Express Book Reviews API

### Location

final_project

### Stack

- Node.js
- Express
- express-session
- JSON Web Token (JWT)
- Axios

### Features Implemented

- Register new users
- Login for registered users
- Get all books
- Search books by ISBN, author, and title
- Get reviews by ISBN
- Add or modify review for authenticated users
- Delete review for authenticated users
- Promise callback endpoints
	- /promise/books
	- /promise/isbn/:isbn
- Async callback endpoints
	- /async/books
	- /async/author/:author
	- /async/title/:title

### Run Locally

```bash
cd final_project
npm install
node index.js
```

API base URL:

http://localhost:5000

## Project 2: Online Course Django App

### Location

onlinecourse_django_project

### Stack

- Python 3.10+
- Django 3.2.25
- SQLite

### Rubric-Aligned Files Implemented

- Models
	- onlinecourse_django_project/onlinecourse/models.py
	- includes Question, Choice, Submission and related models
- Admin
	- onlinecourse_django_project/onlinecourse/admin.py
	- includes 7 imported model classes and admin inline implementations
- Course details template
	- onlinecourse_django_project/onlinecourse/templates/onlinecourse/course_details_bootstrap.html
- Views
	- onlinecourse_django_project/onlinecourse/views.py
	- includes submit and show_exam_result
- URLs
	- onlinecourse_django_project/onlinecourse/urls.py
	- includes submit and show_exam_result routes

### Run Locally

```bash
cd onlinecourse_django_project
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8000
```

Application URL:

http://localhost:8000/onlinecourse/

Admin URL:

http://localhost:8000/admin/

## Submission Screenshots

- Admin page showing Authentication and Authorization + Onlinecourse
	- 03-admin-site.png
- Final exam result page showing successful attempt
	- 07-final.png

## Notes

- This repository is organized to keep implementation code and grading artifacts together.
- All required task files and screenshots are committed to main for direct URL submission.

## License

See LICENSE.