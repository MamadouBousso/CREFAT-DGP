/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
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

