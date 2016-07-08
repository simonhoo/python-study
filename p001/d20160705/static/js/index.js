/**
 * Created by simon on 16/7/5.
 */

jQuery(function () {
    //检查请求参数
    jQuery("#userName").blur(
        function () {
            if(jQuery("#userName").val() == ""){
                alert("账号不能为空")
            }else {
                var userName = jQuery("#userName").val();

                jQuery.ajax({
                    type:"POST",
                    ur:"/login",
                })
            }
        }
    )


})
