const API_BASE = 'http://127.0.0.1:5000/api';
let currentYear = 2024;

async function fetchDrivers(year) {
    const response = await fetch(`${API_BASE}/seasons/${year}/drivers`);
    return await response.json();
}

async function fetchDriverStandings(year) {
    const response = await fetch(`${API_BASE}/seasons/${year}/driver-standings`);
    return await response.json();
}

async function fetchHeadshots(year) {
    const response = await fetch(`${API_BASE}/seasons/${year}/headshots`);
    return await response.json();
}

async function renderDriverCards(year) {
    const drivers = await fetchDrivers(year);
    const standingsData = await fetchDriverStandings(year);
    const headshots = await fetchHeadshots(year);
    const standings = standingsData[0]?.DriverStandings || [];

    const grid = document.querySelector('.driver-grid');
    grid.innerHTML = '';

    drivers.forEach(driver => {
        const standing = standings.find(s => s.Driver.driverId === driver.driverId);
        const pos = standing?.position || '-';
        const pts = standing?.points || '-';
        const team = standing?.Constructors[0]?.name || '-';
        const abbr = driver.code || '';
        const photo = headshots[abbr] || '';

        const avatarContent = photo
            ? `<img src="${photo}" alt="${driver.givenName}" style="width:100%;height:100%;object-fit:cover;border-radius:50%;">`
            : `<svg viewBox="0 0 24 24"><path d="M12 2a9 9 0 0 0-9 9c0 3.6 2.1 6.7 5.2 8.1l.8-2.1A7 7 0 0 1 5 11a7 7 0 0 1 7-7 7 7 0 0 1 7 7c0 2.6-1.4 4.9-3.5 6.1l.9 2A9 9 0 0 0 21 11a9 9 0 0 0-9-9zm-1 8h2v5h-2v-5zm0-3h2v2h-2V7z"/></svg>`;

        const card = `
        <div class="driver-card">
            <span class="driver-number">${driver.permanentNumber || '-'}</span>
            <div class="driver-avatar-wrapper">
                <div class="driver-avatar">
                    ${avatarContent}
                </div>
            </div>
            <div class="driver-info">
                <div class="driver-name">
                    <span>${driver.givenName}</span>${driver.familyName}
                </div>
                <div class="driver-team">${team}</div>
            </div>
            <div class="card-footer-stats">
                <div class="card-footer-item">
                    <span>Pos</span>
                    <span>${pos}</span>
                </div>
                <div class="card-footer-item">
                    <span>PTS</span>
                    <span>${pts}</span>
                </div>
            </div>
        </div>`;
        grid.innerHTML += card;
    });
}

document.querySelectorAll('.season-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        document.querySelectorAll('.season-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        currentYear = parseInt(this.textContent);
        renderDriverCards(currentYear);
    });
});

renderDriverCards(currentYear);