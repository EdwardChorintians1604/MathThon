// Data pendidikan per provinsi (data contoh)
const educationData = {
    provinsi: ['DKI Jakarta', 'Jawa Barat', 'Jawa Timur', 'Yogyakarta', 'Bali', 'Sumatera Utara', 'Sulawesi Selatan', 'Kalimantan Timur'],
    apm: [95.2, 88.7, 87.3, 92.8, 90.5, 85.1, 83.4, 89.2], // Angka Partisipasi Murni
    rataLamaSekolah: [11.5, 9.2, 8.8, 10.8, 10.2, 8.5, 8.3, 9.8],
    melekHuruf: [99.2, 97.5, 96.8, 98.9, 98.5, 96.2, 95.8, 97.8]
};

// Variabel global
let currentChartType = 'bar';
let currentIndicator = 'apm';
let educationChart = null;

const indicatorLabels = {
    'apm': 'Angka Partisipasi Murni (%)',
    'rataLamaSekolah': 'Rata-rata Lama Sekolah (tahun)',
    'melekHuruf': 'Tingkat Melek Huruf (%)'
};

const indicatorUnits = {
    'apm': '%',
    'rataLamaSekolah': ' tahun',
    'melekHuruf': '%'
};

// Warna untuk setiap provinsi
const provinceColors = [
    'rgba(255, 99, 132, 0.8)',
    'rgba(54, 162, 235, 0.8)',
    'rgba(255, 205, 86, 0.8)',
    'rgba(75, 192, 192, 0.8)',
    'rgba(153, 102, 255, 0.8)',
    'rgba(255, 159, 64, 0.8)',
    'rgba(199, 199, 199, 0.8)',
    'rgba(83, 102, 255, 0.8)'
];

// Inisialisasi chart saat dokumen siap
document.addEventListener('DOMContentLoaded', function() {
    initializeChart();
    setupEventListeners();
});

function initializeChart() {
    const ctx = document.getElementById('educationChart').getContext('2d');
    
    // Hancurkan chart sebelumnya jika ada
    if (educationChart) {
        educationChart.destroy();
    }
    
    const config = {
        type: currentChartType,
        data: {
            labels: educationData.provinsi,
            datasets: [{
                label: indicatorLabels[currentIndicator],
                data: educationData[currentIndicator],
                backgroundColor: currentChartType === 'bar' ? provinceColors : 'rgba(54, 162, 235, 0.8)',
                borderColor: currentChartType === 'bar' ? 
                    provinceColors.map(color => color.replace('0.8', '1')) : 
                    'rgba(54, 162, 235, 1)',
                borderWidth: 2,
                fill: currentChartType === 'line',
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const value = context.parsed.y;
                            const unit = indicatorUnits[currentIndicator];
                            return `${context.dataset.label}: ${value}${unit}`;
                        }
                    }
                },
                title: {
                    display: true,
                    text: indicatorLabels[currentIndicator],
                    font: {
                        size: 16,
                        weight: 'bold'
                    },
                    padding: 20
                }
            },
            scales: {
                y: {
                    beginAtZero: currentIndicator !== 'rataLamaSekolah',
                    min: currentIndicator === 'rataLamaSekolah' ? 7 : 0,
                    max: currentIndicator === 'melekHuruf' ? 100 : undefined,
                    title: {
                        display: true,
                        text: indicatorLabels[currentIndicator],
                        font: {
                            weight: 'bold',
                            size: 12
                        }
                    },
                    grid: {
                        color: 'rgba(0,0,0,0.1)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Provinsi',
                        font: {
                            weight: 'bold',
                            size: 12
                        }
                    },
                    grid: {
                        display: false
                    }
                }
            },
            animation: {
                duration: 1000,
                easing: 'easeOutQuart'
            }
        }
    };

    educationChart = new Chart(ctx, config);
    updateSummary();
    updateActiveButtons();
}

