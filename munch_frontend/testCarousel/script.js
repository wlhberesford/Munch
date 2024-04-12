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

let test = new SlideCarousel();

function setUp(){
    test.setUp("test-card")
    console.log("READY")
}


