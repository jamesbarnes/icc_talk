var public_spreadsheet_url = config.mySheet;;

sheet = []

window.onload = function() { init() };
 
function init() {
  Tabletop.init( { key: public_spreadsheet_url,
                   callback: showInfo,
                   simpleSheet: true } )
}

function showInfo(data, tabletop) {
  sheet = data;
  listSheet(data);
}

function listSheet(sheet){
  for(i=0;i<sheet.length;i++){
    $(".contentdiv").append("<h2>"+sheet[i].title+"</h2>");
    $(".contentdiv").append(sheet[i].ogdescription + "</br>");
    $(".contentdiv").append(sheet[i].bio);
  }
}