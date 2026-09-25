document.addEventListener('DOMContentLoaded', async () => {
  const CSV_URL = '/static/chart/api/education_data/kelayakan-pendidikan-indonesia.csv';
  const canvas = document.getElementById('enrolmentChart');
  if (!canvas) return; // Keluar jika elemen canvas tidak ditemukan

  // 1. Tambahkan CSS secara dinamis ke head
  const style = document.createElement('style');
  style.textContent = `
    .grafik {
      background:#fff;
      border-radius: 12px;
      box-shadow: 0 1px 6px rgba(0,0,0,0.04);
      width:100%;
      height:100%;
    }
    .chart-responsive {
      min-height:420px;
      max-height:600px;
      height:52vw;
      max-width:100%;
      position:relative;
    }
    @media (max-width: 576px) {
      .chart-responsive {
        height: 450px; /* Tinggi tetap untuk layar kecil */
      }
      .grafik {
      background:#fff;
      border-radius: 12px;
      box-shadow: 0 1px 6px rgba(0,0,0,0.04);
      width:100%;
      height:100%;
    }
    }
  `;
  document.head.appendChild(style);

  const ctx = canvas.getContext('2d');

  let errorDiv = document.getElementById('csvError');
  if (!errorDiv) {
    errorDiv = document.createElement('div');
    errorDiv.id = 'csvError';
    errorDiv.style.color = 'red';
    errorDiv.style.marginTop = '16px';
    errorDiv.style.fontWeight = 'bold';
    canvas.parentNode.appendChild(errorDiv);
  }
  errorDiv.textContent = 'Memuat data grafik...';

  function setupExportButton(chart) {
    const actionsContainer = document.getElementById('chart-actions');
    if (!actionsContainer) return;

    let exportBtn = document.createElement('button');
    exportBtn.id = 'exportChartBtn';
    exportBtn.className = 'btn btn-success mb-2';
    exportBtn.innerHTML = '<i class="fas fa-download me-2"></i>Download Grafik (PNG)';
    actionsContainer.appendChild(exportBtn);

    exportBtn.onclick = () => {
      const url = chart.toBase64Image();
      const a = document.createElement('a');
      a.href = url;
      a.download = "grafik_pendidikan_provinsi.png";
      a.click();
    };
  }

  function tooltipNumber(context) {
    const value = context.raw;
    return value !== null && value !== undefined
      ? value.toLocaleString('id-ID', { maximumFractionDigits: 0 })
      : '-';
  }

  try {
    const response = await fetch(CSV_URL);
    if (!response.ok) throw new Error('Gagal memuat CSV');
    const text = await response.text();

    // Split CSV (dukung , atau ;)
    const delimiter = text.includes(';') ? ';' : ',';
    const rows = text.trim().split(/\r?\n/).map(line => line.split(delimiter));

    const headers = rows[0].map(h => h.trim().toLowerCase().replace(/[_\s]+/g, ''));
    console.log('Header CSV:', headers);

    // Fungsi bantu cari kolom fleksibel
    const findCol = keyword =>
      headers.findIndex(h => h.includes(keyword.toLowerCase().replace(/\s+/g, '')));

    const provinsiIndex = findCol('provinsi');
    const siswaIndex = findCol('siswa');
    const putusIndex = findCol('putus');
    const mengulangIndex = findCol('mengulang');

    if (provinsiIndex === -1 || siswaIndex === -1 || putusIndex === -1 || mengulangIndex === -1) {
      throw new Error(`Kolom CSV tidak lengkap. Kolom ditemukan: ${headers.join(', ')}`);
    }

    const provinsi = [];
    const jumlahSiswa = [];
    const jumlahPutusSekolah = [];
    const jumlahMengulang = [];

    for (let i = 1; i < rows.length; i++) {
      const row = rows[i];
      if (row.length < headers.length) continue;

      provinsi.push(row[provinsiIndex]);
      jumlahSiswa.push(Number(row[siswaIndex].replace(/[^0-9.]/g, '')) || 0);
      jumlahPutusSekolah.push(Number(row[putusIndex].replace(/[^0-9.]/g, '')) || 0);
      jumlahMengulang.push(Number(row[mengulangIndex].replace(/[^0-9.]/g, '')) || 0);
    }

    if (provinsi.length === 0) {
      errorDiv.textContent = 'Data CSV kosong.';
      return;
    }

    errorDiv.textContent = '';

    const chart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: provinsi,
        datasets: [
          {
            label: 'Jumlah Siswa',
            data: jumlahSiswa,
            borderColor: 'rgba(54, 162, 235, 1)',
            backgroundColor: 'rgba(54, 162, 235, 0.6)',
            borderWidth: 1
          },
          {
            label: 'Putus Sekolah',
            data: jumlahPutusSekolah,
            borderColor: 'rgba(255, 99, 132, 1)',
            backgroundColor: 'rgba(255, 99, 132, 0.6)',
            borderWidth: 1
          },
          {
            label: 'Mengulang',
            data: jumlahMengulang,
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.6)',
            borderWidth: 1
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        indexAxis: 'y',
        plugins: {
          legend: {
            position: 'top',
            labels: { usePointStyle: true }
          },
          title: {
            display: true,
            text: 'Data Pendidikan per Provinsi (Jumlah Siswa, Putus Sekolah, Mengulang)'
          },
          tooltip: {
            callbacks: {
              label: context => {
                let label = context.dataset.label || '';
                if (label) label += ': ';
                return label + tooltipNumber(context);
              }
            }
          }
        },
        scales: {
          x: {
            beginAtZero: true,
            title: { display: true, text: 'Jumlah' },
            ticks: {
              callback: val => val.toLocaleString('id-ID')
            }
          },
          y: {
            title: { display: true, text: 'Provinsi' }
          }
        }
      }
    });

    setupExportButton(chart);
  } catch (err) {
    console.error('Error:', err);
    errorDiv.textContent = `Gagal membaca atau memproses CSV: ${err.message}`;
  }
});
