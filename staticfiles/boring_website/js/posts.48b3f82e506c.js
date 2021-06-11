function closeImage() {
	document.getElementById('imageWindowDisplayer').style.display = "none";
}
function openImage(url) {
	var windowDisplayer = document.getElementById('imageWindowDisplayer');
	windowDisplayer.innerHTML = "";
	var image = document.createElement('IMG');
	var closeIcon = document.createElement('I');
	closeIcon.classList.add("fas");
	closeIcon.classList.add("fa-times-circle");
	closeIcon.addEventListener("click", closeImage);
	image.src = 'img/' + url;
	windowDisplayer.appendChild(image);
	windowDisplayer.appendChild(closeIcon);
	windowDisplayer.style.display = "block";
	document.onkeydown = function(evt) {
    	if (evt.keyCode == 27) {
        	closeImage();
    	}
	};	
}