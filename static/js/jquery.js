$(document).ready(function() {
    $("#searchbox").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#recipe-card div").filter(function() {
            $(this).toggle($(this).find('h5').text().toLowerCase().indexOf(value) > -1)
        });
    });
});