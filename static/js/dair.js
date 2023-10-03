// script.js
function scrollLefte() {
    const scrollContainer = document.getElementById('dair_spase');
    scrollContainer.scrollLeft -= 120; // التمرير إلى اليسار بمقدار 140 بكسل
}

function scrollRight() {
    const scrollContainer = document.getElementById('dair_spase');
    scrollContainer.scrollLeft += 120; // التمرير إلى اليمين بمقدار 140 بكسل
}

document.addEventListener("DOMContentLoaded", function() {
    const openModalButton = document.getElementById("open_modal_img_dair");
    const modal = document.getElementById("data_entry_modal");
    const closeButton = document.getElementById("close");
    
    openModalButton.addEventListener("click", function() {
        modal.style.display = "block";
    });
    
    closeButton.addEventListener("click", function() {
        modal.style.display = "none";
    });
    
    window.addEventListener("click", function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});
var modal = document.getElementById('modal_views_dair_img');
var modalImage = document.getElementById('modal_image_dair');
var closeBtn = document.getElementsByClassName('close_img_dair')[0];

function openModal(imageUrl) {
    modalImage.src = imageUrl;
    modal.style.display = 'block';

    // قم بإغلاق المودال تلقائيًا بعد 30 ثانية
    setTimeout(function() {
        closeModal();
    }, 30000); // 30 ثانية
}

function closeModal() {
    modal.style.display = 'none';
}

// إغلاق المودال عند النقر على زر الإغلاق (x)
closeBtn.onclick = function() {
    closeModal();
};