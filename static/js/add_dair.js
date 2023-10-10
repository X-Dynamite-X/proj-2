// دالة لتبديل عرض النافذة المودالية
function toggleModal(displayValue) {
    const dataEntryModal = document.getElementById("data_entry_modal");
    dataEntryModal.style.display = displayValue;
  }
  
  // دالة لإغلاق النافذة المودالية
  function closeModal() {
    // العناصر المرتبطة بالصورة والفيديو
    const imagePreview = document.getElementById("dair_user_views_image");
    const videoPreview = document.getElementById("dair_user_views_video");
  
    // إعادة تعيين مصادر الصورة والفيديو وإضافة "hidden"
    imagePreview.src = "";
    videoPreview.src = "";
    imagePreview.classList.add("hidden");
    videoPreview.classList.add("hidden");
  
    // إغلاق النافذة المودالية
    toggleModal("none");
  }
  
  // الأزرار المستخدمة لفتح وإغلاق النافذة المودالية
  const openButton = document.getElementById("open_modal_img_dair");
  const closeButton = document.getElementById("close");
  
  openButton.addEventListener("click", () => toggleModal("block"));
  closeButton.addEventListener("click", closeModal);
  
  // استماع للنقر خارج النافذة المودالية لإغلاقها
  window.addEventListener("click", (event) => {
    const dataEntryModal = document.getElementById("data_entry_modal");
    if (event.target === dataEntryModal) {
      closeModal();
    }
  });
  
  // العناصر المستخدمة لعرض معاينة الصورة أو الفيديو
  const imagePreview = document.getElementById("dair_user_views_image");
  const videoPreview = document.getElementById("dair_user_views_video");
  const fileInput = document.getElementById("dair_img_and_video_file_input");
  
  // استماع لتغيير الملف المختار
  fileInput.addEventListener("change", function () {
    const file = this.files[0];
  
    if (file) {
      if (file.type.startsWith("image")) {
        imagePreview.src = URL.createObjectURL(file);
        imagePreview.classList.remove("hidden");
        videoPreview.classList.add("hidden");
      } else if (file.type.startsWith("video")) {
        videoPreview.src = URL.createObjectURL(file);
        videoPreview.classList.remove("hidden");
        imagePreview.classList.add("hidden");
      }
    } else {
      imagePreview.classList.add("hidden");
      videoPreview.classList.add("hidden");
    }
  });
  