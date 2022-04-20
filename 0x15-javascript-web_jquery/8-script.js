const $ = window.$;
$.get(
  'https://swapi-api.hbtn.io/api/films/?format=json',
  function (data, status) {
    const res = data.results;
    for (let n = 0; n < res.length; n++) {
      $('ul#list_movies').append($('<li>').text(res[n].title));
    }
  }
);
