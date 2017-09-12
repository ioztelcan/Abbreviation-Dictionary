# Abbreviation-Dictionary

This is a simple dictionary with a database and a front end that I created to hold all the abbreviations we use at Irdeto. 
And we have many, many abbreviations.

When I started, I pretty much knew nothing about databases or creating a working website for the project. I started following an
awesome tutorial about making your blog using Flask, by Miguel Grinberg. Instead of a blog, I implemented a simple searchable database.

You can find the tutorial here:
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

For the front end of my database, I just found a nice looking template on the internet and mutilated its code a bit. I found a really good one on azmind.com, where you can find a lot of nice Bootstrap templates.
- http://azmind.com/free-bootstrap-themes-templates/

## Dependencies

I used Python 2.7.12 to test out the code, so sticking to that would be smart. Following modules are required to make it work:

- Flask
- Flask-SQLAlchemy
- Flask-WTF

## How to Use

Once you get all the required libraries, the application can be started by running **run.py**.

This will start a local server at `127.0.0.1:5001` (The default flask port is 5000). You can navigate to this address with a browser and start searching.

README TODO:
- Creating a database and adding stuff.
