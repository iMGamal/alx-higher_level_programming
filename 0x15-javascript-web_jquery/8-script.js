$(document).ready(function() {
	$.git('https://swapi-api.alx-tools.com/api/films/?format=json').function(data) {
		for (const movie of data.results) {
			$('#UL#list_movies').append('<li>' + movie.title + '</li>');
		}
	});
});

