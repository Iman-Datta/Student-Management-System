$(document).ready(function () {
  console.log("Student Jquery");

  $("#student_register_btn").click(function (e) {
    e.preventDefault();

    console.log("AAAAAAAAA");

    const student_id = $("#student_id").val();
    const student_name = $("#name").val();
    const age = $("#age").val();
    const gender = $("#gender").val();
    const dob = $("#date_of_birth").val();
    const address = $("#address").val();
    const guardian_name = $("#guardian_name").val();
    const guardian_relation = $("#guardian_relation").val();
    const guardian_contact = $("#guardian_contact").val();
    const phone = $("#phone_number").val() || '';
    const email = $("#email").val();
    const stream = $("#stream").val();
    const section = $("#section").val();
    const csrfToken = $("input[name=csrfmiddlewaretoken]").val(); // This DOM element, name is a atribute of DOM

    console.log(
      student_name,
      age,
      gender,
      dob,
      address,
      guardian_name,
      guardian_relation,
      guardian_contact,
      phone,
      email,
      stream,
      section
    );

    $.ajax({
      url: student_id ? `edit_student/${student_id}/` : `addStudent/`,
      method: "POST",
      data: {
        student_name: student_name,
        age: age,
        gender: gender,
        dob: dob,
        address: address,
        guardian_name: guardian_name,
        guardian_relation: guardian_relation,
        guardian_contact: guardian_contact,
        phone_number: phone,
        email: email,
        stream: stream,
        section: section,
        csrfmiddlewaretoken: csrfToken,
      },

      success: function (response) {
        $("#name").val("");
        $("#age").val("");
        $("#gender").val("");
        $("#date_of_birth").val("");
        $("#address").val("");
        $("#guardian_name").val("");
        $("#guardian_relation").val("");
        $("#guardian_contact").val("");
        $("#phone_number").val("");
        $("#email").val("");
        $("#stream").val("");
        $("#section").val("");
        $("#student_register_btn").val("Register");

        $("#acknowledge")
          .text("Student Added Successfully")
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

    const studentModalEl = document.getElementById("studentModal");
    const studentModal = bootstrap.Modal.getInstance(studentModalEl);
    if (studentModal) {
      studentModal.hide();
    }

    $("#studentForm").collapse("show");

    console.log("Edit button clicked 2");

    const studentId = $(this).data("id");
    const name = $(this).data("name");
    const age = $(this).data("age");
    const gender = $(this).data("gender");
    const dob = $(this).data("dob");
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

    console.log(studentId, name, age, gender, dob, address, stream, section);

    $("#student_id").val(studentId);
    $("#name").val(name);
    $("#age").val(age);
    $("#gender").val(gender);
    $("#date_of_birth").val(dob);
    $("#address").val(address);
    $("#guardian_name").val(guardian_name);
    $("#guardian_relation").val(guardian_relation);
    $("#guardian_contact").val(guardian_contact);
    $("#phone_number").val(phone_number);
    $("#email").val(email);
    $("#stream").val(stream);
    $("#section").val(section);
    $("#student_register_btn").text("Update")
  });
});
