$(function () {

    $('.show__purchase__record').click(function () {
        $.ajax({
            url: '/inventory__webapp/show_purchase_record/',
            type: 'GET',
            dataType: 'json',
            success(response) {
                $('.main').html(response.purchase_render)
            }
        })
    })

    $('.add__product__button').click(function () {
        $.ajax({
            url: '/inventory__webapp/purchase_product/',
            type: 'get',
            dataType: 'json',
          
            success(response) {
                $('.modal .modal-content .modal-body').html(response.purchase_product_form);
                $('#myModal').modal('show');
            }
        })

    })

   
   
})