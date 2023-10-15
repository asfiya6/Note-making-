# to run the website
from website import create_app

app = create_app()

if __name__ == '__main__': #created in __init__.py
    app.run(debug=True) #automatically rerun the web server if we have changed the code