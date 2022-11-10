document.addEventListener('DOMContentLoaded', () => {
    const options = {
        chart: {
            type: 'column',
            // 확대기능
            zoomType: 'xy'
        },
        // 하단 링크설정
        credits: {
            // 제거하기
            enabled: false
        },
        // 차트명
        title: {
            text: '딸기 연간 가격추이'
        },
        yAxis: {
            title: {
                text: '가격'
            }
        }
    };
    $.get('딸기 상품 연간가격(단위 2kg).csv', csv => {
        options.data = {
            csv
        };
        Highcharts.chart('container', options);
    });
});