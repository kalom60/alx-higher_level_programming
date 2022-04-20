const $ = window.$;
$.get(
  'https://swapi-api.hbtn.io/api/people/5/?format=json',
  function (data, status) {
    $('div#character').text(data.name);
  }
);
