let timeOut, selectedColor;
let extraColorButtons = [];
let colors = [5];
let	logoClickGameCounter, colorGameGuessed, colorGameMissed, colorLevel = 0;
let counter = 100;
let logoLoved = false;
const messages = ["I hope you are bored...","What's your favourite boring thing to do?","Do you have a boring pet?","I like your smile.","Everything is also nothing :O .","I want you to be bored.","Share with your friends your heart.","Be kind.","Be bored.","Don't get creative, being bored is better.","Do you like being bored?","We love boring things.","Happy boring day!","How is it going?","I want a boring snack!","Ouch...","Hey! Stop pushing the button.","You are boring.","I am boring.","BORING MESSAGE","Are you hungry?","Do you like this website?","How many times have you pushed this button?","You done yet?","I don't like creative people...","Procrastination is boring!","Encourage others to be bored.","Boring is love.","Keep Clam and stay bored.","I love the Boring Web","Boring Web supports you.","We love you.","Get lost!","BOOOOooooorrrRRinG."];

function loveTheLogo(game_function, game_likes) {
	document.body.style.background = "pink";
	let playing_area = document.querySelector("#game-content-box-"+game_function);
	playing_area.innerHTML = "";
	let button = document.createElement('button');
	button.addEventListener('click', loveTheLogoGame, false);
	let heart = document.createElement('i');
	heart.classList.add('fas');
	heart.classList.add('fa-heart');
	button.appendChild(heart);
	let title = document.createElement('h1');
	title.innerHTML = "Loved ";
	let number = document.createElement('span');
	number.innerHTML = game_likes+1;
	number.setAttribute('id', 'love-the-logo-clicks');
	title.append(number);
	playing_area.appendChild(button);
	playing_area.appendChild(title);
}
function loveTheLogoGame() {
	if (logoLoved == true) {
		return;
	}else{
		document.getElementById('love-the-logo-clicks').innerHTML = parseInt(document.getElementById('love-the-logo-clicks').innerHTML) + 1;
		logoLoved = true;
	}
}
function colorGame(game_function, game_likes) {
	let playing_area = document.querySelector("#game-content-box-"+game_function);
	playing_area.innerHTML = "";
	playing_area.setAttribute('id', 'guess-the-color-game');
	let options = document.createElement('div');
	options.setAttribute('id', 'guess-the-color-game-options');
	let result = document.createElement('span');
	result.setAttribute('id', 'color-result');
	let button1 = document.createElement('button');
	button1.addEventListener('click', function(){colorGuess(0);} ,false);
	let button1Color = document.createElement('span');
	button1Color.classList.add('colorOption');
	button1Color.setAttribute('id', 'colorOption0');
	button1.appendChild(button1Color);
	options.appendChild(result);
	options.appendChild(button1);
	let start = document.createElement('button');
	start.addEventListener('click', loadColorGame ,false);
	start.setAttribute('id', 'start-restart-color-game');
	let startText = document.createElement('h1');
	startText.innerHTML = "Start";
	let startIcon = document.createElement('i');
	startIcon.classList.add('fas');
	startIcon.classList.add('fa-play');
	startText.appendChild(startIcon);
	start.appendChild(startText);
	let restart = document.createElement('button');
	restart.addEventListener('click', resetColorGame, false);
	restart.setAttribute('id', 'reset-color-game');
	let restartText = document.createElement('h6');
	restartIcon = document.createElement('i');
	restartIcon.classList.add('fas');
	restartIcon.classList.add('fa-trash');
	restartText.appendChild(restartIcon);
	restart.appendChild(restartText);
	let stats = document.createElement('h4');
	let guessed = document.createElement('span');
	guessed.setAttribute('id', 'colorGuessedCounter');
	let missed = document.createElement('span');
	missed.setAttribute('id', 'colorMissedCounter')
	let rate = document.createElement('span');
	rate.setAttribute('id', 'colorRating');
	stats.innerHTML = "Colors guessed: "
	stats.appendChild(guessed)
	stats.appendChild(document.createElement('hr'));
	stats.innerHTML += "Missed: ";
	stats.appendChild(missed);
	stats.appendChild(document.createElement('hr'));
	stats.innerHTML += "Rate: ";
	stats.appendChild(rate);
	stats.innerHTML += "%";
	let levelset = document.createElement('h3');
	let colorLevel = document.createElement('span');
	colorLevel.setAttribute('id', 'guess-the-color-level');
	let colorLevelIcon = document.createElement('i');
	colorLevelIcon.classList.add('far');
	colorLevelIcon.classList.add('fa-frown-open');
	colorLevel.innerHTML = "0";
	colorLevel.appendChild(colorLevelIcon);
	levelset.innerHTML = "Level: ";
	levelset.appendChild(colorLevel);
	playing_area.appendChild(options);
	playing_area.appendChild(start);
	playing_area.appendChild(restart);
	playing_area.appendChild(stats);
	playing_area.appendChild(levelset);
	colorGameGuessed = 0;
	colorGameMissed = 0;
	loadColorGame();
}
function loadColorGame() {
	document.getElementById('start-restart-color-game').innerHTML = '<i class="fas fa-redo-alt"></i>'; 
	let optionFields = document.getElementsByClassName("colorOption");
	for(let colorcounter = 0; colorcounter < optionFields.length; colorcounter++) {
		// optionFields[colorcounter].innerHTML = colors[colorcounter] = getColor();
		// optionFields[colorcounter].style.color = colors[colorcounter];
		optionFields[colorcounter].innerHTML = "";
		optionFields[colorcounter].style.color = colors[colorcounter] = getColor();
		let circle = document.createElement("I");
		circle.classList.add("fas");
		circle.classList.add("fa-circle");
		circle.style.color = colors[colorcounter];
		circle.style.animation = "openColor 2s ease";
		optionFields[colorcounter].appendChild(circle);
	}
	document.getElementById("guess-the-color-game").style.backgroundColor = (selectedColor = colors[Math.floor((Math.random()*optionFields.length))]);
}
function colorGuess(option) {
	let resultIcon = document.createElement("I");
	if (colors[option] == selectedColor) {
		colorGameGuessed++;
		resultIcon.classList.add("fas");
		resultIcon.classList.add("fa-check");
		resultIcon.style.color = "green";
		document.getElementById('colorGuessedCounter').innerHTML = colorGameGuessed;
		document.getElementById('colorGuessedCounter').style.color = selectedColor;
	}else {
		colorGameMissed++;
		resultIcon.classList.add("fas");
		resultIcon.classList.add("fa-times");
		resultIcon.style.color = "red";
		document.getElementById('colorMissedCounter').innerHTML = colorGameMissed;
	}
	if((colorGameGuessed) >= Math.floor((Math.pow(5, colorLevel)*colorLevel)/(Math.pow(4, colorLevel))+1)) {
		levelUpColorGuess();
	}
	document.getElementById('color-result').innerHTML = "";
	document.getElementById('color-result').appendChild(resultIcon);
	loadColorGame();
	setColorRating();
}
function setColorRating() {
	document.getElementById('colorRating').innerHTML = ((colorGameGuessed / (colorGameMissed + colorGameGuessed))*100).toFixed(2);
}
function getColor() {
	let colorCode = Math.floor(Math.random()*16777215).toString(16);
	return "#"+colorCode;
}
function resetColorGame() {
	if (confirm('Do you really want to reset your progress?')) {
		colorGameGuessed = 0;
		colorGameMissed = 0;
		document.getElementById('colorRating').innerHTML = "";
		document.getElementById('colorGuessedCounter').innerHTML = "";
		document.getElementById('colorMissedCounter').innerHTML = "";
	}
	extraColorButtons.forEach(element => document.getElementById('guess-the-color-game-options').removeChild(element));
	extraColorButtons = [];
	document.getElementById('guess-the-color-level').innerHTML = colorLevel = 0;;
	loadColorGame();
}
function levelUpColorGuess() {
	colorLevel++;
	let optionFields = document.getElementsByClassName("colorOption");
	let newButton = document. createElement("BUTTON");
	let buttonSpan = document.createElement("SPAN");
	extraColorButtons.push(newButton);
	buttonSpan.setAttribute('id', "colorOption"+optionFields.length);
	buttonSpan.classList.add("colorOption");
	newButton.appendChild(buttonSpan);
	newButton.setAttribute("onclick", "colorGuess(" + optionFields.length + ");");
	document.getElementById('guess-the-color-game-options').appendChild(newButton);
	let levelField = document.getElementById('guess-the-color-level');
	let levelSymbolField = document.createElement("I");
	levelField.innerHTML = colorLevel + " ";
	if (colorLevel == 1) {
		levelSymbolField.classList.add("fas");
		levelSymbolField.classList.add("fa-stamp");
		levelSymbolField.style.color = "#77eb34";
	}else if (colorLevel == 2) {
		levelSymbolField.classList.add("fas");
		levelSymbolField.classList.add("fa-eraser");
		levelSymbolField.style.color = "#369400";
	}else if (colorLevel == 3) {
		levelSymbolField.classList.add("fas");
		levelSymbolField.classList.add("fa-paint-roller");
		levelSymbolField.style.color = "#54e880";
	}else if (colorLevel == 4) {
		levelSymbolField.classList.add("fas");
		levelSymbolField.classList.add("fa-paint-brush");
		levelSymbolField.style.color = "#60d1be";
	}else if (colorLevel == 5) {
		levelSymbolField.classList.add("fas");
		levelSymbolField.classList.add("fa-fill");
		levelSymbolField.style.color = "#15bed1";
	}else if (colorLevel == 6) {
		levelSymbolField.classList.add("fas");
		levelSymbolField.classList.add("fa-spray-can");
		levelSymbolField.style.color = "#1594d4";
	}else if (colorLevel == 7) {
		levelSymbolField.classList.add("fas");
		levelSymbolField.classList.add("fa-palette");
		levelSymbolField.style.color = "#f0ec24";
	}else if (colorLevel == 8) {
		levelSymbolField.classList.add("fas");
		levelSymbolField.classList.add("fa-brush");
		levelSymbolField.style.color = "#e37209";
	}else if (colorLevel == 9) {
		levelSymbolField.classList.add("fas");
		levelSymbolField.classList.add("fa-paw");
		levelSymbolField.style.color = "#adc4c2";
	}else {
		levelSymbolField.classList.add("fas");
		levelSymbolField.classList.add("fa-infinity");
		levelSymbolField.style.color = selectedColor;
	}
	levelField.appendChild(levelSymbolField);
}
function seconds_game(game_function, game_likes) {
	let playing_area = document.querySelector("#game-content-box-"+game_function);
	playing_area.innerHTML = "";
	let slider = document.createElement('div');
	slider.setAttribute('id', 'background-slider');
	let movement = document.createElement('span');
	movement.setAttribute('id', 'you-moved');
	movement.innerHTML = 'You moved!'
	let counterElement = document.createElement('p');
	counterElement.setAttribute('id', 'the-100-sec-game-time-left');
	counterElement.addEventListener('mouseenter', startCounter ,false);
	counterElement.addEventListener('mouseleave', clearCounter ,false);
	counterElement.innerHTML = 'Time left: ';
	let timeLeft = document.createElement('span');
	timeLeft.setAttribute('id', 'the-100-sec-game-time-left-counter');
	counterElement.appendChild(timeLeft);
	counterElement.innerHTML += 's.';
	playing_area.appendChild(slider);
	playing_area.appendChild(movement);
	playing_area.appendChild(counterElement);
}
function startCounter() {
	if ( counter <= 0) {
		document.getElementById('the-100-sec-game-time-left').innerHTML = "You Won!<br>Here have a Bannana &#x1F34C;"; 
		document.getElementById('you-moved').style.display =  "none";
		return;
	}
	document.getElementById('you-moved').style.visibility = "hidden";
	document.getElementById('the-100-sec-game-time-left-counter').innerHTML = counter-=1;
	timeOut = setTimeout(startCounter, 1000);
}
function clearCounter() {
	clearTimeout(timeOut);
	counter = 100;
	document.getElementById('the-100-sec-game-time-left-counter').innerHTML = counter;
	document.getElementById('you-moved').style.visibility =  "visible";

} 
function no_you_cant_win(game_function, game_likes) {
	let playing_area = document.querySelector("#game-content-box-"+game_function);
	playing_area.innerHTML = "";
	let cant_win = document.createElement('p');
	cant_win.setAttribute('id', 'you-cant-win-text')
	let click_section = document.createElement('span');
	click_section.setAttribute('id', 'click-section');
	let button = document.createElement('span');
	button.addEventListener('click', youClickYouWin, false)
	button.innerHTML = "Click to win!";
	click_section.appendChild(button);
	cant_win.appendChild(click_section)
	playing_area.appendChild(cant_win);
}
function youClickYouWin() {
	document.getElementById('you-cant-win-text').innerHTML = "<span id='youClickedYouWon'>You WON!</span>"; 
	return "Nice, you won!";
}
function getHint(gameHint) {
	alert("gameHint");
}
function boring_switch(game_function, game_likes) {
	let playing_area = document.querySelector("#game-content-box-"+game_function);
	load_switch_game(playing_area, 50);
}
function load_switch_game(playing_area, switchers) {
	playing_area.innerHTML = "";
	for (let index = 0; index < switchers; index++) {
		let switch_element = document.createElement('div');
		switch_element.classList.add('switch-container');
		let icon = document.createElement('span');
		icon.classList.add('switch-icon');
		icon.setAttribute('id', 'switch' + index);
		icon.addEventListener("click", function() {switcher(index)}, false);
		switch_element.appendChild(icon);
		switch_element.appendChild(document.createElement('hr'));
		playing_area.appendChild(switch_element);
	}
}
function switcher(switchId) {
	let switchElement = document.getElementById('switch' + switchId);
	switchElement.style.animation =  'switch 1s ease';
	setTimeout(function(){
		switchElement.style.transform =  'translate3d(15px, 0, 0)';
		switchElement.style.backgroundColor =  'green';
	}, 1000);
}
function rgba_game(game_function, game_likes) {
	let playing_area = document.querySelector("#game-content-box-"+game_function);
	playing_area.innerHTML = "";
	let section1 = document.createElement('h1');
	section1.setAttribute('id', 'color-rgba');
	let r_section = document.createElement('span');
	r_section.setAttribute('id', 'r-element');
	r_section.innerHTML = "R";
	r_section.addEventListener('mouseover',function() {rgbaColor(0);} , false);
	let g_section = document.createElement('span');
	g_section.setAttribute('id', 'g-element');
	g_section.addEventListener('mouseover',function() {rgbaColor(1);} , false);
	g_section.innerHTML = "G";
	let b_section = document.createElement('span');
	b_section.setAttribute('id', 'b-element');
	b_section.addEventListener('mouseover',function() {rgbaColor(2);} , false);
	b_section.innerHTML = "B";
	section1.appendChild(r_section);
	section1.appendChild(g_section);
	section1.appendChild(b_section);
	playing_area.appendChild(section1);
}
function rgbaColor(colorCode) {
	let backgroundElement = document.getElementById('color-rgba');
	if (colorCode == 0) {
		backgroundElement.style.background = 'red';
	}else if (colorCode == 1) {
		backgroundElement.style.background = 'green';
	}else if (colorCode == 2) {
		backgroundElement.style.background = 'blue';
	}
}
function ninja(game_function, game_likes) {
	let playing_area = document.querySelector("#game-content-box-"+game_function);
	playing_area.innerHTML = "";
	let text = document.createElement('p');
	text.classList.add('ninja');
	text.innerHTML = "DJ Ninja";
	let icon = document.createElement('i');
	icon.classList.add('fas');
	icon.classList.add('fa-user-ninja');
	icon.classList.add('fa-rotate-90');
	icon.addEventListener('click', revealNinja, false);
	playing_area.appendChild(text);
	playing_area.appendChild(icon);
}
function revealNinja() {
	document.getElementById('ninja').style.color = 'white';
	document.getElementById('ninja').style.display = 'block';
}
function mysterious_messages(game_function, game_likes) {
	let playing_area = document.querySelector("#game-content-box-"+game_function);
	playing_area.innerHTML = "";
	let button = document.createElement('button');
	button.addEventListener('click', getMessage, false);
	let text = document.createElement('span');
	text.setAttribute('id', 'mysterious-message-message');
	text.innerHTML = "Try it";
	button.appendChild(text);
	playing_area.appendChild(button);
}
function getMessage() {
	document.getElementById('mysterious-message-message').innerHTML = messages[Math.floor(Math.random()*messages.length)];
}
function logo_click(game_function, game_likes) {
	let playing_area = document.querySelector("#game-content-box-"+game_function);
	playing_area.innerHTML = "";
	let image =  document.createElement('img');
	image.src = 'https://cpmr-islands.org/wp-content/uploads/sites/4/2019/07/test.png';
	image.style.width = '100px'
	image.setAttribute('id', 'logo-click-image');
	image.addEventListener('click', logoClickGame, false);
	let text =  document.createElement('h4');
	text.innerHTML = "Total Clicks: ";
	let result = document.createElement('span');
	result.setAttribute('id', 'logo-click-clicks');
	logoClickGameCounter = 0;
	result.innerHTML = logoClickGameCounter;
	let message = document.createElement('span');
	message.setAttribute('id', 'logo-click-message');
	text.appendChild(result);
	text.appendChild(document.createElement('br'));
	text.appendChild(message);
	playing_area.appendChild(image);
	playing_area.appendChild(text);
}
function logoClickGame() {
	logoClickGameCounter++;
	document.getElementById('logo-click-clicks').innerHTML = logoClickGameCounter;
	document.getElementById('logo-click-message').innerHTML = "Good one! Keep it up!";
	if (logoClickGameCounter >= 50 && logoClickGameCounter < 100) {
		document.getElementById('the-logo-click-game').style.color = "#1f7a3c"
		document.getElementById('the-logo-click-game').style.animation = "bounce 1.5s ease infinite"
		document.getElementById('logo-click-message').innerHTML = "You sure are a good player!!!";
	}else if (logoClickGameCounter >= 100 && logoClickGameCounter < 205) {
		document.getElementById('the-logo-click-game').style.color = "#21ad62"
		document.getElementById('logo-click-message').innerHTML = "Are you not Bored yet?";
	}else if (logoClickGameCounter >= 250 && logoClickGameCounter < 500) {
		document.getElementById('the-logo-click-game').style.color = "#5dc9c2"
		document.getElementById('logo-click-message').innerHTML = "You got it, let's beat the Record!";
	}else if (logoClickGameCounter >= 500 && logoClickGameCounter < 1000) {
		document.getElementById('the-logo-click-game').style.color = "#88969e"
		document.getElementById('the-logo-click-game').style.animation = "shake 1.5s ease-in-out 1.0s infinite"
		document.getElementById('logo-click-message').innerHTML = "Whyyy? This is uselessss :/ ";
	}else if (logoClickGameCounter > 1000) {
		document.getElementById('the-logo-click-game').style.color = "#b2a406"
		document.getElementById('the-logo-click-game').style.fontSize = "140%"
		document.getElementById('logo-click-message').innerHTML = "Amazing job! You are the boss!";
	}
}
function mysterious_emoji(game_function, game_likes) {
	let playing_area = document.querySelector("#game-content-box-"+game_function);
	playing_area.innerHTML = "";
	let emojis_section = document.createElement('p');
	let emoji_list = ["&#9200", "&#9203", "&#9748", "&#9749", "&#9875", "&#9898", "&#9924", "&#9968", "&#9970", "&#9973", "&#9978", "&#9981", "&#9986", "&#11088", "&#127386", "&#127752", "&#127754", "&#127759", "&#127784", "&#127792", "&#127790", "&#127800", "&#127909", "&#127789", "&#127832", "&#127911", "&#127918", "&#127812", "&#127921", "&#127849", "&#127922", "&#127930", "&#127929", "&#127928", "&#127940", "&#127963", "&#128011", "&#128014", "&#128085", "&#128163", "&#128152", "&#128179", "&#128190", "&#128197", "&#128279", "&#128212", "&#128276", "&#128165", "&#128230", "&#128264", "&#128274", "&#128296", "&#128305", "&#128333", "&#128374", "&#128465", "&#128532", "&#128511", "&#128586", "&#128666", "&#128748", "&#129341", "&#129360", "&#129361", "&#129413", "&#129504", "&#129417", "&#129506", "&#129510", "&#129412", "&#129369", "&#128672"]
	emoji_list.forEach(emoji => {
		let span = document.createElement('span');
		span.innerHTML = emoji;
		emojis_section.appendChild(span);
	});
	playing_area.appendChild(emojis_section);
}
function boring_rain(game_function, game_likes) {
	let playing_area = document.querySelector("#game-content-box-"+game_function);
	playing_area.innerHTML = "Boring Rain Should display here..."
}
function game_loading(game_function, game_likes) {
	let gameSection = document.querySelector("#game-content-box-"+game_function);
	gameSection.innerHTML = "";
	let gameElement1 = document.createElement("p");
	gameElement1.innerHTML = "LOADING";
	gameSection.appendChild(gameElement1);
	let gameElement2 = document.createElement("h1");
	let gameElement2Element1 = document.createElement("i");
	gameElement2Element1.classList.add("fas")
	gameElement2Element1.classList.add("fa-spinner");
	gameElement2Element1.classList.add("fa-spin");
	gameElement2.appendChild(gameElement2Element1);
	gameSection.appendChild(gameElement2);
	let caption = document.createElement("figcaption");
	caption.innerHTML = "Game will start soon";
	let details = document.createElement("details");
	let detailsElement1 = document.createElement("summary");
	detailsElement1.innerHTML = "Load more info";
	details.appendChild(detailsElement1);
	let detailsElement2 = document.createElement("p");
	detailsElement2.innerHTML = "This game is abou";
	let detailsElement2Element1 = document.createElement("span");
	detailsElement2Element1.classList.add("loading-dots");
	let detailsElement2Element1Element1 = document.createElement("i");
	detailsElement2Element1Element1.classList.add("fas");
	detailsElement2Element1Element1.classList.add("fa-circle");
	let detailsElement2Element1Element2 = document.createElement("i");
	detailsElement2Element1Element2.classList.add("fas");
	detailsElement2Element1Element2.classList.add("fa-circle");
	let detailsElement2Element1Element3 = document.createElement("i");
	detailsElement2Element1Element3.classList.add("fas");
	detailsElement2Element1Element3.classList.add("fa-circle");
	detailsElement2Element1.appendChild(detailsElement2Element1Element1);
	detailsElement2Element1.appendChild(detailsElement2Element1Element2);
	detailsElement2Element1.appendChild(detailsElement2Element1Element3);
	detailsElement2.appendChild(detailsElement2Element1);
	details.appendChild(detailsElement2);
	let detailsElement3 = document.createElement("footer");
	let detailsElement3Element1 = document.createElement("p");
	detailsElement3Element1.innerHTML = "Developed by LoaderKing"
	detailsElement3.appendChild(detailsElement3Element1);
	details.appendChild(detailsElement3);
	let figure = document.createElement("figure");
	figure.appendChild(caption);
	figure.appendChild(details);
	let article = document.createElement("article");
	article.appendChild(figure);
	let title = document.createElement("h2");
	title.classList.add("game-title");
	title.innerHTML = "Game Loading";
	let gameContainer = document.createElement("section");
	gameContainer.classList.add("game-container");
	gameContainer.appendChild(title);
	gameContainer.appendChild(article);
	let gameBox = document.createElement("section");
	gameBox.classList.add("game-box");
	gameBox.classList.add("container-of-game-loading");
	gameBox.appendChild(gameContainer);
	gameSection.appendChild(gameBox);
}
function loadGame(game_function, gameLikes) {
	let deleteStuff = true;
	while (true) {
		let activeGame = document.getElementsByClassName("active-game");
		if (activeGame.length == 0) {
			break;
		}
		else {
			for(let i = 0; i < activeGame.length; i++) {
				activeGame[i].style.display = "none";
				activeGame[i].classList.remove("active-game");
			}
		}
	}
	let game = document.getElementsByClassName("container-of-the-"+game_function);
	for(let j = 0; j < game.length; j++) {
		game[j].classList.add("active-game");
		game[j].style.display = "block";
	}
	"x + sen(x^4ey)"
	try {
		this[game_function](game_function, gameLikes);	
		document.querySelector('#game-content-load-'+game_function).style.display = "none";
	} catch (error) {
		console.log("Game Function '"+game_function+"' not Founded\n" + error);
	}
}