$(document).ready(function() {
    $('.container').height($(document).height());
    $('.imgur-container').imgagine({
        boxViewSel: '.generate-boxes',
        gridViewSel: '.generate-grid',
        regenerateSel: '.generate-random'
    });
})
