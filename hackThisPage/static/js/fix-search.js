window.onload = function () {
  var topSearchBar = document.querySelector("header nav li.top-search-bar input");
  var midSearchBar = document.querySelector("header figure.logo input");

  window.onscroll =  function() {
    var top = (window.pageYOffset || document.documentElement.scrollTop)  - (document.documentElement.clientTop || 0);
      console.log(top);
      if (top + 25 >= midSearchBar.offsetTop) {
          topSearchBar.style.visibility = "visible";
          midSearchBar.style.visibility = "hidden";
      }
      else {
        topSearchBar.style.visibility = "hidden";
        midSearchBar.style.visibility = "visible";
      }
  };
}
