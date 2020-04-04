import sqlite3

import pytest
from flaskr.db import get_db

def test_get_close_db(app):
    # Check db gets same connection each time
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute("SELECT 1")

    assert "closed" in str(e.value)

def test_init_db_command(runner, monkeypatch):
    # Test the init-db CLI works as intended
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    # Use a pytest monkeypatch to replace actual init with a fake
    monkeypatch.setattr("flaskr.db.init_db", fake_init_db)
    result = runner.invoke(args=["init-db"])
    assert "Initialised" in result.output
    assert Recorder.called