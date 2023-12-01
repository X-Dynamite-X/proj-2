// تعريف وظيفة للتمرير إلى اليسار
function scrollLefte() {
  const contentContainer = document.getElementById("dair_spase");
  contentContainer.scrollLeft -= 150;
}
// تعريف وظيفة للتمرير إلى اليمين
function scrollRight() {
  const contentContainer = document.getElementById("dair_spase");
  contentContainer.scrollLeft += 150;
}
// دالة لفتح النافذة المودالية وعرض الوسائط (صورة أو فيديو)
// دالة لفتح النافذة المودالية وإظهار الوسائط
function openModal(mediaUrl, mediaType) {
  const modalViewsDairImg = document.getElementById("modal_views_dair_img_video");
  const modalImageDair = document.getElementById("modal_image_dair");
  const modalVideoDair = document.getElementById("modal_video_dair");
  const modalBarDair = document.getElementById("bar");

  // التحقق من نوع الوسائط (صورة أم فيديو) وعرض المحتوى بناءً على ذلك
  if (mediaType === "image") {
    modalImageDair.src = mediaUrl; // تعيين مصدر الصورة
    modalImageDair.style.display = "block"; // عرض الصورة
    modalBarDair.style.display="block"
    modalVideoDair.style.display = "none"; // إخفاء الفيديو
      // إغلاق النافذة المودالية بعد 20 ثانية
      // setTimeout(function() {
      //   closeModal1();
      // }, 20000); // 20 ثانية = 20000 مللي ثانية
  } else if (mediaType === "video") {
    modalVideoDair.src = mediaUrl; // تعيين مصدر الفيديو
    modalVideoDair.style.display = "block"; // عرض الفيديو
    modalImageDair.style.display = "none"; // إخفاء الصورة
    modalBarDair.style.display="none"

  }

  modalViewsDairImg.style.display = "block"; // عرض النافذة المودالية

  // استمع لحدث "ended" عند انتهاء الفيديو وقم بإغلاق النافذة
  modalVideoDair.addEventListener('ended', function() {
    closeModal1(); // اسم الدالة التي تقوم بإغلاق النافذة
  });
}

// دالة لإغلاق النافذة


// دالة لإغلاق النافذة المودالية ومسح المحتوى
function closeModal1() {
  // الحصول على عناصر النافذة المودالية
  const modalViewsDairImg = document.getElementById("modal_views_dair_img_video");
  const modalImageDair = document.getElementById("modal_image_dair");
  const modalVideoDair = document.getElementById("modal_video_dair");

  modalViewsDairImg.style.display = "none"; // إخفاء النافذة المودالية

  // إعادة تعيين مصادر الصورة والفيديو
  modalImageDair.src = "";
  modalVideoDair.src = "";
}


// const contents = document.querySelectorAll('.media_container_image1');
// let currentIndex = 0;

// function showContent() {

//   contents[currentIndex].style.display = 'block';
//   setTimeout(hideContent, 3000); // عرض العنصر لمدة 30 ثانية

// }

// function hideContent() {
//   contents[currentIndex].style.display = 'none';
//   currentIndex++;

//   if (currentIndex >= contents.length) {
//     currentIndex = 0;
//   }

//   showContent(); // انتقال إلى العنصر التالي
// }

// showContent();



// ####################################



const contents = document.querySelectorAll('.media_container_image1');
let currentIndex = 0;

function showContent() {
  const currentContent = contents[currentIndex];
  const media = currentContent.querySelector('.media');

  if (media.tagName === 'IMG') {
    // عرض الصورة
    currentContent.style.display = 'block';
    setTimeout(hideContent, 3000); // عرض الصورة لمدة 3 ثواني
  } else if (media.tagName === 'VIDEO') {
    // تشغيل الفيديو
    media.play();
    currentContent.style.display = 'block';

    // استماع لانتهاء الفيديو ومن ثم تغيير العنصر
    media.addEventListener('ended', function() {
      currentContent.style.display = 'none'; // إخفاء العنصر الحالي بعد انتهاء الفيديو
      currentIndex++;

      if (currentIndex >= contents.length) {
        currentIndex = 0;
      }

      showContent(); // انتقال إلى العنصر التالي
    });
  }
}

function hideContent() {
  contents[currentIndex].style.display = 'none';
  currentIndex++;

  if (currentIndex >= contents.length) {
    currentIndex = 0;
  }

  showContent(); // انتقال إلى العنصر التالي
}

showContent(); // بدء العرض

