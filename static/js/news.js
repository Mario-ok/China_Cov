function get_news() {
    $.ajax({
        url:'/news/',
        timeout:'10000',
        success:function (data) {
            var result = '';
            $.each(data,function () {
                result += '<div style="margin-top: 4%"><a id="title_a" href="'+this['url']+'" target="_blank" >'
                    + this['title']+'</a><span id="time_span">'+ this['date'] +'</span></div>';
            });
            $('#news').html(result);
        }
    })
}
get_news();
setInterval(get_news,1000*10);