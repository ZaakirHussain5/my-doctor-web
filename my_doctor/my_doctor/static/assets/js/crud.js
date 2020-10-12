
function crudOperations(options){

    jQuery(options.table_id).on('change','.active',function(){
        var button = jQuery(this)
        jQuery.getJSON(options.url + button.attr('data-id') + '/', {}, function(data) {
            var record = data;
            record.is_active = button.prop('checked');
            delete record.icon; 
            jQuery.ajax({
                data: JSON.stringify(record),
                method: 'PUT',
                url: options.url + button.attr('data-id') + '/',
                contentType: 'application/json',
                success: function(data) {
                    toastr.success(button.prop('checked')=='true'?'Activated Successfully':'Deactivated Successfully', 'Success', {
                        positionClass: "toast-top-center"
                    })
                },
                error: function(err) {
                    console.log(err)
                    toastr.error('Operation failed', 'Error', {
                        positionClass: "toast-top-center"
                    })
                }
            })
        })
      })
    
      jQuery(options.table_id).on('click', '.delete', function () {
        var id = jQuery(this).attr('data-id')  
        bootbox.confirm({
              message: "Are you sure to delete the Specialist Type permenently?",
              callback: function (result) {
                  if(result){
                      jQuery.ajax({
                          url:`${options.put_url}${id}`,
                          method: 'DELETE',
                          success:function(){
                              options.table.ajax.reload()
                              toastr.success("Deleted Successfully","Success",{positionClass:'toast-top-center'})
                          },
                          error:function(err){
                              console.log(err)
                              toastr.error("Deletion Failed","Error",{positionClass:'toast-top-center'})
                          }
                      })
                  }
              }
          });
      })
    
      jQuery(options.table_id).on('click', '.edit', function () {
          var data = JSON.parse(jQuery(this).attr('data-obj'))
          formDeserialize(document.getElementById(options.form_id.slice(1)), data)
          jQuery('#submitBtn').html('Update ' + options.entity)
          if(options.tabs){
            jQuery('#myTab a[href="#form"]').tab('show')
          }
          else{
            document.documentElement.scrollTop = 0;
          }
          
      })
    
      jQuery(options.form_id).submit(function(e){
          e.preventDefault();
          e.stopImmediatePropagation();
          var data = new FormData(this)
          if(document.getElementById('image1')!=null){
            if(document.getElementById('image1').files.length==0) data.delete('icon')
          }
          
          var action = 'POST'
          var url = options.url
          var successMessage = options.entity + ' Added Successfully'
          if(jQuery('#submitBtn').html() == 'Update ' + options.entity){
              action = 'PUT';
              url = `${options.put_url}${jQuery(options.id_selector).val()}/`
              successMessage = options.entity + ' Updated Successfully'
          }
          if(jQuery(options.form_id).valid()){
              jQuery.ajax({
                  url:url,
                  method:action,
                  data:data,
                  contentType:false,
                  processData:false
              }).done(function(data){
                  options.table.ajax.reload()
                  jQuery(options.form_id).trigger('reset');
                  jQuery('#submitBtn').html('Add ' + options.entity)
                  if(options.tabs){
                     jQuery('#myTab a[href="#list"]').tab('show')
                  }
                  jQuery( ".wrap-custom-file" ).load(window.location.href + " .wrap-custom-file" );
                  toastr.success(successMessage,"Success",{positionClass:'toast-top-center'})
              }).fail(function(data){
                  console.log(data)
                  toastr.error("Operation Failed","Success",{positionClass:'toast-top-center'})
              })
          }
      })
    
      function formDeserialize(form, data) {
        const entries = (new URLSearchParams(data)).entries();
        for (const [key, val] of entries) {
            const input = form.elements[key];
            if (input != undefined) {
                if (input.type == 'file') {
                    if (val) {
                        var $file = jQuery('#' + input.id),
                            $label = $file.next('label'),
                            $labelText = $label.find('span'),
                            labelDefault = $labelText.text();
                        var filename = val.split('/').pop()
                        console.log(filename)
                        if (filename) {
                            $label
                                .addClass('file-ok')
                                .css('background-image', 'url(' + val + ')');
                            $labelText.text(filename);
                        } else {
                            $label.removeClass('file-ok');
                            $labelText.text(labelDefault);
                        }
                    }
                    
                } else {
    
                    switch (input.type) {
                        case 'checkbox':
                            input.checked = !!val;
                            break;
                        case 'select-one':
                            if (val)
                                input.value = val;
                            else
                                input.selectedIndex = 0;
    
                            break;
                        default:
                            input.value = val;
                            break;
    
                    }
    
                }
            }
    
        }
    }
}
