const years = [2000, 2003, 2006, 2009, 2012, 2015, 2018, 2022];

    // Contoh data – ganti sesuai data sebenarnya
    const readingScores = [ /* mis: 402, 395, 390, 402, 398, 371, 371, 359 */ ];
    const mathScores    = [ /* mis: ..., ..., ..., ..., ..., 376, 379, 366 */ ];
    const scienceScores = [ /* mis: ..., ..., ..., ..., ..., 379, 396, 383 */ ];

    let pisaChart = null;

    function initPISAChart() {
        if (pisaChart) return; // Prevent multiple initializations
        const ctx = document.getElementById('pisaChart');
        if (!ctx) return;
        const context = ctx.getContext('2d');
        pisaChart = new Chart(context, {
            type: 'line',
            data: {
                labels: years,
                datasets: [
                    {
                        label: 'Reading (Membaca)',
                        data: readingScores,
                        borderColor: 'rgba(255, 99, 132, 1)',
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        tension: 0.3
                    },
                    {
                        label: 'Mathematics (Matematika)',
                        data: mathScores,
                        borderColor: 'rgba(54, 162, 235, 1)',
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        tension: 0.3
                    },
                    {
                        label: 'Science (Sains)',
                        data: scienceScores,
                        borderColor: 'rgba(75, 192, 192, 1)',
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        tension: 0.3
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    tooltip: { mode: 'index', intersect: false },
                    legend: { position: 'top' }
                },
                interaction: { mode: 'nearest', axis: 'x', intersect: false },
                scales: {
                    x: { title: { display: true, text: 'Tahun PISA' } },
                    y: { title: { display: true, text: 'Skor' }, beginAtZero: false }
                }
            }
        });
    }

    // Initialize chart when slide becomes active
    document.addEventListener('DOMContentLoaded', function() {
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
                    const target = mutation.target;
                    if (target.classList.contains('active') && target.querySelector('#pisaChart')) {
                        initPISAChart();
                    }
                }
            });
        });

        const slides = document.querySelectorAll('.slide');
        slides.forEach(slide => {
            observer.observe(slide, { attributes: true });
        });
    });
