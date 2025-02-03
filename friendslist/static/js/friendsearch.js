$(document).ready(function() {
    $('#search-button').on('click', function() {
        var query = $('#search_query').val();
        if (query.length > 2) {
            $.ajax({
                url: "{% url 'search-usernames' %}",
                data: {
                    'term': query
                },
                dataType: 'json',
                success: function(data) {
                    var suggestions = data.map(function(username) {
                        return '<option value="' + username + '">';
                    });
                    $('#username-suggestions').html(suggestions.join(''));
                }
            });
        }
    });
});