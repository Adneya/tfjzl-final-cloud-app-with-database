Command:
curl.exe -s -c session.cookie -X POST http://localhost:5000/customer/login -H 'Content-Type: application/json' -d '{"username":"adneya7798","password":"Pass@123"}'

Output:
{"message":"User successfully logged in","accessToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbmV5YTc3OTgiLCJpYXQiOjE3NzYzNjQwMzMsImV4cCI6MTc3NjM2NzYzM30.svlTz5tjplO4pM6fQfHii_aO8vjrCjhQyON_FLkbzhI"}

