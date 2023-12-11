<!-- list_candidates.tpl -->

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
                <a href="/vote/{{ candidate['id'] }}">{{ candidate['name'] }}</a>
                
            </li>
        % end
    </ul>
</body>
</html>
