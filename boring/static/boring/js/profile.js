document.addEventListener("DOMContentLoaded", function(event) {
    if (!(document.querySelector('#content-selected') === null)) {
        let arrow = document.createElement('i');
        arrow.id = "arrow-back"
        arrow.classList.add('fas');
        arrow.classList.add('fa-arrow-left');
        let back = document.createElement('span');
        back.style.position = 'absolute';
        back.style.top = '5px';
        back.style.left = '5px';
        back.addEventListener('click', goBack, false);
        back.appendChild(arrow);
        arrow.style.display = 'none'
        document.querySelector('#content-selected').appendChild(back);   
    }
    if(!(document.querySelector('#notice') === null )) {
        setTimeout(() => {
            document.querySelector('#notice').animate([
                { transform: 'translateY(0px)' },
                { transform: 'translateY(-300px)' }
            ], {
                duration: 5000
            });   
        }, 5000);
        setTimeout(() => {
            document.querySelector('#notice').style.display = "none";
        }, 10000);
    }
    document.querySelectorAll('input').forEach(input => {
        input.classList.add('form-control');
        input.style.marginBottom = "1rem";
    });
    document.querySelectorAll('label').forEach(label => {
        label.classList.add('form-control');
        label.style.marginBottom = 0;
    });
    document.querySelectorAll('select').forEach(select => {
        select.classList.add('form-control');
        select.style.marginBottom = "1rem";
    });
    document.querySelectorAll('textarea').forEach(textarea => {
        textarea.classList.add('form-control');
        textarea.style.marginBottom = "1rem";
        textarea.style.height = "100px";
    });
});
function newGame() {
    openWindow("New Game! 1000 ,10");
    showElement('game-form');
};
function newPost() {
    openWindow("New Post! 500, 0");
    showElement('post-form');
};
function openShop() {
    openWindow("Boring Shop!<hr>");
    showElement('shop');
};
function openSettings() {
    openWindow("Settings");
    showElement('settings-form');

};
function showItems() {
    openWindow("Your Items!");
    showElement("items-collection");
};
function goBack(params) {
    document.querySelector('#content-selected-header').innerHTML = "";
    document.querySelector('#content-selected').style.display = "none";
    document.querySelector('#profile-menu').style.display = "block";
};
function openWindow(content) {
    document.querySelector('#profile-menu').style.display = "none";
    document.querySelector('#content-selected').style.display = "block";
    document.querySelector('#content-selected-header').innerHTML = content;
    document.querySelector('#arrow-back').style.display = 'block';
};
function showElement(name) {
    document.querySelectorAll('.form').forEach(form => form.style.display = 'none');
    document.querySelector('#'+name).style.display = 'block';
};
function filterItemType(url_type) {
    $.ajax({
        type: "GET",
        url: url_type,
        success: function (response) {
            let logged_user_id = document.querySelector('#shop-nav').dataset.userId;
            if (JSON.parse(response.items).length != 0) {
                document.querySelector('#shop-items-container').innerHTML = "";
                JSON.parse(response.items).forEach(item => {
                    let container = document.querySelector('#shop-items-container');
                    let card = document.createElement('div');
                    card.classList.add('card');
                    card.classList.add('shop-card');
                    card.classList.add('mb-3');
                    let card_body = document.createElement('div');
                    card_body.classList.add('col');
                    card_body.classList.add('card-body');
                    let item_name = document.createElement('h5');
                    item_name.classList.add('card-title');
                    item_name.innerHTML = item.fields.name;
                    let item_type = document.createElement('h6');
                    item_type.classList.add('card-subtitle');
                    item_type.classList.add('mb-2');
                    item_type.classList.add('text-muted');
                    item_type.innerHTML = item.fields.type;
                    let description = document.createElement('p');
                    description.classList.add('card-text');
                    description.innerHTML = item.fields.description;
                    let button = document.createElement('a');
                    let button_text = document.createElement('h6');
                    button_text.classList.add('card-text');
                    button.classList.add('card-link');
                    button.classList.add('btn');
                    let owns_item = false;
                    item.fields.user.forEach(user_id => {
                        if (user_id == logged_user_id )
                            owns_item = true;
                    })
                    if (owns_item) {
                        button.classList.add('btn-danger');
                        button.classList.add('disabled');
                        button_text.innerHTML += 'Owned!'
                    }else {
                        let coins = document.createElement('i');
                        coins.classList.add('fas');
                        coins.classList.add('fa-coins');
                        let diamonds = document.createElement('i');
                        diamonds.classList.add('far');
                        diamonds.classList.add('fa-gem');
                        button_text.appendChild(coins);
                        button_text.innerHTML += item.fields.price_coins
                        button_text.appendChild(diamonds);
                        button_text.innerHTML += item.fields.price_diamonds
                        button.classList.add('btn-success');
                    }
                    button.appendChild(button_text);
                    button.href = "boring_transaction/" + item.pk;
                    card_body.appendChild(item_name);
                    card_body.appendChild(item_type);
                    card_body.appendChild(document.createElement('hr'));
                    card_body.appendChild(description);
                    card_body.appendChild(button);
                    card.appendChild(card_body);
                    container.appendChild(card);
                });
            } else {
                document.querySelector('#shop-items-container').innerHTML = 'There are no ' + url_type.split("/")[url_type.split("/").length-1] + " items :( ..."
            }
            for(let type of document.querySelector('#shop-nav').children){
                type.classList.remove('active')
            }
            document.querySelector('#shop-nav-type-'+url_type.split("/")[url_type.split("/").length-1]).classList.add('active');
        },
        error: function (response) {
            console.log(response.responseJSON.errors)
        }
    });
};