heroku login
heroku git:remote -a pauper-system-backend
git push heroku main
heroku scale worker=1