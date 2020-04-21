import os

from dotenv import load_dotenv
from flask_migrate import Migrate, upgrade


load_dotenv(dotenv_path=".env")

from app import create_app, db
from app.models import User


app = create_app(os.getenv("FLASK_CONFIG") or "default")
app.app_context().push()
migrate = Migrate(app, db)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User,)


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    print(db)
    upgrade()
