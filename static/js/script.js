$(document).ready(function(){
    $("#submit").click(function(){
        $(this).html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Wait...');
        $(this).prop("disabled", true);
        const csrfmiddlewaretoken = ($("input[name=csrfmiddlewaretoken]").val());
        const url = $("#url").val();
        $("#url").prop("disabled", true);
        setTimeout(function() {
            $.post("api/short-url/", {"csrfmiddlewaretoken": csrfmiddlewaretoken, "url": url}, function (result) {
                $("#submit").html("Shorten").prop("disabled", false);
                $("#url").val("").prop("disabled", false);
                $("#short-url").val(window.location.origin+"/"+result.short_code+"/");
                $("#before").prop("hidden", true);
                $("#next").prop("hidden", false);
            });
        }, 2000);
  });

    $("#copy").click(function () {
        navigator.clipboard.writeText($("#short-url").val())
        $(this).html("Copied")
    });

    $("#back").click(function () {
        $("#before").prop("hidden", false);
        $("#next").prop("hidden", true);
    });
});