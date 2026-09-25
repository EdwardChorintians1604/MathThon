// ===============================
// DATA (ISI SESUAI GAMBAR ANDA)
// ===============================
const countries = [
"Singapore","Chinese Taipei","Korea, Rep. of","Hong Kong SAR","Japan","Macao SAR",
"Chinese Taipei (again?)","Lithuania","Turkey","England","Poland","Ireland",
"Romania","Netherlands","Latvia","Italy","Norway","Czech Republic",
"Sweden","Bulgaria","Finland","Australia","Germany","Denmark","Serbia",
"Belgium (Flemish)","Hungary","United States","Portugal","Slovak Republic",
"Cyprus","Slovenia","Italy (again?)","Armenia","Albania","Canada",
"United Arab Emirates","Spain","Georgia","Azerbaijan","New Zealand",
"Belgium (French)","Kazakhstan","France","Montenegro","North Macedonia",
"Qatar","Bahrain","Bosnia & Herzegovina","Chile","Uzbekistan","Jordan",
"Iran","Oman","Saudi Arabia","Brazil","Morocco","Kuwait","South Africa"
];

const scores = [
610,600,595,590,580,575,560,555,550,545,540,538,
536,534,532,530,528,526,
524,523,522,521,520,519,518,
517,516,514,512,511,
509,508,507,505,503,501,
499,497,495,492,490,
488,487,485,480,475,470,
460,455,445,435,430,420,
400,380,360
];

// ===============================
// HISTOGRAM CONFIGURATION
// ===============================

// Function to create histogram bins
function createHistogramData(scores, binSize = 50) {
    const minScore = Math.min(...scores);
    const maxScore = Math.max(...scores);
    const bins = [];
    const labels = [];
    const counts = [];

    for (let i = Math.floor(minScore / binSize) * binSize; i <= maxScore; i += binSize) {
        bins.push({ min: i, max: i + binSize, count: 0 });
        labels.push(`${i}-${i + binSize}`);
    }

    scores.forEach(score => {
        const binIndex = Math.floor((score - bins[0].min) / binSize);
        if (binIndex >= 0 && binIndex < bins.length) {
            bins[binIndex].count++;
        }
    });

    bins.forEach(bin => counts.push(bin.count));

    return { labels, counts };
}

const histogramData = createHistogramData(scores);

// Generate gradient color for bars
function getGradient(ctx, chartArea) {
    const gradient = ctx.createLinearGradient(0, chartArea.bottom, 0, chartArea.top);
    gradient.addColorStop(0, "#9acd32");
    gradient.addColorStop(0.5, "#1e90ff");
    gradient.addColorStop(1, "#4b0082");
    return gradient;
}

let timssChart = null;

function initTIMSSChart() {
    if (timssChart) return; // Prevent multiple initializations
    const ctx = document.getElementById('timssChart');
    if (!ctx) return;
    const context = ctx.getContext('2d');
    timssChart = new Chart(context, {
        type: 'bar',
        data: {
            labels: histogramData.labels,
            datasets: [{
                label: "Number of Countries",
                data: histogramData.counts,
                backgroundColor: function(context) {
                    const chart = context.chart;
                    const {ctx, chartArea} = chart;

                    if (!chartArea) return "#888";
                    return getGradient(ctx, chartArea);
                },
                borderWidth: 1,
                borderColor: '#333'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    enabled: true,
                    callbacks: {
                        title: function(context) {
                            return `Score Range: ${context[0].label}`;
                        },
                        label: function(context) {
                            return `Countries: ${context.parsed.y}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: "Score Range",
                        font: { size: 14 }
                    },
                    ticks: {
                        font: { size: 10 }
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: "Number of Countries",
                        font: { size: 14 }
                    },
                    ticks: {
                        stepSize: 1
                    }
                }
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
                if (target.classList.contains('active') && target.querySelector('#timssChart')) {
                    initTIMSSChart();
                }
            }
        });
    });

    const slides = document.querySelectorAll('.slide');
    slides.forEach(slide => {
        observer.observe(slide, { attributes: true });
    });
});
