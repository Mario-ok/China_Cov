function get_all_day(){
    $.ajax({
        url:'/day',
        timeout:'10000',
        success:function(data){
            day_list = data.key;
            diagnosis_list = data.value1;
            cure_list = data.value2;
            dead_list = data.value3;
            var myec = echarts.init(document.getElementById('l1'));
            option = {
                title: {
                    left:'10%',
                    text: '全国累计趋势',
                    textStyle:{
                        color:"rgba(255, 255, 255, 1)",
                    },
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    left:'right',
                    textStyle:{
                        color:"rgba(255, 255, 255, 1)",
                    },
                    data: ['累计确诊', '累计治愈', '累计死亡'],
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                toolbox: {
                    feature: {
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    axisLine: {
                      lineStyle: {
                        color:"rgba(255, 255, 255, 1)",
                      }
                    },
                    data: day_list
                },
                yAxis: {
                    type: 'value',
                    axisLine: {
                      lineStyle: {
                        color:"rgba(255, 255, 255, 1)",
                      }
                    },
                },
                series: [
                    {
                        name: '累计确诊',
                        type: 'line',
                        stack: '总量',
                        data: diagnosis_list
                    },
                    {
                        name: '累计治愈',
                        type: 'line',
                        stack: '总量',
                        data: cure_list
                    },
                    {
                        name: '累计死亡',
                        type: 'line',
                        stack: '总量',
                        data: dead_list
                    },
                ]
            };
            myec.setOption(option);
            window.onresize = myec.resize()
        }
    })
}
function get_new_cov(){
    $.ajax({
        url:'/new_cov/',
        timeout:'10000',
        success:function (data) {
            day_list_l1 = data.key;
            new_cov_list = data.value;
            var myec1 = echarts.init(document.getElementById('l2'));
            option_1 = {
                title: {
                        left:'10%',
                        text: '全国新增趋势',
                        textStyle:{
                            color:"rgba(255, 255, 255, 1)",
                        },
                    },
                tooltip: {
                            trigger: 'axis'
                        },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: {
                    type: 'category',
                    data: day_list_l1,
                    axisLine: {
                      lineStyle: {
                        color:"rgba(255, 255, 255, 1)",
                      }
                    },
                },
                yAxis: {
                    type: 'value',
                    axisLine: {
                      lineStyle: {
                        color:"rgba(255, 255, 255, 1)",
                      }
                    },
                },
                series: [{
                    name:'新增人数',
                    data: new_cov_list,
                    type: 'line'
                }]
            };
            myec1.setOption(option_1);
            window.onresize = myec1.resize();
        }
    });
}
get_new_cov();
get_all_day();
setInterval(get_new_cov,1000*10);
setInterval(get_all_day,1000*10);