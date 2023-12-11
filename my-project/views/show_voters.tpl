<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voters List</title>
</head>
<body>
    <h2>Voters List</h2>
    
    <!-- Add an input field for search -->
    <label for="searchInput">Search:</label>
    <input type="text" id="searchInput" oninput="searchVoters()" placeholder="Enter voter name">
    
    <ul id="votersList">
        % for voter in voters:
            <li>ID: {{ voter['id'] }}, Name: {{ voter['name'] }},Candidate ID: {{ voter['candidate_id'] }}</li>
        % end
    </ul>

    <script>
        function searchVoters() {
            // Get input value
            var input = document.getElementById("searchInput").value.toUpperCase();
            
            // Get the voter list
            var votersList = document.getElementById("votersList");
            
            // Get all list items in the voter list
            var voters = votersList.getElementsByTagName("li");
            
            // Loop through all list items
            for (var i = 0; i < voters.length; i++) {
                // Get the voter's name in uppercase
                var name = voters[i].innerText.toUpperCase();
                
                // Check if the input matches the voter's name
                if (name.indexOf(input) > -1) {
                    voters[i].style.display = "";
                } else {
                    voters[i].style.display = "none";
                }
            }
        }
    </script>
</body>
</html>
