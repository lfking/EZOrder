/**
 * Created by marina on 22/11/13.
 */

!function ($) {

  $(function(){


    $('.tooltip-test').tooltip()
    $('.popover-test').popover()

    $("[data-toggle=popover]")
      .popover('')

    $('.darken').hover(
    function(){
       $(this).find('.message').fadeIn(1000);
    },
    function(){
       $(this).find('.message').fadeOut(1000);
    }
    );

})

}(window.jQuery)
