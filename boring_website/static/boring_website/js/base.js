document.addEventListener("DOMContentLoaded", function(event) {
	for(let a of document.querySelector('#navBar').firstElementChild.children){
		a.classList.remove('active')
	}
	if (document.querySelector('#home-active')) {
		document.querySelector('#navBar').firstElementChild.children[1].classList.add('active')
	}else if (document.querySelector('#about-active')) {
		document.querySelector('#navBar').firstElementChild.children[2].classList.add('active')
	}else if (document.querySelector('#games-active')) {
		document.querySelector('#navBar').firstElementChild.children[3].classList.add('active')
	}else if (document.querySelector('#posts-active')) {
		document.querySelector('#navBar').firstElementChild.children[4].classList.add('active')
	}else if (document.querySelector('#faq-active')) {
		document.querySelector('#navBar').firstElementChild.children[5].classList.add('active')
	}
	// setTimeout(
	// 	function() {
	// 		let container = document.createElement('div');
	// 		container.style.position = 'fixed';
	// 		container.style.top = '10%';
	// 		container.style.left = '5%';
	// 		container.style.width = '90%';
	// 		container.style.height = '80%';
	// 		container.style.backgroundColor = 'pink';
	// 		container.style.textAlign = 'center';
	// 		container.style.padding = '3rem';
	// 		container.innerHTML = "Time to Review the website<br>We will you offer 5 free diamonds.";
	// 		document.body.appendChild(container);
	// }, 50000);
});
