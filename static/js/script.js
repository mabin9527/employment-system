
var DELETE_ID;
$(function() {
  bindBtnDeleteEvent();
  bindBtnConfirmDeleteEvent();
  bindMouseClickEvent();
});

function bindBtnDeleteEvent() {
  $('.btn-delete').click(function() {
    $('#myModal').modal('show');
    DELETE_ID = $(this).attr('uid');
  });
}

function bindBtnConfirmDeleteEvent() {
  $('.btnConfirmDelete').click(function() {
    $.ajax({
      url: '/admin/' + DELETE_ID + '/delete/',
      type: 'GET',
      dataType: 'JSON',
      success: function (res) {
        if (res.status) {
          $('#myModal').modal('hide');
          $("tr[uid='"+DELETE_ID+"']").remove();
          DELETE_ID = 0;
        }else{
          alert(res.error);
        }
      }
    });
  });
}


