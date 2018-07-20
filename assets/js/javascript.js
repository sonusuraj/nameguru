$(document).ready(function() {
  $("#namefun").click(function() {
      $("#instfun").hide();
  });
  $("#namefun").click(function() {
      $("#funbox").show();
  });

  $("#divgender").hide();
  $("#divfirstletter").hide();
  $("#divnofletters").hide();
  $("#divlettertimes").hide();
  $("#getnm").hide();

  $('#religion').on('change', function() {
    if(this.value){
        $("#divreligion").hide();
        $("#divgender").show();
    }
  });
  $('#gender').on('change', function() {
    if(this.value){
        $("#divgender").hide();
        $("#divfirstletter").show();
    }
  });
  $('#firstletter').on('change', function() {
    if(this.value){
        $("#divfirstletter").hide();
        $("#divnofletters").show();
    }
  });
  $('#nofletters').on('change', function() {
    if(this.value){
        $("#divnofletters").hide();
        $("#divlettertimes").show();
        for(var i=1; i<=this.value; i++){
            $("#lettertimes").append('<input type="text" name="lt'+i+'" maxlength="1">&nbsp;&nbsp;');
        }
        $("#getnm").show();
    }
  });

});
