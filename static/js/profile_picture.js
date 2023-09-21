
$(document).ready(function () {
  // النقر على الصورة لفتح نافذة اختيار الملف للصورة الشخصية
  $("#profile_picture").click(function () {
      $("#profile_picture_input").click();
  });

  // النقر على الصورة الخلفية لفتح نافذة اختيار الملف للصورة الخلفية
  $("#profile_picture_background").click(function () {
      $("#profile_picture_background_input").click();
  });

  // عند تغيير ملف الصورة الشخصية
  $("#profile_picture_input").change(function () {
      var input = this;
      var preview = $("#profile_picture")[0];

      if (input.files && input.files[0]) {
          var reader = new FileReader();

          reader.onload = function (e) {
              preview.src = e.target.result;
          };

          reader.readAsDataURL(input.files[0]);
      }
  });

  // عند تغيير ملف الصورة الخلفية
  $("#profile_picture_background_input").change(function () {
      var input = this;
      var backgroundDiv = $(".background_img_user")[0];

      if (input.files && input.files[0]) {
          var reader = new FileReader();

          reader.onload = function (e) {
              backgroundDiv.style.backgroundImage = "url('" + e.target.result + "')";
          };

          reader.readAsDataURL(input.files[0]);
      }
  });
});

