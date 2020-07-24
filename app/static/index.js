// parses access_token from auth0 from url
var parseToken = function() {
    var url = window.location.href;
    s = url.indexOf("access_token") + "access_token=".length;
    e = url.indexOf("&expires_in");
    if (s > -1 && e > -1) {
        return "Bearer " + url.substring(s, e);
    }
    return null;
}

// stores access_token in localStorage
var login = function(token) {
    window.localStorage.setItem("token", token);
    $.ajaxSetup({
        headers: {
            'Authorization': token
        }
    });
    document.getElementById("token").value = token;
}

var logout = function() {
    window.localStorage.clear();
    document.getElementById("token").value = "";
}

window.onload = function() {
    var parsedToken = parseToken();
    if (parsedToken !== null) {
        login(parsedToken);
    }
    if (parsedToken) {
        document.getElementById("login").style.display = "none";
    } else {
        document.getElementById("logout").style.display = "none";
        document.getElementById("token").style.display = "none";
    }
}