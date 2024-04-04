class SlideCarousel{
    constructor(slides){
        this.slides=slides;
        this.slideCount= slides.length
        this.slideIndex=0;
    }

    setUp(){
        this.slideIndex = 0;
        this.slideCount= this.slides.length;
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

function setUp(slideList){
    slideList.forEach(i => {
        i.setUp();
    });
}

let carousel = [];
carousel[0] = new SlideCarousel(document.getElementsByClassName("card"));

setUp(carousel);






/*
let slideIndex = 0;
const cards = document.getElementsByClassName("card");
let cardCount;

function setUp(){
    slideIndex = 0;
    cardCount= cards.length;
    
    console.log(cards)
    console.log(cards.length)
};


function prevSlide(){
    slideIndex -= 1;
    showSlide(slideIndex+1);
};

function nextSlide(){
    slideIndex += 1;
    showSlide(slideIndex-1);
};

function showSlide(p){
    if (slideIndex <0 ) {slideIndex = cardCount-1; }
    if (slideIndex >= cardCount) {slideIndex = 0; }

    console.log(p,slideIndex)


    cards[slideIndex].dataset.active = true;
    delete cards[p].dataset.active;


};
*/
