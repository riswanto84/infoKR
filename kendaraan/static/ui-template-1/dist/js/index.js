
$('#btn-slider').click(function(){
    if($('#sliders').hasClass('active')){
        $('#sliders').removeClass('active');
        $('#sliders-background').removeClass('active');
    } else {
        $('#sliders').addClass('active');
        $('#sliders-background').addClass('active');
    }
});


$('#sliders-background').click(function(){
    $('#sliders').removeClass('active');
    $('#sliders-background').removeClass('active');
});


// this for char one type bar
var ctx = document.getElementById('myChartOne').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
        datasets: [{
            label: ' Data Kontrak Tahun 2022',
            data: [12, 19, 3, 5, 2, 3, 10, 19, 3, 50, 2, 3, 10],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgb(60, 179, 113, 0.2)',
                'rgba(245, 40, 145, 0.2)',
                'rgba(147, 144, 215, 0.2)',
                'rgba(197, 95, 208, 0.2)',
                'rgba(95, 142, 208, 0.2)',
                'rgba(163, 208, 95, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgb(60, 179, 113, 1)',
                'rgba(245, 40, 145, 1)',
                'rgba(147, 144, 215, 1)',
                'rgba(197, 95, 208, 1)',
                'rgba(95, 142, 208, 1)',
                'rgba(163, 208, 95, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// this for chart Two type line
var ctx = document.getElementById('myChartTwo').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
        datasets: [{
            label: ' Data Kontrak Tahun 2022',
            data: [12, 19, 3, 5, 2, 3, 10, 19, 3, 50, 2, 3, 10],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgb(60, 179, 113, 0.2)',
                'rgba(245, 40, 145, 0.2)',
                'rgba(147, 144, 215, 0.2)',
                'rgba(197, 95, 208, 0.2)',
                'rgba(95, 142, 208, 0.2)',
                'rgba(163, 208, 95, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgb(60, 179, 113, 1)',
                'rgba(245, 40, 145, 1)',
                'rgba(147, 144, 215, 1)',
                'rgba(197, 95, 208, 1)',
                'rgba(95, 142, 208, 1)',
                'rgba(163, 208, 95, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

$(document).ready(function () {
    $('#dtBasicExample').DataTable();
    $('.dataTables_length').addClass('bs-select');
});