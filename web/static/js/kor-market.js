(async () => {

    const topology = await fetch(
      'https://code.highcharts.com/mapdata/countries/kr/kr-all.topo.json'
    ).then(response => response.json());
  
    // Initialize the chart
    Highcharts.mapChart('container', {
  
      chart: {
        map: topology
      },
  
      title: {
        text: '가까운 농산물 도매시장 위치를 확인해보세요!'
      },
  
      accessibility: {
        description: 'Map where city locations have been defined using latitude/longitude.'
      },
  
      mapNavigation: {
        enabled: true
      },
  
      tooltip: {
        headerFormat: '',
        pointFormat: '<b>{point.name}</b><br>Lat: {point.lat}, Lon: {point.lon}'
      },
  
      series: [{
        // Use the gb-all map with no data as a basemap
        name: 'South Korea',
        borderColor: '#A0A0A0',
        nullColor: 'rgba(200, 200, 200, 0.3)',
        showInLegend: false
      }, {
        name: 'Separators',
        type: 'mapline',
        nullColor: '#707070',
        showInLegend: false,
        enableMouseTracking: false,
        accessibility: {
          enabled: false
        }
      }, {
        // Specify points using lat/lon
        type: 'mappoint',
        name: 'Cities',
        accessibility: {
          point: {
            valueDescriptionFormat: '{xDescription}. Lat: {point.lat:.2f}, lon: {point.lon:.2f}.'
          }
        },
        color: Highcharts.getOptions().colors[1],
        data: [{
          name: 'Busan',
          lat: 35.1796,
          lon: 129.0756
        }, 
        ]
      }]
    });
  
  })();
  