// enter trigger for keyword input field
$('#keyword_input').on('keyup', function (e) {
    if (e.key === 'Enter' || e.keyCode === 13) {
        document.getElementById('keyword-button').click();
    }
});


// enter trigger for user skill list
$('#skills_input').on('keyup', function (e) {
    if (e.key === 'Enter' || e.keyCode === 13) {
        document.getElementById('skills-button').click();
    }
});
