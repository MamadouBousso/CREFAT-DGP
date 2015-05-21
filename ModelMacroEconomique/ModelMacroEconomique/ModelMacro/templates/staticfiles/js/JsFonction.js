$(function(){
    $("#valider").click(function(){
        valide= true;
        if($("#cin").val() == ""){
            $("#cin").css("border-color","#ff0000");
            $("#cin").next(".ErreurMessage").fadeIn().text(" \r Veillez entrer un numero CIN").css("color","#ff0000");
            valide= false;
        }
        /*else if($("#cin").val().match(/^[0-9]+$/i)){
            $("#cin").css("border-color","#ff0000");
            $("#cin").next(".ErreurMessage").fadeIn().text(" \r Veillez entrer un numero CIN Valide").css("color","#ff0000");
            valide= false;
        }*/
        else{
            $("#cin").next(".ErreurMessage").fadeOut();
            $("#cin").css("border-color","#ffffff");
        }
        if($("#nom").val() == ""){
            $("#nom").css("border-color","#ff0000");
            $("#nom").next(".ErreurMessage").fadeIn().text(" \r Veillez entrer un nom").css("color","#ff0000");
            valide= false;
        }
        else if(!$("#nom").val().match(/^[a-z]+$/i))
        {
            $("#nom").css("border-color","#ff0000");
            $("#nom").next(".ErreurMessage").fadeIn().text(" \r Veillez entrer un nom Valide").css("color","#ff0000");
            valide= false;
        }
        else{
            
            $("#nom").css("border-color","#000000");
            $("#nom").next(".ErreurMessage").fadeOut();
        }
        if($("#prenom").val() == ""){
            $("#prenom").css("border-color","#ff0000");
            $("#prenom").next(".ErreurMessage").fadeIn().text(" \r Veillez entrer un prenom").css("color","#ff0000");
            valide= false;
        }
        else{
            $("#prenom").css("border-color","#000000");
            $("#prenom").next(".ErreurMessage").fadeOut();
        }
        return valide;
    });
    /*$("#numEmployer").click(function(){
        var numEmployer = $(this).find("option[name=idemp]").val();
        //alert(numEmployer);
        $.post("../js/index.php",{numEmployer:numEmployer},function(data){
            alert(data.length);
        });
        return false;
        
    })*/
});

  //**Retourne la valeur du select selectId
    function getSelectValue(selectId)
    {
    //**On récupère l'élement html <select>
        var selectElmt = document.getElementById(selectId);
        //selectElmt.options correspond au tableau des balises <option> du select
        //selectElmt.selectedIndex correspond à l'index du tableau options qui est actuellement sélectionné

        return selectElmt.options[selectElmt.selectedIndex].value;
    }
    // Fonction Ajax 
   function maFonctionAjax(unParametre,action)
{
   var MonAjax;
   if (window.XMLHttpRequest)
   {
      // Mozilla, Safari, ...
      MonAjax = new XMLHttpRequest();
   }
   else if (window.ActiveXObject)
   {  
      // IE
      MonAjax = new ActiveXObject('Microsoft.XMLHTTP');
   }
   else 
   {
      alert("Votre navigateur n'est pas adapté pour faire des requêtes AJAX..."); 
      MonAjax = false;
   }
   
   MonAjax.open('POST',"a.php",true); 
   
   MonAjax.onreadystatechange = function()
   {
      if (MonAjax.readyState == 4 && MonAjax.status == 200)
      {
         if(action=="fait1") { document.getElementById('LeRetour1').innerHTML = MonAjax.responseText;}
         if(action=="fait2") { document.getElementById('LeRetour2').innerHTML = MonAjax.responseText;}
      }
   }
   
   MonAjax.setRequestHeader('Content-type','application/x-www-form-urlencoded');
   MonAjax.send('unParametre='+unParametre+'&action='+action);                  
}

