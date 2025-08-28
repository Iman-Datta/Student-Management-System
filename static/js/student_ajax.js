$(document).ready(function () {
  console.log("Student Jquery");

  $("#student_register_btn").click(function (e) {
    e.preventDefault();

    console.log("AAAAAAAAA");
    const student_name = $("#name").val();
    const age = $("#age").val();
    const gender = $("#gender").val();
    const dob = $("#date_of_birth").val();
    const address = $("#address").val();
    const guardian_name = $("#guardian_name").val();
    const guardian_relation = $("#guardian_relation").val();
    const guardian_contact = $("#guardian_contact").val();
    const phone = $("#phone_number").val();
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
      url: `addStudent/`,
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
        phone: phone,
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
});
