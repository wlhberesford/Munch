

function getCurrentMeal(){
    const d = new Date();
    var hour = d.getHours();
    console.log(hour);
    if ( 7< hour && hour < 11){
        document.getElementById("current_food_title").innerHTML="What's For Breakfast?";
        console.log(hour);

    }else if ( hour < 16){
        document.getElementById("current_food_title").innerHTML="What's For Lunch?";

    } else if ( hour < 23){
        document.getElementById("current_food_title").innerHTML="What's For Dinner?";

    }else{
        document.getElementById("current_food_title").innerHTML="You gotta wait for food my boi";

    }
}

function makeCards(diningHall){

}

let currentCardIndex = 0;
const commonsStations = document.querySelectorAll('.Commons_Station');
const sageStations = document.querySelectorAll('.Sage_Station');
const barhStations = document.querySelectorAll('.Barh_Station');
const blitmanStations = document.querySelectorAll('.Blitman_Station');

let maxcards = cards.length;

function showCard(index) {
    cards.forEach((card, i) => {
      const offset = i - index;
      card.style.transform = `translateX(${offset * 100}%)`;
    });
}

function prevCard() {
    if (currentCardIndex > 0) {
      currentCardIndex--;
      showCard(currentCardIndex);
    }else{
      currentCardIndex=maxcards-1;
      showCard(currentCardIndex);
    }
}

function nextCard() {
    if (currentCardIndex < cards.length - 1) {
      currentCardIndex++;
      showCard(currentCardIndex);
    }else{
      currentCardIndex=0;
      showCard(currentCardIndex);
    }
}