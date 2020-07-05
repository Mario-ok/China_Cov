function randomData() {
    return Math.round(Math.random()*500);
}
function map() {
    $.ajax({
        url: '/china/',
        timeout: '10000',
        success: function (data) {
            optionMap = {
            title: {
                text: '全国新增人数',
                subtext: '',
                textStyle: {
                    color: 'rgb(255,255,255)',
                },
                x: 'center',
            },
            tooltip: {
                trigger: 'item'
            },
            //左侧小导航图标
            visualMap: {
                show: true,
                left: 'left',
                top: 'bottom',
                splitList: [
                    {start: 10, end: 20}, {start: 5, end: 10},
                    {start: 1, end: 5}, {start: 0, end: 0},

                ],
                textStyle: {
                    color: 'rgb(255,255,255)',
                },
                color: ['#5475f5', '#9feaa5', '#85daef', '#fff',]
            },

            //配置属性
            series: [{
                name: '数据',
                type: 'map',
                mapType: 'china',
                textStyle: {
                    color: 'rgb(255,255,255)',
                },
                roam: false,
                label: {
                    normal: {
                        show: true  //省份名称
                    },
                    emphasis: {
                        show: false
                    }
                },
                data: data  //数据
            }]
        };
            var myChart = echarts.init(document.getElementById('c2'));
            myChart.setOption(optionMap);
            window.onresize = myChart.resize();
        }
    })
}
map();
setInterval(map, 1000*10);