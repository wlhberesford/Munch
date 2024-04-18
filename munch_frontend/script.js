class SlideCarousel{
  constructor(){
      this.className;
      this.slides;
      this.slideCount= 0;
      this.slideIndex=0;
  }

  setUp(idName){
      this.slideIndex = 0;
      var jQeryPre='[id^="';
      var jQeryPost='"]';

      this.slides=$(jQeryPre+idName+jQeryPost);
      this.slideCount= this.slides.length;
      console.log("Total slides: ",this.slideCount," ",this.slides.length);
      console.log("Currently: ",this.slideIndex);

      this.slides[this.slideIndex].dataset.active = true;
  }

  prevSlide(){
      this.slideIndex -= 1;
      this.showSlide(this.slideIndex+1);
  }

  nextSlide(){
      this.slideIndex += 1;
      this.showSlide(this.slideIndex-1);
  }

  showSlide(prev){
      if (this.slideIndex <0 ) {this.slideIndex = this.slideCount-1; }
      if (this.slideIndex >= this.slideCount) {this.slideIndex = 0; }
  
      console.log(prev,this.slideIndex)
  
      this.slides[this.slideIndex].dataset.active = true;
      delete this.slides[prev].dataset.active;
  }
}

function getCurrentMeal(){
    const d = new Date();
    var hour = d.getHours();
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

var commons=new SlideCarousel();
var sage=new SlideCarousel();
var blitman=new SlideCarousel();
var barh=new SlideCarousel();

console.log("READY");

function setUpCarousels(){
  commons.setUp("Commons-Card-");
  sage.setUp("Sage-Card-");
  blitman.setUp("Blitman-Card-");
  barh.setUp("Barh-Card");


  console.log("SETUP COMPLETE");
}




