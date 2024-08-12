// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    // Add interactive features here
});

// Example: Add smooth scrolling to internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add more JavaScript functionality as needed

// static/js/main.js

// Email form submission
const emailForm = document.getElementById('email-form');
if (emailForm) {
    emailForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        // Here you would typically send an AJAX request to your backend
        // For demonstration, we'll just log the values
        console.log('Sending email:', {
            name,
            email,
            message
        });
        alert('Email sent successfully!');
        emailForm.reset();
    });
}

// Add this to your static/js/main.js file

// University admission rates chart
const admissionChart = document.getElementById('admissionChart');
if (admissionChart) {
    const ctx = admissionChart.getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
            datasets: [{
                label: 'University Admission Rate',
                data: [75, 78, 80, 82, 85, 87, 89, 90, 92, 95],
                borderColor: 'rgb(0, 102, 204)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    // max: 100
                }
            }
        }
    });
}

// Add this to your static/js/main.js file

function initMap() {
    const mapDiv = document.getElementById('google-map');
    if (mapDiv) {
        const githumu = {
            lat: -0.7156,
            lng: 36.7508
        }; // Replace with actual coordinates
        const map = new google.maps.Map(mapDiv, {
            zoom: 15,
            center: githumu,
        });
        new google.maps.Marker({
            position: githumu,
            map: map,
            title: 'Githumu High School'
        });
    }
}
