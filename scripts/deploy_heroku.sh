heroku login
heroku git:remote -a pauper-system-backend
git push heroku main
heroku ps:scale web=2
