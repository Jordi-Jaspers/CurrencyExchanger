let selectFrom = document.getElementById('currencyFrom');
let selectTo = document.getElementById('currencyTo');
let selectAmount = document.getElementById('amount');

function watchValues(){
    var FORMAT = "json";
    var FROM = selectFrom.options[selectFrom.selectedIndex].value;
    var TO = selectTo.options[selectTo.selectedIndex].value;
    var AMOUNT = selectAmount.value;

    fetch("https://currency-converter5.p.rapidapi.com/currency/convert?format="
    + FORMAT + "&from="
    + FROM + "&to="
    + TO + "&amount="
    + AMOUNT,
    {
    "method": "GET",
    "headers": {
        "x-rapidapi-host": "currency-converter5.p.rapidapi.com",
        "x-rapidapi-key": "151b0b9918msh2973aa6cdbc840cp1d73b9jsnf2794cc2844a"
    }})
    .then(response => {
        response.json().then(function(obj){
            if(obj.status == "success"){
                document.getElementById("exchangerate").value = new Number(obj.rates[TO].rate);
                document.getElementById("receive").value = new Number(obj.rates[TO].rate_for_amount);
                document.getElementById("lastupdate").innerHTML = obj.updated_date;
                document.getElementById("status").innerHTML = "Succes!";
            }
            else{
                document.getElementById("exchangerate").value = new Number(0);
                document.getElementById("receive").value = new Number(0);
                document.getElementById("lastupdate").innerHTML = "No Data Found";
                document.getElementById("status").innerHTML = "Failed: Valuta not in database";
            };
        });
        console.log(response);
    })
    .catch(err => {
        console.log(err);
    });
}

selectAmount.onchange = function() {watchValues()};
selectFrom.onchange =  function() {watchValues()};
selectTo.onchange =  function() {watchValues()};