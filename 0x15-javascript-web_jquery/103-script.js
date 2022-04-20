const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const langg = $('INPUT#language_code').val();
    hello(langg);
  });

  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      const langg = $('INPUT#language_code').val();
      hello(langg);
    }
  });

  const hello = (langg) => {
    const url = 'https://fourtonfish.com/hellosalut/?lang=';
    $.get(url + langg, function (data, status) {
      $('DIV#hello').text(data.hello);
    });
  };
};
