javascript:(function() {
    var url = prompt("Please enter a URL:");
    var option = parseInt(prompt("Choose an option (1: Video, 2: Audio):"));
    
    if (option === 1) {
        var joined_url = "https://lostshadowgd.github.io/py-yt/endpoint/?url=" + url;
    } else if (option === 2) {
        var joined_url = "https://lostshadowgd.github.io/py-yt/endpoint/audio/?url=" + url;
    } else {
        alert("Invalid option. Download Cancelled.");
        return;
    }
    
    setTimeout(function() {
        window.open(joined_url, '_blank');
    }, 1500);
})();
