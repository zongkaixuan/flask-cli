from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, DataError


db = SQLAlchemy()


def commit_error_handler(d=db):
    """ Handle the error when we try to commit changes to DB """
    result = CommitResult()
    try:
        d.session.commit()
    except (IntegrityError, DataError) as e:
        result.error_code = e.orig.pgcode
        result.message = e.orig.pgerror
        # code 23505 means duplicate row in table
        result.level = 'warn' if result.error_code == '23505' else 'error'
        d.session.rollback()
    else:
        result.error_code = '0'

    return result


class CommitResult:
    def __init__(self, error_code=None, message=None, level=None):
        self.error_code = error_code
        self.message = message
        self.level = level


from .demo_model import Users
