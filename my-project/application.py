from bottle import route, post, run, template, redirect, request
import database

@route("/")
def get_index():
    redirect("/login")

@route("/check_votes")
def check_votes():
    candidates = database.get_results()
    return template("check_votes.tpl", results=candidates)

@route("/voters")
def show_voters():
    voters = database.get_voters()
    return template("show_voters.tpl", voters=voters)
@route("/login")
def get_login():
    return template("login.tpl")

@post("/login")
def post_login():
    username = request.forms.get("username")
    password = request.forms.get("password")

    user = database.check_login(username, password)

    if user:
        if username=='admin':
            candidates = database.get_candidates()
            return template("admin.tpl",candidate_list=candidates)
        else:
            redirect("/list")
        
    else:
        return template("alert_template.tpl", message="Invalid username or password",link='/login')
        


@post("/delete/<id>")
def post_delete(id):
    candidates = database.get_candidates()
    database.delete_candidate(id)
    return template("admin.tpl",candidate_list=candidates)


@route("/list")
def get_list():
    candidates = database.get_candidates()
    return template("list_candidates.tpl", candidate_list=candidates)

@route("/vote/<id>")
def get_vote(id):
    candidate = database.get_candidates(id)
    return template("vote.tpl", candidate=candidate[0])

@post("/vote")
def post_vote():
    candidate_id = request.forms.get("candidate_id")
    voter_id = request.forms.get("voter_id")
    voter_name = request.forms.get("voter_name")
    result=database.add_voter(voter_id,voter_name,candidate_id)
    if result is None:
        database.update_vote(candidate_id)
        redirect("/list")
    else:
        return result    


    database.update_vote(candidate_id)
    redirect("/list")

run(host='localhost', port=8080, debug=True)
