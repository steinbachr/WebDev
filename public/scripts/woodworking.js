$(document).ready(function() {
    var RUKKUS_IMAGES = {
        DINING_TABLE: [
            {src: "public/images/woodworking/dining_table/dining_table_1.jpg", alt: "planning", caption: "the initial sketch for the table"},
            {src: "public/images/woodworking/dining_table/dining_table_2.jpg", alt: "joint", caption: "one of the mortises (the main joints for the table)"},
            {src: "public/images/woodworking/dining_table/dining_table_3.jpg", alt: "joint 2", caption: "side view of one of the mortises. I had to cut these all by hand using a chisel."},
            {src: "public/images/woodworking/dining_table/dining_table_4.jpg", alt: "end legs", caption: "pair of end legs"},
            {src: "public/images/woodworking/dining_table/dining_table_5.jpg", alt: "joint 3", caption: "yet another mortise"},
            {src: "public/images/woodworking/dining_table/dining_table_6.jpg", alt: "joint 4", caption: "...and again from the side"},
            {src: "public/images/woodworking/dining_table/dining_table_7.jpg", alt: "basic frame", caption: "the basic frame (minus bottom shelf)"},
            {src: "public/images/woodworking/dining_table/dining_table_8.jpg", alt: "joint 5", caption: "more mortises, hoorray"},
            {src: "public/images/woodworking/dining_table/dining_table_10.jpg", alt: "basic frame 2", caption: "the basic frame, bottom shoelf included"},
            {src: "public/images/woodworking/dining_table/dining_table_11.jpg", alt: "basic frame 3", caption: "and again from the side"},
            {src: "public/images/woodworking/dining_table/dining_table_12.jpg", alt: "end leg", caption: "one of the legs after a little stud embellishment + staining"},
            {src: "public/images/woodworking/dining_table/dining_table_13.jpg", alt: "finished 1", caption: "end result from the top. The finish was actually satin not gloss, that sheen wore off after a few hours."},
            {src: "public/images/woodworking/dining_table/dining_table_14.jpg", alt: "finished 2", caption: "end result from the side"}
        ],
        HEXAGONS: [
            {src: "public/images/woodworking/hexagons/hexagons_8.jpg", alt: "base hexagons", caption: "1 down, 4 to go"},
            {src: "public/images/woodworking/hexagons/hexagons_7.jpg", alt: "base hexagons", caption: "the hexagons before staining"},
            {src: "public/images/woodworking/hexagons/hexagons_5.jpg", alt: "hexagon light wires", caption: "mess of wires for the LED connections"},
            {src: "public/images/woodworking/hexagons/hexagons_6.jpg", alt: "hexagon light wire connection", caption: "one of the LED connections"},
            {src: "public/images/woodworking/hexagons/hexagons_2.jpg", alt: "hexagons from top", caption: "they look pretty cool from the top"},
            {src: "public/images/woodworking/hexagons/hexagons_3.jpg", alt: "hexagons from side", caption: "...and also from the side"},
            {src: "public/images/woodworking/hexagons/hexagons_4.jpg", alt: "hexagon lights", caption: "yup they've got some LED's hooked up"},
            {src: "public/images/woodworking/hexagons/hexagons_1.jpg", alt: "hexagons and whiskey", caption: "maybe not the most functional, but it is interesting to look at"}
        ],
        BOTTLE_OPENER: [
            {src: "public/images/woodworking/bottle_opener/bottle_opener_1.jpg", alt: "bottle opener", caption: "yes, it certainly gets used"},
            {src: "public/images/woodworking/bottle_opener/bottle_opener_2.jpg", alt: "bottle opener box", caption: "thankfully, its got a handy box for catching the caps"},
            {src: "public/images/woodworking/bottle_opener/bottle_opener_3.jpg", alt: "bottle opener box", caption: "of course it needs to be detachable so we don't run out of room"},
        ]
    };

    var diningTableColl = new ImageCollection(RUKKUS_IMAGES.DINING_TABLE);
    new ExpandedImageView({collection: diningTableColl, el: '.dining-table-screenshots-container .big-screenshot-container'});
    new MiniImagesView({collection: diningTableColl, el: '.dining-table-screenshots-container .thumbnails-container'});

    var hexagonsColl = new ImageCollection(RUKKUS_IMAGES.HEXAGONS);
    new ExpandedImageView({collection: hexagonsColl, el: '.hexagons-screenshots-container .big-screenshot-container'});
    new MiniImagesView({collection: hexagonsColl, el: '.hexagons-screenshots-container .thumbnails-container'});

    var bottleOpenerColl = new ImageCollection(RUKKUS_IMAGES.BOTTLE_OPENER);
    new ExpandedImageView({collection: bottleOpenerColl, el: '.bottle-opener-container .big-screenshot-container'});
    new MiniImagesView({collection: bottleOpenerColl, el: '.bottle-opener-container .thumbnails-container'});
});