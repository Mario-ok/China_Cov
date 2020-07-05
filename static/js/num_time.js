function get_num(){
    $.ajax({
        url:'/num/',
        timeout:'10000',
        success:function (data){
            $('#num:nth-child(1)').text(data[3]);
            $('#num:nth-child(2)').text(data[0]);
            $('#num:nth-child(3)').text(data[1]);
            $('#num:nth-child(4)').text(data[2]);
    },error:function (xhr,type) {

        }
    })
}
function get_time(){
    $.ajax({
        url:'/time/',
        timeout:'10000',
        success:function (data){
            $('#time').text(data)
    },error:function (xhr,type) {

        }
    })
}
get_num();
get_time();
setInterval(get_time,1000);
setInterval(get_num,1000*10);