<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Check Votes</title>
</head>
<body>
    <h2>Vote Results</h2>
    <ul>
        % for result in results:
            <li>{{ result['name'] }} - Votes: {{ result['votes'] }}</li>
        % end
    </ul>
</body>
</html>