// Setup event listeners untuk interaksi
function setupEventListeners() {
    // Tambahkan event listener untuk resize window
    window.addEventListener('resize', function() {
        if (educationChart) {
            educationChart.resize();
        }
    });
}

// Fungsi untuk mengganti tipe chart
function changeChartType(type) {
    currentChartType = type;
    initializeChart();
}

// Fungsi untuk mengganti indikator
function toggleIndikator() {
    const indicators = ['apm', 'rataLamaSekolah', 'melekHuruf'];
    const currentIndex = indicators.indexOf(currentIndicator);
    currentIndicator = indicators[(currentIndex + 1) % indicators.length];
    initializeChart();
}

// Fungsi untuk mengganti indikator secara spesifik
function changeIndicator(indicator) {
    if (indicatorLabels.hasOwnProperty(indicator)) {
        currentIndicator = indicator;
        initializeChart();
    }
}

// Update tombol aktif
function updateActiveButtons() {
    const buttons = document.querySelectorAll('.control-btn');
    buttons.forEach(btn => {
        btn.classList.remove('active');
        
        // Cek jika ini adalah tombol chart type
        if (btn.onclick && btn.onclick.toString().includes(`changeChartType('${currentChartType}')`)) {
            btn.classList.add('active');
        }
    });
}

// Update summary
function updateSummary() {
    const data = educationData[currentIndicator];
    const maxValue = Math.max(...data);
    const minValue = Math.min(...data);
    const maxProvince = educationData.provinsi[data.indexOf(maxValue)];
    const minProvince = educationData.provinsi[data.indexOf(minValue)];
    const average = (data.reduce((a, b) => a + b, 0) / data.length).toFixed(2);
    const unit = indicatorUnits[currentIndicator];
    
    // Analisis tambahan
    const aboveAverage = data.filter(value => value > parseFloat(average)).length;
    const percentageAboveAverage = ((aboveAverage / data.length) * 100).toFixed(1);

    document.getElementById('educationSummary').innerHTML = `
        <h3>📊 Analisis ${indicatorLabels[currentIndicator]}</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;">
            <div>
                <p><strong>🏆 Provinsi Tertinggi:</strong><br>${maxProvince} (${maxValue}${unit})</p>
                <p><strong>📉 Provinsi Terendah:</strong><br>${minProvince} (${minValue}${unit})</p>
            </div>
            <div>
                <p><strong>📐 Rata-rata Nasional:</strong><br>${average}${unit}</p>
                <p><strong>📈 Di Atas Rata-rata:</strong><br>${aboveAverage} provinsi (${percentageAboveAverage}%)</p>
            </div>
        </div>
        <p style="margin-top: 15px; padding-top: 15px; border-top: 1px solid #ddd;">
            <strong>📏 Selisih Tertinggi-Terendah:</strong> ${(maxValue - minValue).toFixed(2)}${unit}
        </p>
    `;
}

// Fungsi untuk mengekspor data sebagai CSV
function exportData() {
    const headers = ['Provinsi', indicatorLabels[currentIndicator]];
    const csvData = educationData.provinsi.map((provinsi, index) => {
        return [provinsi, educationData[currentIndicator][index]];
    });
    
    const csvContent = [headers, ...csvData]
        .map(row => row.join(','))
        .join('\n');
    
    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.setAttribute('hidden', '');
    a.setAttribute('href', url);
    a.setAttribute('download', `data_pendidikan_${currentIndicator}.csv`);
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

// Fungsi untuk mendapatkan data chart saat ini
function getCurrentChartData() {
    return {
        type: currentChartType,
        indicator: currentIndicator,
        data: educationData[currentIndicator],
        labels: educationData.provinsi,
        indicatorLabel: indicatorLabels[currentIndicator]
    };
}

// Fungsi untuk update data secara dinamis
function updateChartData(newData) {
    if (newData && newData.provinsi && newData[currentIndicator]) {
        educationData.provinsi = newData.provinsi;
        educationData[currentIndicator] = newData[currentIndicator];
        initializeChart();
    }
}