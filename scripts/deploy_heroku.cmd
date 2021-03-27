call heroku login
call heroku git:remote -a pauper-system-backend
call git push heroku main
call heroku ps:scale web=1
