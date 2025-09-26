$(document).ready(function () {
  console.log("Student Jquery");

  // $(document).on("click", ".imagePreview_row", function () {
  //   console.log("Image clicked");
  //   const imgSrc = $(this).attr("src"); // get the clicked image src
  //   $("#modalImage").attr("src", imgSrc); // set it to modal image
  // });

  $("#profile_pic").on("change", function (event) {
    const file = event.target.files[0];
    const preview = $("#imagePreview");
    const modalImg = $("#modalImage"); // <-- modal image

    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        preview.attr("src", e.target.result).show();
        modalImg.attr("src", e.target.result); // <-- sync modal image
      };
      reader.readAsDataURL(file);
    } else {
      preview.attr("src", "").hide();
      modalImg.attr("src", ""); // clear modal too
    }
  });

  $("#student_register_btn").click(function (e) {
    e.preventDefault();

    console.log("AAAAAAAAA");

    $("#student_name").prop("disabled", false);
    $("#email").prop("disabled", false);

    const student_id = $("#student_id").val();
    const formElement = document.getElementById("studentForm");
    let formData = new FormData(formElement);

    $.ajax({
      url: student_id ? `edit_student/${student_id}/` : `addStudent/`,
      method: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        formElement.reset();
        $("#student_register_btn").text("Register");

        const collapseEl = document.getElementById("studentFormCollapse");
        const collapse = bootstrap.Collapse.getInstance(collapseEl);
        if (collapse) {
          collapse.hide();
        }

        $("#acknowledge")
          .text(response.message)
          .css("color", "green")
          .fadeIn()
          .delay(2000)
          .fadeOut();

        $("#studentlist").html(response.students);
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

  $(document).on("click", ".student-profile-btn", function (event) {
    event.preventDefault();
    const studentId = $(this).data("id");
    console.log(studentId);

    $.ajax({
      url: `student_profile/${studentId}/`,
      method: "GET",
      success: function (response) {
        $("#student-details").html(response.student);
        // $("#studentModal").modal("show");
        var myModal = new bootstrap.Modal(
          document.getElementById("studentModal")
        );
        myModal.show();
      },
      error: function () {
        alert("Failed to load student details");
      },
    });
  });

  $(document).on("click", ".editStudentBtn", function (event) {
    event.preventDefault();
    console.log("Edit button clicked");

    // Lock fields when editing
    $("#student_name").prop("disabled", true);
    $("#email").prop("disabled", true);

    const studentModalEl = document.getElementById("studentModal");
    const studentModal = bootstrap.Modal.getInstance(studentModalEl);
    if (studentModal) {
      studentModal.hide();
    }

    const collapseEl = document.getElementById("studentFormCollapse");
    const collapse = new bootstrap.Collapse(collapseEl, {
      toggle: false,
    });
    collapse.show();

    console.log("Edit button clicked 2");

    let studentId = $(this).data("id");
    const name = $(this).data("name");
    const age = $(this).data("age");
    const gender = $(this).data("gender");
    const address = $(this).data("address");
    const guardian_name = $(this).data("guardian_name");
    const guardian_relation = $(this).data("guardian_relation");
    const guardian_contact = $(this).data("guardian_contact");
    const phone_number = $(this).data("phone_number");
    const email = $(this).data("email");
    const stream = $(this).data("stream");
    const roll_number = $(this).data("roll_number");
    const section = $(this).data("section");
    const profilePic = $(this).data("profile_pic");

    console.log("Edit button clicked 3");

    console.log(studentId, name, age, gender, address, stream, section, profilePic);

    $("#student_id").val(studentId);
    $("#student_name").val(name);
    $("#age").val(age);
    $("#gender").val(gender);
    $("#address").val(address);
    $("#guardian_name").val(guardian_name);
    $("#guardian_relation").val(guardian_relation);
    $("#guardian_contact").val(guardian_contact);
    $("#phone_number").val(phone_number);
    $("#email").val(email);
    $("#stream").val(stream);
    $("#section").val(section);
    $("#imagePreview").attr("src", profilePic).show();
    $("#modalImage").attr("src", profilePic).show();

    $("#student_register_btn").text("Update");
  });

  $(document).on("click", ".deleteStudentBtn", function (event) {
    event.preventDefault();
    const studentModalEl = document.getElementById("studentModal");
    const studentModal = bootstrap.Modal.getInstance(studentModalEl);
    if (studentModal) {
      studentModal.hide();
    }

    console.log("Delete button clicked");
    let studentId = $(this).data("id");
    const csrfToken = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      url: `delete_student/${studentId}/`,
      method: "POST",
      data: {
        csrfmiddlewaretoken: csrfToken,
      },
      success: function (response) {
        $("#acknowledge")
          .text("Student Deleted Successfully")
          .css("color", "green")
          .fadeIn()
          .delay(2000)
          .fadeOut();
        $("#studentlist").html(response.students);
      },
      error: function (error) {
        $("#acknowledge")
          .text("Failed to delete the stream")
          .css("color", "red")
          .fadeIn()
          .delay(2000)
          .fadeOut();
      },
    });
  });
});
