document.addEventListener("DOMContentLoaded", function(event) {
	for(let a of document.querySelector('#navBar').firstElementChild.children){
		a.classList.remove('active')
	}
	if (document.querySelector('#home-active')) {
		document.querySelector('#navBar').firstElementChild.children[1].classList.add('active')
	}else if (document.querySelector('#quizz-active')) {
		document.querySelector('#navBar').firstElementChild.children[2].classList.add('active')
	}else if (document.querySelector('#games-active')) {
		document.querySelector('#navBar').firstElementChild.children[3].classList.add('active')
	}else if (document.querySelector('#posts-active')) {
		document.querySelector('#navBar').firstElementChild.children[4].classList.add('active')
	}else if (document.querySelector('#faq-active')) {
		document.querySelector('#navBar').firstElementChild.children[5].classList.add('active')
	}
	setTimeout(
		function() {
			fetch(document.body.dataset['review'])
			.then(response => response.json()) 
			.then(data => {
				let parsed_data = JSON.parse(data['elements']);
				let parent = document.querySelector('#review-inputs');
				parsed_data.forEach(element => {
					let input = document.createElement('input');
					let label = document.createElement('label');
					let span = document.createElement('span');
					input.addEventListener('input', function() {changeInputSpan(span, input.value)}, false);
					input.type = "range";
					input.min = 1;
					input.max = 100;
					input.setAttribute('value', '50');
					input.setAttribute('id', element.pk+'_'+element.fields.review);
					input.setAttribute('form', "review-inputs");
					input.name = element.pk+'_'+element.fields.review;
					label.classList.add('form-control');
					label.setAttribute('for', element.pk+'_'+element.fields.review);
					label.innerHTML = data['options'][element.fields.element]+":";
					label.style.maxWidth = "300px";
					label.style.margin = "auto";
					label.style.backgroundColor = "#ffeea6";
					label.style.fontSize = "110%";
					parent.appendChild(label);
					parent.appendChild(input);
					parent.appendChild(span);
				});
				let submit = document.createElement('input');
				submit.classList.add("btn");
				submit.classList.add("btn-primary");
				submit.classList.add("d-block");
				submit.classList.add("m-auto");
				submit.classList.add("btn-lg");
				submit.classList.add("p-4");
				submit.setAttribute('type', 'submit');
				submit.setAttribute('value', 'Send Review');
				parent.appendChild(submit);
			});
			document.querySelector('#review-container').style.display = "block";
	}, 300000);
});
function changeInputSpan(span, value) {
	span.innerHTML=value;
}