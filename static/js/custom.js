$(".extra-fields-customer").click(function () {
  $(".customer_records").clone().appendTo(".customer_records_dynamic");
  $(".customer_records_dynamic .customer_records").addClass("single remove");
  $(".single .extra-fields-customer").remove();
  $(".single").append(
    '<a href="#" class="remove-field btn-remove-customer col-md-12 mt-2">Remove Fields</a>'
  );
  $(".customer_records_dynamic > .single").attr("class", "remove mt-3 row");
});

$(document).on("click", ".remove-field", function (e) {
  $(this).parent(".remove").remove();
  e.preventDefault();
});

$(".moreless-button").click(function () {
  $(".moretext").slideToggle();
  if ($(this).text() == "See more") {
    $(this).text("See less");
  } else {
    $(this).text("See more");
  }
});
