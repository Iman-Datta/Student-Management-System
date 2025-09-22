$(document).ready(function () {
  console.log("Student Jquery");

  $("#student_register_btn").click(function (e) {
    e.preventDefault();

    console.log("AAAAAAAAA");

    $("#student_name").prop("disabled", false);
    $("#email").prop("disabled", false);

    const student_id = $("#student_id").val();
    // const student_name = $("#name").val();
    // const age = $("#age").val();
    // const gender = $("#gender").val();
    // const address = $("#address").val();
    // const guardian_name = $("#guardian_name").val();
    // const guardian_relation = $("#guardian_relation").val();
    // const guardian_contact = $("#guardian_contact").val();
    // const phone = $("#phone_number").val() || "";
    // const email = $("#email").val();
    // const stream = $("#stream").val();
    // const section = $("#section").val();
    // const csrfToken = $("input[name=csrfmiddlewaretoken]").val(); // This DOM element, name is a atribute of DOM
    const formElement = document.getElementById("studentForm");
    let formData = new FormData(formElement);

    $.ajax({
      url: student_id ? `edit_student/${student_id}/` : `addStudent/`,
      method: "POST",
      data: formData,
      processData: false,
      contentType: false,
      // {
      //   student_name: student_name,
      //   age: age,
      //   gender: gender,
      //   // dob: dob,
      //   address: address,
      //   guardian_name: guardian_name,
      //   guardian_relation: guardian_relation,
      //   guardian_contact: guardian_contact,
      //   phone_number: phone,
      //   email: email,
      //   stream: stream,
      //   section: section,
      //   csrfmiddlewaretoken: csrfToken,
      // },

      success: function (response) {
        // $("#name").val("");
        // $("#age").val("");
        // $("#gender").val("");
        // $("#date_of_birth").val("");
        // $("#address").val("");
        // $("#guardian_name").val("");
        // $("#guardian_relation").val("");
        // $("#guardian_contact").val("");
        // $("#phone_number").val("");
        // $("#email").val("");
        // $("#stream").val("");
        // $("#section").val("");
        formElement.reset();
        $("#student_register_btn").text("Register");
        // $("#student_heading").text("Student Register")

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
    // const dob = $(this).data("dob");
    // if (dob) {
    // dob = new Date(dob).toISOString().split("T")[0]; // "YYYY-MM-DD"
    // }
    const address = $(this).data("address");
    const guardian_name = $(this).data("guardian_name");
    const guardian_relation = $(this).data("guardian_relation");
    const guardian_contact = $(this).data("guardian_contact");
    const phone_number = $(this).data("phone_number");
    const email = $(this).data("email");
    const stream = $(this).data("stream");
    const roll_number = $(this).data("roll_number");
    const section = $(this).data("section");

    console.log("Edit button clicked 3");

    console.log(studentId, name, age, gender, address, stream, section);

    $("#student_id").val(studentId);
    $("#student_name").val(name);
    $("#age").val(age);
    $("#gender").val(gender);
    // $("#date_of_birth").val(dob);
    $("#address").val(address);
    $("#guardian_name").val(guardian_name);
    $("#guardian_relation").val(guardian_relation);
    $("#guardian_contact").val(guardian_contact);
    $("#phone_number").val(phone_number);
    $("#email").val(email);
    $("#stream").val(stream);
    $("#section").val(section);
    $("#student_register_btn").text("Update");
    // $("#student_heading").text("Student Profile Update")
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
