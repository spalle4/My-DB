<!-- admin.tpl -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Candidate List</title>
</head>
<body>
    <h2>Candidate List</h2>
    <ul>
        % for candidate in candidate_list:
            <li>
                 <p3>{{ candidate['name'] }}</p3>
                <form action="/delete/{{ candidate['id'] }}" method="post" style="display:inline;">
                    <button type="submit" onclick="return confirm('Are you sure you want to delete this candidate?')">Delete</button>
                </form>
            </li>
        % end
    </ul>
    <a href="/check_votes"><button>Check Votes</button></a>
    <a href="/voters"><button>View Voters</button></a>
</body>
</html>
