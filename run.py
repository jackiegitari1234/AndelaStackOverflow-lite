
#this is imported from the __init__.py file contained in the subdirectory called app
from app import create_app 

app = create_app()

if __name__ == '__main__':
    app.run()
