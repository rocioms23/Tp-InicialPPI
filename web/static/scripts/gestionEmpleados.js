document.addEventListener('DOMContentLoaded', function () {
    document.body.classList.add('slide-out-right');
    document.querySelectorAll('nav a').forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelectorAll('nav a').forEach(l => l.classList.remove('active', 'bg-gray-800', 'text-white'));
            this.classList.add('active', 'bg-gray-800', 'text-white','py-1','px-2','rounded-xl');
            document.body.classList.add('slide-out-left');
            setTimeout(function () {
                window.location.href = link.getAttribute('href');
            }, 300);
        });

    });
});