$(document).ready(function () {
  let catName = "";
  var urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has("catName")) {
    catName = urlParams.get("catName");
  }
  $.getJSON(`/api/v1/search?name=${catName}`, function (data, status, xhr) {
    let cats = data["results"];
    cats.forEach(function (cat) {
      let article = $("<article></article>");
      article.append("<figure></figure>");
      article.children("figure").append(`<img src=${cat["picture"]}>`);
      article.append("<section class='info'></section>");
      article.children("section").append(`<h1>${cat["name"]}</h1>`);
      article.children("section").append(`<h4>$${cat["price"]}</h4>`);
      article.children("section").append(`<p>${cat["description"]}</p>`);
      $("main").append(article);
    });
  });
});
