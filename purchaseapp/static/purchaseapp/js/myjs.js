jQuery(document).ready(function(){


 // Add rows to the table
  jQuery('#Addmorebtnid').click(function(){
    var form_idx = $('#id_purchasedetails_set-TOTAL_FORMS').val();
    $('#idpurchasebilltbody').append($('#empty_form').html().replace(/__prefix__/g, form_idx)); 
    $('#id_purchasedetails_set-TOTAL_FORMS').val(parseInt(form_idx) + 1);


  });

  //To check repeated state value.
  jQuery('#id_StateName').change(function(){

    var statename = $(this).val();
    $.ajax({
      type: "GET",
      url: '/ajax/ValidateStateName/',
      data: {
        'statename': statename
      },
      dataType: 'json',
      success: function (data) {
        if (data.is_taken) {
          alert("Statename already exists.");
          jQuery('#id_StateName').val("");
        }
      }
    });
  });

    
    //Tocheck duplicate supplier exists

    jQuery('#id_PartyName').change(function(){

     var partyname = $(this).val();
     $.ajax({
       type: "GET",
       url: '/ajax/ValidatePartyName/',
       data: {
         'partyname': partyname
       },
       dataType: 'json',
       success: function (data) {
         if (data.is_taken) {
           alert("Supplier name already exists.");
           jQuery('#id_PartyName').val("");
         }
       }
     });

    });
    
    
    
    



  
    
  jQuery('#id_Paymode').change(function(){
      
    var value=jQuery('#id_Paymode option:selected').text()
    if((value=="Master")|| (value=="Credit") || (value=="Visa"))
       {
        $(".mastercarddetailstable").show(); 
       
       }
    else if ((value=="Cheque" ) || (value=="Cash")){

      $(".mastercarddetailstable").hide(); 
    }
  
      
      
  });


  //To get city based on state
  jQuery("#id_State").change(function () {

    var state = jQuery('#id_State option:selected').text();
    
    jQuery.ajax({
       
        type: "GET",
        url: "/ajax/CitynamebasedonState/",
        contents: "application/json; charset=utf-8",
        dataType: "json",
        data: { "argstate": state},
        success: function (response) {
            console.log(response)

            jQuery('#id_City').empty().append('<option selected="selected" value="">Please select City</option>');
            jQuery.each(response, function (i, item) {
                jQuery('#id_City').append(`<option value="${item.value}">${item.text}</option>`);
              
              });
          }
  
    });
        
  
  });

    
  //Toget hsncode and tax based on item selected

  jQuery('#id_purchasedetails_set-0-Item').change(function(){

    var item = jQuery('#id_purchasedetails_set-0-Item option:selected').text();
    
    $.ajax({
      type: "GET",
      url: '/ajax/GetHsnandTax/',
      data: {
        'item': item
      },
      dataType: 'json',
      success: function (hsn) {
        jQuery('#id_purchasedetails_set-0-HSNCode').val(hsn);
        
      }
      
    });




  })


  //Toget taxable value 
  jQuery('#id_purchasedetails_set-0-Taxable').blur(function(){
  
   qty=jQuery('#id_purchasedetails_set-0-Quantity').val();
   rate=jQuery('#id_purchasedetails_set-0-Rate').val();
   discount=jQuery('#id_purchasedetails_set-0-Disc').val();
   taxable=(qty*rate-discount)
   jQuery('#id_purchasedetails_set-0-Taxable').val(taxable)
  });


  //To assign cgst and sgst

  jQuery('#id_purchasedetails_set-0-Tax').change(function(){

    taxable=jQuery('#id_purchasedetails_set-0-Taxable').val();
    tax=jQuery('#id_purchasedetails_set-0-Tax').val();
    gst=taxable*tax/100
    cgst=gst/2;
    sgst=gst/2;
    jQuery('#id_purchasedetails_set-0-CGST').val(cgst);
    jQuery('#id_purchasedetails_set-0-SGST').val(sgst);
    discount=jQuery('#id_purchasedetails_set-0-Disc').val();
    amt=parseInt(taxable+cgst+sgst-discount)
    alert(parseInt(amt))
    jQuery('#id_purchasedetails_set-0-Amount').val(amt);
  })



})  
    
    

    
    
    
  
   


