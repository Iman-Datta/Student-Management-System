$(document).ready(function () {
  console.log("Subject Jquery");

  $("#subject_register_btn").click(function (event) {
    event.preventDefault();

    const subject_id = $("#subject_id").val();
    const stream_id = $("#stream_id").val();
    const subject_name = $("#subject_name").val();
    const csrfToken = $("input[name=csrfmiddlewaretoken]").val();

    console.log(stream_id, "", subject_name);

    $.ajax({
      url: `/subject/add_subject/`,
      method: "POST",
      data: {
        stream_id: stream_id,
        subject_name: subject_name,
        csrfmiddlewaretoken: csrfToken,
      },
      success: function (response) {
        $("#acknowledge")
          .text(response.message)
          .css("color", "green")
          .fadeIn()
          .delay(2000)
          .fadeOut();
        $("#subjectList").html(response.subjects);
      },
      error: function (error) {
        const errorMessage = error.responseJSON?.message || "An error occurred";
        $("#acknowledge")
          .text(errorMessage)
          .css("color", "red")
          .fadeIn()
          .delay(2000)
          .fadeOut();
      },
    });
  });
});

// $(document).on("click", ".sub_edit-brn", function (event) {
//   event.preventDefault();
//   const subject_id = $(this).data("id");
//   const subject_name = $(this).data("name");

//   console.log(`Subject ID: ${subject_id} Subject Name: ${subject_name}`);

//   $("#subject_id").val(subject_id);
//   $("#subject_name").val(subject_name);
//   $('#subject_register_btn').text('Update');
// });

$(document).on("click", ".sub_delete-btn", function (event) {
  event.preventDefault();

  const subject_id = $(this).data("id");
  const csrfToken = $("input[name=csrfmiddlewaretoken]").val();
  console.log(subject_id);

  $.ajax({
    url: `del_subject/${subject_id}/`,
    method: "POST",
    data: {
      csrfmiddlewaretoken: csrfToken,
    },
    success: function (response) {
      $("#acknowledge")
        .text(response.message)
        .css("color", "green")
        .fadeIn()
        .delay(2000)
        .fadeOut();

      $("#subjectList").html(response.subjects);
    },
    error: function (err) {
      $("#acknowledge")
        .text("Failed to delete the stream")
        .css("color", "red")
        .fadeIn()
        .delay(2000)
        .fadeOut();
    },
  });
});
