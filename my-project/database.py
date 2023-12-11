import sqlite3
from bottle import route, run, template, post, request, redirect

connection = sqlite3.connect("voting-system.db")

def get_candidates(id=None):
    cursor = connection.cursor()
    if id is None:
        rows = cursor.execute("select id, name, votes from candidates")
    else:
        rows = cursor.execute(f"select id, name, votes from candidates where id={id}")
    rows = list(rows)
    rows = [{'id': row[0], 'name': row[1], 'votes': row[2]} for row in rows]
    return rows

def get_voters():
    cursor = connection.cursor()
    rows = cursor.execute("select id, name from voters")
    rows = list(rows)
    rows = [{'id': row[0], 'name': row[1]} for row in rows]
    return rows
def get_current_user():
    return {'username': 'admin', 'role': 'admin'}

def add_candidate(name):
    cursor = connection.cursor()
    cursor.execute(f"insert into candidates(name, votes) values ('{name}', 0)")
    connection.commit()

def add_voter(id, name):
    cursor = connection.cursor()
#error handling
    try:
        cursor.execute(f"insert into voters(id, name) values ({id}, '{name}')")
        connection.commit()
    except sqlite3.IntegrityError:

        return template("alert_template.tpl", message=f"Voter with ID {id} already exists",link='/list')

def check_login(username, password):
    cursor = connection.cursor()
    cursor.execute(f"select * from users where username='{username}' and password='{password}'")
    user = cursor.fetchone()
    return user

def delete_candidate(candidate_id):
    cursor = connection.cursor()
    cursor.execute(f"delete from candidates where id={candidate_id}")
    connection.commit()

def update_vote(id):
    cursor = connection.cursor()
    cursor.execute(f"update candidates set votes = votes + 1 where id={id}")
    connection.commit()

def get_results():
    candidates = get_candidates()
    return sorted(candidates, key=lambda x: x['votes'], reverse=True)

def set_up_database():
    cursor = connection.cursor()
    try:
        cursor.execute("drop table candidates")
    except:
        pass
    try:
        cursor.execute("drop table voters")
    except:
        pass
    try:
        cursor.execute("drop table users")
    except:
        pass

    cursor.execute("create table candidates(id integer primary key, name text, votes integer)")
    cursor.execute("create table voters(id integer primary key, name text)")

    cursor.execute("create table users(id integer primary key, username text unique, password text, role text)")

    for candidate in ['Candidate A', 'Candidate B', 'Candidate C']:
        cursor.execute(f"insert into candidates (name, votes) values ('{candidate}', 0)")

    for voter in ['Voter 1', 'Voter 2', 'Voter 3']:
        cursor.execute(f"insert into voters (name) values ('{voter}')")

    for user in [('admin', 'admin123', 'admin'), ('user1', 'pass1', 'regular'), ('user2', 'pass2', 'regular')]:
        cursor.execute(f"insert into users (username, password, role) values ('{user[0]}', '{user[1]}', '{user[2]}')")


    connection.commit()

def test_set_up_database():
    print("testing set_up_database()")
    set_up_database()
    candidates = get_candidates()
    assert len(candidates) == 3
    names = [candidate['name'] for candidate in candidates]
    for name in ['Candidate A', 'Candidate B', 'Candidate C']:
        assert name in names

    voters = get_voters()
    assert len(voters) == 3
    voter_names = [voter['name'] for voter in voters]
    for name in ['Voter 1', 'Voter 2', 'Voter 3']:
        assert name in voter_names

def test_get_candidates():
    print("testing get_candidates()")
    candidates = get_candidates()
    assert type(candidates) is list
    assert len(candidates) == 3
    for candidate in candidates:
        assert type(candidate) is dict
        assert 'id' in candidate
        assert type(candidate['id']) is int
        assert 'name' in candidate
        assert type(candidate['name']) is str
        assert 'votes' in candidate
        assert type(candidate['votes']) is int

def test_add_candidate():
    print("testing add_candidate()")
    set_up_database()
    candidates = get_candidates()
    original_length = len(candidates)
    add_candidate("Candidate D")
    candidates = get_candidates()
    assert len(candidates) == original_length + 1
    names = [candidate['name'] for candidate in candidates]
    assert "Candidate D" in names

def test_update_vote():
    print("testing update_vote()")
    set_up_database()
    candidates = get_candidates()
    id = candidates[1]['id']
    votes = candidates[1]['votes']
    update_vote(id)
    candidates = get_candidates()
    assert candidates[1]['votes'] == votes + 1

def test_get_results():
    print("testing get_results()")
    set_up_database()
    update_vote(get_candidates()[0]['id'])
    results = get_results()
    assert len(results) == 3
    assert results[0]['votes'] == 1

if __name__ == "__main__":
    test_set_up_database()
    test_get_candidates()
    test_add_candidate()
    test_update_vote()
    test_get_results()
    add_voter(123, "sai")
    print("done.")
