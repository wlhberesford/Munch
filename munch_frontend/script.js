

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