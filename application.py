from project import create_app

# from project import scheduler_helper

# Call the application factory function to construct a Flask application
# instance using the development configuration
application = create_app("flask.cfg")

# if os.getenv("ENABLE_SCHEDULER") == "True":
#    scheduler_helper.start(application)
if __name__ == "__main__":
    application.run(debug=True)

