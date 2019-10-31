window.onload = function () {
  var navBar = document.querySelector("header nav");
  var topSearchBar = document.querySelector("header nav li.top-search-bar input");
  var midSearchBar = document.querySelector("header figure.logo input");
  var firstArticle = document.querySelector("main article:first-child");

  window.onscroll =  function() {
    var top = (window.pageYOffset || document.documentElement.scrollTop)  - (document.documentElement.clientTop || 0);
      if (top + 25 >= midSearchBar.offsetTop) {
          topSearchBar.style.visibility = "visible";
          midSearchBar.style.visibility = "hidden";
      }
      else {
        topSearchBar.style.visibility = "hidden";
        midSearchBar.style.visibility = "visible";
      }

      if (top + 50 >= firstArticle.offsetTop)
        navBar.classList.add("fixed-bg");
      else
        navBar.classList.remove("fixed-bg");
  };
}
