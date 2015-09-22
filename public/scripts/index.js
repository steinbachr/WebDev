$(document).ready(function() {
    var RUKKUS_IMAGES = [
        {src: "public/images/product/rukkus/events.png", alt: "browse activity", caption: "browse around, see what's happening nearby"},
        {src: "public/images/product/rukkus/search.png", alt: "search activity", caption: "search by performer or by event"},
        {src: "public/images/product/rukkus/performer.png", alt: "performer activity", caption: "check out all of a performer's nearby (and far away) events"},
        {src: "public/images/product/rukkus/tickets1.png", alt: "ticket map 1", caption: "use the fully interactive map to find the perfect tickets"},
        {src: "public/images/product/rukkus/tickets2.png", alt: "ticket map 2", caption: "apply filters, zoom, and view real seat views to narrow your search"},
        {src: "public/images/product/rukkus/tickets3.png", alt: "ticket map 3", caption: "beautiful!"},
        {src: "public/images/product/rukkus/order_details.png", alt: "order details", caption: "easily track and view past orders"},
        {src: "public/images/product/rukkus/scan_tickets.png", alt: "scan tickets", caption: "No more printing out paper tickets, scan your tickets directly at the door!<br /><br /> *for select venues only"}
    ];


    var images = new ImageCollection(RUKKUS_IMAGES);
    images.selectedImage = images.at(0);

    new ExpandedImageView({collection: images, el: '.big-screenshot-container'});
    new MiniImagesView({collection: images, el: '.thumbnails-container'});
});