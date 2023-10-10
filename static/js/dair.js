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
function openModal(mediaUrl, mediaType) {
  // الحصول على عناصر النافذة المودالية
  const modalViewsDairImg = document.getElementById("modal_views_dair_img");
  const modalImageDair = document.getElementById("modal_image_dair");
  const modalVideoDair = document.getElementById("modal_video_dair");

  // التحقق من نوع الوسائط (صورة أم فيديو) وعرض المحتوى بناءً على ذلك
  if (mediaType === "image") {
    modalImageDair.src = mediaUrl; // تعيين مصدر الصورة
    modalImageDair.style.display = "block"; // عرض الصورة
    modalVideoDair.style.display = "none"; // إخفاء الفيديو
  } else if (mediaType === "video") {
    modalVideoDair.src = mediaUrl; // تعيين مصدر الفيديو
    modalVideoDair.style.display = "block"; // عرض الفيديو
    modalImageDair.style.display = "none"; // إخفاء الصورة
  }

  modalViewsDairImg.style.display = "block"; // عرض النافذة المودالية
}

// دالة لإغلاق النافذة المودالية ومسح المحتوى
function closeModal1() {
  // الحصول على عناصر النافذة المودالية
  const modalViewsDairImg = document.getElementById("modal_views_dair_img");
  const modalImageDair = document.getElementById("modal_image_dair");
  const modalVideoDair = document.getElementById("modal_video_dair");

  modalViewsDairImg.style.display = "none"; // إخفاء النافذة المودالية

  // إعادة تعيين مصادر الصورة والفيديو
  modalImageDair.src = "";
  modalVideoDair.src = "";
}
