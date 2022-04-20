const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const langg = $('INPUT#language_code').val();
    $.get(
      'https://fourtonfish.com/hellosalut/?lang=' + langg,
      function (data, status) {
        $('DIV#hello').text(data.hello);
      }
    );
  });
};
