let pic = document.querySelector('.inputImg');
const picPrev = document.querySelector('.previewImg');

if (pic){
    // Change preview photo when input aplied by user
    pic.addEventListener("change", function() {
        if(pic.files){
            const [picName] = pic.files
            picPrev.src = URL.createObjectURL(picName)
        }
    })
}