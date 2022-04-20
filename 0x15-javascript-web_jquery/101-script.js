const $ = window.$;
window.onload = function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append($('<li>').text('Item'));
  });

  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list').remove();
  });
};
