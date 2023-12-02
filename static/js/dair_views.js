
document.addEventListener("DOMContentLoaded", function() {
  var video = document.getElementById("modal_video_dair");

  // إضافة استماع لحدث التشغيل
  video.addEventListener("play", function() {
    console.log("تم تشغيل الفيديو");
  });

  // إضافة استماع لحدث الإيقاف
  video.addEventListener("pause", function() {
    console.log("تم إيقاف الفيديو");
  });
});

document.addEventListener("DOMContentLoaded", function() {
  var playButtonSvg = document.querySelector(".user_control_sbase_dair_play_button_svg");
  var pauseButtonSvg = document.querySelector(".user_control_sbase_dair_pause_button_svg");
  var video = document.getElementById("modal_video_dair"); // يجب عليك استبدال "your_video_element_id" بالمعرف الفعلي لعنصر الفيديو الخاص بك

  // إضافة استماع لحدث التشغيل
  video.addEventListener("play", function() {
    // إظهار رمز التوقف وإخفاء رمز التشغيل
    playButtonSvg.style.display = "none";
    pauseButtonSvg.style.display = "block";
  });

  // إضافة استماع لحدث الإيقاف
  video.addEventListener("pause", function() {
    // إظهار رمز التشغيل وإخفاء رمز التوقف
    playButtonSvg.style.display = "block";
    pauseButtonSvg.style.display = "none";
  });

  // إضافة استماع لتغيير حالة الـ checkbox
  document.getElementById("user_control_sbase_dair_start_puss_button_checkbox").addEventListener("change", function() {
    // تحديث حالة التشغيل/التوقف على الفيديو بناءً على حالة الـ checkbox
    if (this.checked) {
      video.play();
    } else {
      video.pause();
    }
  });
});



document.addEventListener("DOMContentLoaded", function() {
  var checkbox = document.querySelector(".user_control_sbase_dair_dair_noaudio_button_mute_voice_checkbox");
  var video = document.getElementById("modal_video_dair");
  var muteSvg = document.querySelector(".user_control_sbase_dair_dair_noaudio_button_mute_svg");
  var voiceSvg = document.querySelector(".user_control_sbase_dair_dair_noaudio_button_voice_svg");

  // تحديث حالة الرموز SVG على أساس حالة الكتم
  function updateSvgIcons() {
    if (video.muted) {
      muteSvg.style.display = "block";
      voiceSvg.style.display = "none";
    } else {
      muteSvg.style.display = "none";
      voiceSvg.style.display = "block";
    }
  }

  // إضافة استماع لتغيير حالة الـ checkbox
  checkbox.addEventListener("change", function() {
    var isChecked = checkbox.checked;

    // حفظ حالة الكتم في Local Storage
    localStorage.setItem("isMuted", isChecked);

    // تحديث حالة الكتم على الفيديو
    video.muted = !isChecked;

    // تحديث حالة الرموز SVG
    updateSvgIcons();

    // تحديث حالة الصوت في جميع الفيديوهات على الموقع
    updateAudioStatusForAllVideos(isChecked);
  });

  // إضافة استماع لتغيير حالة الفيديو
  video.addEventListener("volumechange", function() {
    // حفظ حالة الصوت في Local Storage
    localStorage.setItem("volumeLevel", video.volume);

    // تحديث حالة الرموز SVG
    updateSvgIcons();
  });

  // استرجاع حالة الكتم من Local Storage عند تحميل الصفحة
  var isMuted = localStorage.getItem("isMuted");
  if (isMuted === "true") {
    checkbox.checked = true;
    video.muted = true;
  }

  // استرجاع حالة الصوت من Local Storage عند تحميل الصفحة
  var savedVolumeLevel = localStorage.getItem("volumeLevel");
  if (savedVolumeLevel) {
    video.volume = parseFloat(savedVolumeLevel);
  }

  // تحديث حالة الرموز SVG عند تحميل الصفحة
  updateSvgIcons();
});

// تحديث حالة الصوت في جميع الفيديوهات على الموقع
function updateAudioStatusForAllVideos(isMuted) {
  // قم بالتحقق من وجود جميع الفيديوهات على الموقع وقم بتحديث حالة الصوت
  // يمكنك الوصول إلى الفيديوهات باستخدام معرفاتها أو أي آخر طريقة ملائمة
  var allVideos = document.querySelectorAll("video");
  allVideos.forEach(function(video) {
    video.muted = isMuted;
  });
}
