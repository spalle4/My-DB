<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vote for {{ candidate['name'] }}</title>
    <script>
        function validateVoterId() {
            var voterId = document.getElementById('voter_id').value;
            var numericRegex = /^[0-9]+$/;

            if (!numericRegex.test(voterId)) {
                alert('Voter ID should contain only numerical values.');
                return false;
            }

            return true;
        }
    </script>
</head>
<body>
    <h2>Vote for {{ candidate['name'] }}</h2>
    <form action="/vote" method="post" onsubmit="return validateVoterId();">
        <input type="hidden" name="candidate_id" value="{{ candidate['id'] }}">
        <label for="voter_id">Your ID:</label>
        <input type="text" id="voter_id" name="voter_id" required>
        <label for="voter_name">Your Name:</label>
        <input type="text" id="voter_name" name="voter_name" required>
        <button type="submit">Cast your vote</button>
    </form>
</body>
</html>
