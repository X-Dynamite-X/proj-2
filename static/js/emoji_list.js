document.addEventListener("DOMContentLoaded", function () {
    const emojiPickerButton = document.getElementById("emoji-picker-button");
    const selectedEmoji = document.getElementById("selected-emoji");
    const textMsgInput = document.getElementById("text_msg");

    // قم بتهيئة Emoji Picker
    const emojiPicker = new EmojiPicker({
      onSelect: (emoji) => {
        // عند اختيار أيموجي، قم بإضافته إلى مربع النص وعرضه
        textMsgInput.value += emoji;
        selectedEmoji.innerHTML = emoji;
      },
    });

    // افتح Emoji Picker عند النقر على الزر Emoji Picker
    emojiPickerButton.addEventListener("click", () => {
      emojiPicker.toggle();
    });
  });