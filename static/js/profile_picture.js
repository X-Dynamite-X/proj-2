    const backgroundImgInput = document.getElementById('background_input_img');
    const backgroundPreviewImage = document.getElementById('background_preview_image');
    const profileImgInput = document.getElementById('profile_img_input');
    const profilePreviewImage = document.getElementById('profile_preview_image');

    backgroundImgInput.addEventListener('change', function() {
        const file = backgroundImgInput.files[0];

        if (file) {
            const reader = new FileReader();

            reader.onload = function(e) {
                backgroundPreviewImage.src = e.target.result;
            };

            reader.readAsDataURL(file);
        }
    });

    profileImgInput.addEventListener('change', function() {
        const file = profileImgInput.files[0];

        if (file) {
            const reader = new FileReader();

            reader.onload = function(e) {
                profilePreviewImage.src = e.target.result;
            };

            reader.readAsDataURL(file);
        }
    });
